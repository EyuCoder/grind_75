# https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        table = set()
        for c in s:
            if c not in table:
                table.add(c)
            else:
                table.remove(c)
        if len(table) != 0:
            return len(s) - len(table) + 1
        else:
            return len(s)
