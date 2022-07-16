# https://leetcode.com/problems/valid-anagram/

from multiprocessing.dummy import Array


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # one liner
        # return sorted(s) == sorted(t)

        if len(s) != len(t):
            return False

        table = [0] * 128

        for c in s:
            table[ord(c)] += 1

        for c in t:
            table[ord(c)] -= 1
            if table[ord(c)] < 0:
                return False
        return True
