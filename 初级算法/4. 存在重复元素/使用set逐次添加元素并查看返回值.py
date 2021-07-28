"""
python set.add() 的返回值都为 None，故不支持这种方式
"""
# class Solution:
#     def containsDuplicate(self, nums) -> bool:
#         temp = set()
#         for num in nums:
#             if not (temp.add(num)):
#                 return True
#         return False
#
#
# s = Solution()
# print(s.containsDuplicate([1, 2, 3, 4]))
temp = set()
print(temp.add(1))
print(temp.add(2))
print(temp.add(1))
print(temp)
