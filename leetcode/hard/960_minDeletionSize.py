import json
from collections import defaultdict, deque
from typing import List
import heapq

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        strLen = len(strs[0])
        maxLengthForId = [1] * strLen
        res = 1

        for i in range(1, strLen):
            for j in range(i):
                isValid = True
                for row in strs:
                    if row[j] > row[i]:
                        isValid = False
                        break
                if isValid:
                    maxLengthForId[i] = max(maxLengthForId[i], maxLengthForId[j] + 1)
                    res = max(res, maxLengthForId[i])

        return strLen - res


'''

cdfabcd

'''


def test():
    params = [
        {
            "input": ["babca","bbazb"],
            "output": 3,
        },
        {
            "input": ["edcba"],
            "output": 4,
        },
        {
            "input": ["ghi","def","abc"],
            "output": 0,
        },
    ]
    solution = Solution()

    for param in params:
        strs = param["input"]
        result = solution.minDeletionSize(strs)
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
