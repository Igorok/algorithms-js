from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        res = 0

        empty = 0
        while numBottles > 0 or empty > numExchange:
            empty += numBottles
            res += numBottles
            numBottles = 0

            if empty >= numExchange:
                numBottles += 1
                empty -= numExchange
                numExchange += 1

        return res

'''

3 1

f:0, e:3, ex:1, r:3
f:1, e:2, ex:2, r:3
f:2, e:0, ex:3, r:3
f:0, e:0, ex:3, r:5

---

numBottles = 10, numExchange = 3
f: 10, e: 0, ex: 3, r: 0
f: 0, e: 10, ex: 3, r: 10
f: 1, e: 7, ex: 4, r: 10
f: 0, e: 8, ex: 4, r: 11
f: 1, e: 4, ex: 5, r: 11
f: 0, e: 5, ex: 5, r: 12
f: 1, e: 0, ex: 6, r: 12
f: 0, e: 0, ex: 6, r: 13


'''

def test():
    params = [
        {
            "input": [13, 6],
            "output": 15,
        },
        {
            "input": [10, 3],
            "output": 13,
        },
    ]
    solution = Solution()

    for param in params:
        numBottles, numExchange = param["input"]
        result = solution.maxBottlesDrunk(numBottles, numExchange)
        correct = json.dumps(result) == json.dumps(param["output"])

        msg = "SUCCESS" if correct else "ERROR"
        msg += "\n"
        if not correct:
            # msg += "input " + json.dumps(param["input"]) + "\n"
            msg += "output " + json.dumps(param["output"]) + "\n"
            msg += "result " + json.dumps(result) + "\n"

        print(msg)


if __name__ == "__main__":
    test()
