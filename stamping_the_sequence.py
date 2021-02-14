class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        def check(stamp, target, i, res):
            change = True
            for j in range(len(stamp)):
                if stamp[j] != target[i + j] and target[i + j] != '?':
                    change = False
                    break
            if change:
                res.append(i)
                for j in range(len(stamp)):
                    target[i + j] = '?'
        ls = list(stamp)
        lt = list(target)
        m = len(stamp)
        n = len(target)
        res = []
        for i in range(n - m + 1):
            check(ls, lt, i, res)
        for i in range(n - m, -1, -1):
            check(ls, lt, i, res)
        return res[::-1] if "".join(lt) == "?" * n else []
