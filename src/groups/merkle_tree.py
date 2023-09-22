import hashlib


class MerkleTree:
    def __init__(self, data):
        self.data = data
        self.leaves = [hashlib.sha256(d.encode()).hexdigest() for d in data]
        self.levels = [self.leaves]

    def build(self):
        while len(self.levels[-1]) > 1:
            level = []
            for i in range(0, len(self.levels[-1]), 2):
                if i + 1 < len(self.levels[-1]):
                    level.append(hashlib.sha256((self.levels[-1][i] + self.levels[-1][i + 1]).encode()).hexdigest())
                else:
                    level.append(self.levels[-1][i])
            self.levels.append(level)

    def root(self):
        return self.levels[-1][0]

    def verify(self, data, root_hash):
        if hashlib.sha256(data.encode()).hexdigest() not in self.leaves:
            return False
        index = self.leaves.index(hashlib.sha256(data.encode()).hexdigest())
        current_hash = self.leaves[index]
        for i in range(len(self.levels) - 1):
            if index % 2 == 0:
                current_hash = hashlib.sha256((current_hash + self.levels[-i - 2][index + 1]).encode()).hexdigest()
            else:
                current_hash = hashlib.sha256((self.levels[-i - 2][index - 1] + current_hash).encode()).hexdigest()
            index //= 2
        return current_hash == root_hash