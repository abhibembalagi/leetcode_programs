class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        index_list=[]
        if target not in nums:
            return([-1,-1])
        for i  in range(len(nums)):
            if target == nums[i]:
                index_list.append(i)
        return ([index_list[0],index_list[-1]])
