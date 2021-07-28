"""
构建临时数组存放数据
"""


def rotate(nums, k) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    temp = nums.copy()
    for i in range(len(nums)):
        new_i = i + k
        while new_i > len(nums):
            new_i -= len(nums)
        if new_i < len(nums):
            nums[new_i] = temp[i]
        else:
            nums[new_i - len(nums)] = temp[i]
