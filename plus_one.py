#digits should not be greater than 9 after adding 1 at end and add carry 1 to prev numbers
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l=len(digits)-1
        while l>=0:
            if digits[l]==9:
                digits[l]=0
            else:
                digits[l]+=1
                return digits
            l-=1
        return [1]+digits
