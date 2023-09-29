from typing import List

from .utilities import hash_sha256


class MerkleTree:
    def __init__(self, hashed_data: list[str] = []):
        self.leaves: List[str] = hashed_data
        self.levels: List[List[str]] = [self.leaves]
        self.build()

    def build(self):
        level = self.leaves

        while len(level) > 1:
            # print(level)
            hashed_level = self.hash_level(level)
            # print(hashed_level)
            self.levels.append(hashed_level)
            level = self.levels[-1]
            # print(level)

    def hash_level(self, level: List[str]) -> List[str]:
        hashed_level = []
        for i in range(0, len(level), 2):
            if i + 1 == len(level):
                hashed_level.append(self.hash_func(level[i] + level[i]))
            else:
                hashed_level.append(self.hash_func(level[i] + level[i + 1]))
        return hashed_level

    @staticmethod
    def hash_func(data):
        return hash_sha256(data)

    def root(self) -> str | None:
        # print(self.leaves)
        if self.levels is None or self.levels == [[]] or self.leaves == []:
            return None
        return self.levels[-1][0]

    def verify(self, leaf_hash: str) -> bool:
        if leaf_hash not in self.leaves:
            return False
        index = self.leaves.index(leaf_hash)
        current_hash = self.leaves[index]
        for i in range(len(self.levels) - 1):
            if index % 2 == 0:
                current_hash = self.hash_func(current_hash + self.levels[i][index + 1])
            else:
                current_hash = self.hash_func(self.levels[i][index - 1] + current_hash)
            index //= 2
        return current_hash == self.root()

    def __str__(self) -> str:
        return f"{self.root()}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(root={self.root()})"
