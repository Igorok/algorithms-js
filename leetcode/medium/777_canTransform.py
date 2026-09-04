import json
from collections import Counter
from functools import cache
from typing import List

"""

"RXXLRXRXL",
"XRLXXRRLX"

---

Do you understand why answer is false?
```
Input
start =
"LXXLXRLXXL"
result =
"XLLXRXLXLX"

Output
true
Expected
false
```
"LXXLXRLXXL", - > llxxxrllxx
"XLLXRXLXLX" -> llxxxrllxx

"""


class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        # check chars and order of L and R
        if start.replace("X", "") != result.replace("X", ""):
            return False

        N = len(start)
        # Get ids of L and R
        startL = [i for i in range(N) if start[i] == "L"]
        resL = [i for i in range(N) if result[i] == "L"]

        startR = [i for i in range(N) if start[i] == "R"]
        resR = [i for i in range(N) if result[i] == "R"]

        # We already know, the order is okay
        # We can move L to the left.
        # If the L in the start already left of the L from the result we can not improve the string
        for i in range(len(startL)):
            if startL[i] < resL[i]:
                return False

        # We can move R to the right. If the R in the start already right of the R from the result we can not improve the string
        for i in range(len(startR)):
            if startR[i] > resR[i]:
                return False

        return True


def test():
    params = [
        {
            "input": ["RXXLRXRXL", "XRLXXRRLX"],
            "output": True,
        },
        {
            "input": ["X", "L"],
            "output": False,
        },
        {
            "input": ["LXXLXRLXXL", "XLLXRXLXLX"],
            "output": False,
        },
    ]
    solution = Solution()

    for param in params:
        start, result = param["input"]
        result = solution.canTransform(start, result)
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
