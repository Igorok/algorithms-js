from typing import List
import json
from collections import deque, defaultdict
from functools import lru_cache


class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)

        def getCode(char):
            return ord(char) - ord('a')

        def getUniqCount(acc):
            res = 0
            while acc > 0:
                res += acc & 1
                acc = acc >> 1
            return res

        def setUniq(acc, code):
            acc = acc | (1 << code)
            return acc

        @lru_cache(None)
        def getMaxCount(id, changed, unique):
            if id == n:
                return 0 if unique == 0 else 1

            code = getCode(s[id])
            updatedUniq = setUniq(unique, code)
            bits = getUniqCount(updatedUniq)
            if bits > k:
                return 1 + getMaxCount(id, changed, 0)

            res = getMaxCount(id+1, changed, updatedUniq)

            if not changed:
                curr = ord(s[id])
                start = ord('a')
                end = ord('z') + 1

                for i in range(start, end):
                    if i == curr:
                        continue

                    char = chr(i)

                    code = getCode(char)
                    updatedUniq = setUniq(unique, code)
                    bits = getUniqCount(updatedUniq)

                    r = 0
                    if bits > k:
                        # acc = ???
                        r = 1 + getMaxCount(id+1, True, setUniq(0, code))
                    else:
                        r = getMaxCount(id+1, True, updatedUniq)

                    res = max(res, r)

            return res

        return getMaxCount(0, False, 0)

'''
["ba", 1]

b
-ba;1+dfs(a);
--a;dfs(a-);1
1+1

c;
ca;



'''



def test():
    params = [

        {
            "input": ["ba", 1],
            "output": 2,
        },
        {
            "input": ["baca", 2],
            "output": 2,
        },
        {
            "input": ["accca", 2],
            "output": 3,
        },
        {
            "input": ["aabaab", 3],
            "output": 1,
        },
        {
            "input": ["xxyz", 1],
            "output": 4,
        },
    ]
    solution = Solution()

    for param in params:
        s, k = param["input"]
        result = solution.maxPartitionsAfterOperations(s, k)
        correct = json.dumps(result) == json.dumps(param["output"])

        msg = "SUCCESS" if correct else "ERROR"
        msg += "\n"
        if not correct:
            msg += "input " + json.dumps(param["input"]) + "\n"
            msg += "output " + json.dumps(param["output"]) + "\n"
            msg += "result " + json.dumps(result) + "\n"

        print(msg)


if __name__ == "__main__":
    test()
