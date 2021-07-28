"""
构建环形数组，一次跳转 i+k 次，并用 hold 存放跳转的数据
"""


def rotate(self, nums: list, k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    hold = nums[0]
    index = 0
    length = len(nums)
    visited = [False for j in range(length)]
    i = 0
    while i < length:
        index = (index + k) % length
        if visited[index]:
            index = (index + 1) % length
            hold = nums[index]
            i -= 1
        else:
            visited[index] = True
            temp = nums[index]
            nums[index] = hold
            hold = temp
        i += 1
