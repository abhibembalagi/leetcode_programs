class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if (target < nums[0]):
            return 0
        if target in nums:
            return nums.index(target)
        else:
            for i in range(len(nums)) :
                if (nums[i] - target)> 0:
                    return i
            else:
                return len(nums)
