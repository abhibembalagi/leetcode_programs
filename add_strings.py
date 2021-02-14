#worst case
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def to_int(string):
            n=0
            c=1
            for s in string[::-1]:
                n+=c*(ord(s)-ord("0"))
                c*=10
            return n
        return(str(to_int(num1)+to_int(num2)))
#best case
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        p1=len(num1)-1
        p2=len(num2)-1
        summ=0
        carry=0
        res=[]
        while p1>=0 or p2>=0:
            if p1>=0:
                x1=ord(num1[p1])-ord("0")
            else:
                x1=0
            if p2>=0:
                x2=ord(num2[p2])-ord("0")
            else:
                x2=0
            summ=(x1+x2+carry)%10
            carry=(x1+x2+carry)//10
            res.append(summ)
            p1-=1
            p2-=1
        if carry:
            res.append(carry)
        return "".join([str(x) for x in res[::-1]])
