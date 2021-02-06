class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_list=[]
        new_list=nums1+nums2
        new_list.sort()
        length=len(new_list)
        if (length % 2 == 0):
            k= length // 2
            return((new_list[k]+new_list[k-1])/2)
        else:
            k= length // 2
            return(new_list[k])
