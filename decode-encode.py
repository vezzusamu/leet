import sys
from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            l = len(s)
            encoded += str(l) + '.' + s
        return encoded

    def _read_dim(self, s: str) -> tuple[int, str]:
        pos = 0
        digits = 0
        while s[pos] != '.':
            digits += 1
            pos += 1
        dim = int(s[0: digits])
        return dim, s[digits + 1: len(s)]

    def _read_word(self, s: str, dim:int) -> tuple[str, str]:
        return s[0: dim],s[dim: len(s)]

    def decode(self, s: str) -> List[str]:
        decoded = []
        while (len(s) > 0):
            word_dim, s = self._read_dim(s)
            word, s = self._read_word(s, word_dim)
            decoded.append(word)
        return decoded