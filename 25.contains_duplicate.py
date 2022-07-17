# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # using set
        hashset = set()

        for i in nums:
            if i in hashset:
                return True
            else:
                hashset.add(i)
        return False

        # using dictionary
        # count = {}

        # for i in nums:
        #     if count.get(i, 0) > 0:
        #         return True
        #     else:
        #         count[i] = 1 + count.get(i, 0)
        # return False
