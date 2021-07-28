"""
通过分批旋转数组来获得结果
"""


def rotate(self, nums: list, k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    while k > len(nums):
        k -= len(nums)
    nums.reverse()
    temp = nums[:k]
    temp.reverse()
    nums[: k] = temp.copy()
    temp = nums[k:]
    temp.reverse()
    nums[k:] = temp.copy()
