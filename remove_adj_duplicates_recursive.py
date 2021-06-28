class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr=[]
        for char in s:
            if len(arr)==0:
                arr.append(char)
            else:
                if arr[-1]==char:
                    arr.pop()
                else:
                    arr.append(char)
        return("".join(arr))
        
