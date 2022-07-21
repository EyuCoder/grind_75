# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        left = 1
        for n in nums:
            res.append(left)
            left *= n

        right = 1
        for i in reversed(range(len(nums))):
            res[i] *= right
            right *= nums[i]

        return res
