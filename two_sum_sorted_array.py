
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first_number={}
        for n,m in enumerate(numbers):
            sec_number = target -m
            if sec_number in first_number:
                return (int(first_number[sec_number])+1,(n+1))
            first_number[m]=n
        return  []
