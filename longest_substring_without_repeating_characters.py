class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        dic = {}
        dic[s[0]] = 1
        l = 0
        r = 1
        res = 0
        maxS = str(dic[s[0]])
        while r < len(s):
            if s[r] not in dic or dic[s[r]] == 0:
                dic[s[r]] = 1
                r += 1
                if r == len(s):
                    if len(maxS) < r - l: maxS = s[l:r]
            else:
                if len(maxS) < r - l: maxS = s[l:r]
                dic[s[r]] += 1
                while True:
                    dic[s[l]] -= 1
                    a = s[l]
                    l += 1
                    if s[r] == a:
                        r += 1
                        break
        return len(maxS)
        
        
    ========================
    class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = dict()
        result = 0
        
        for i in range(0, len(s)):
            if s[i] not in d:
                d[s[i]] = True
                result = max(result, len(d))
            
            else:
                result = max(result, len(d))
                di = d.copy()
                for key,value in di.items():
                    d.pop(key)
                    if key == s[i]:
                        d[s[i]] = True
                        break

        
        return result
