'''The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        str_len=len(s)
        if numRows==1:
            return s
        else:
            arr=[""]*numRows
            row=0
            result=""
            for i in range(str_len):
                arr[row]+=s[i]
                if row == numRows-1:
                    down=False
                elif row==0:
                    down=True
                if down:
                    row+=1
                else:
                    row-=1
            for i in arr:
                result+=i
            return(result)
