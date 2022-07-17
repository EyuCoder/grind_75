# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore's method
        count = res = 0

        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)

        return res

        # count = {}
        # max_count = res = 0

        # for i in nums:
        #     count[i] = 1 + count.get(i, 0)
        #     res = i if count[i] > max_count else res
        #     max_count = max(max_count, count[i])
        # return res
