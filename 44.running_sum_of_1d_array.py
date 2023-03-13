# https://leetcode.com/problems/running-sum-of-1d-array

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum=0
        running_sum=[]
        for i in nums:
            sum+=i
            running_sum.append(sum)
        return running_sum