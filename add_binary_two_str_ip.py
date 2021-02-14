class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l1=len(a)-1
        l2=len(b)-1
        res=""
        carry=0
        while l1>=0 or l2>=0:
            if l1>=0:
                carry+=int(a[l1])
                l1-=1
            if l2>=0:
                carry+=int(b[l2])
                l2-=1
            res=str(carry%2)+res
            carry//=2
        if carry>0:
            res=str(1)+res
        return res
