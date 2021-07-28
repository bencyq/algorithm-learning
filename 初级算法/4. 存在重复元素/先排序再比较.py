class Solution:
    def containsDuplicate(self, nums) -> bool:
        nums.sort()
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] - nums[i - 1] == 0:
                return True
        return False


s = Solution()
print(s.containsDuplicate([1,2,3,4]))
