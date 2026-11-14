import heapq
import json
from collections import defaultdict, deque
from functools import cache
from typing import List


'''
7:
    8, 4, 2, 1
    6, 3, 2, 1
5:
    6, 3, 2, 1
    4, 2, 1

'''

class Solution:
    def integerReplacement(self, n: int) -> int:

        queue = deque([(n, 0)])

        while queue:
            num, score = queue.popleft()

            if num == 1:
                return score

            if num % 2 == 0:
                queue.append((num // 2, score + 1))
            else:
                queue.append((num + 1, score + 1))
                queue.append((num - 1, score + 1))

        return 0

def test():
    params = [
        {
            "input": 8,
            "output": 3,
        },
        {
            "input": 7,
            "output": 4,
        },
        {
            "input": 4,
            "output": 2,
        },
    ]
    solution = Solution()

    for param in params:
        n = param["input"]
        result = solution.integerReplacement(n)
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
