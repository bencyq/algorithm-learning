"""
用set去重，再判断长度
"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        temp = set(nums)
        if len(temp) == len(nums):
            return False
        else:
            return True
