class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = sum(range(len(nums)+1)) - sum(nums)
        return n
        