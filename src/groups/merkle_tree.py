import hashlib


class MerkleTree:
    def __init__(self, hashed_data: list[str]):
        self.leaves = hashed_data
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

    def verify(self, leaf_hash, root_hash):
        if leaf_hash not in self.leaves:
            return False
        index = self.leaves.index(leaf_hash)
        current_hash = self.leaves[index]
        for i in range(1, len(self.levels)):
            if index % 2 == 0:
                current_hash = hashlib.sha256((current_hash + self.levels[i - 1][index + 1]).encode()).hexdigest()
            else:
                current_hash = hashlib.sha256((self.levels[i - 1][index - 1] + current_hash).encode()).hexdigest()
            index //= 2
        return current_hash == root_hash