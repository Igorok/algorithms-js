import json
from collections import defaultdict, deque
from typing import List
# from functools import cache

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        memo = []

        for row in range(102):
            memo.append([0] * row)

            if row == 1:
                memo[row][0] = poured
                continue

            for col in range(row):
                leftVal = memo[row-1][col-1] if col > 0 else 0
                rightVal = memo[row-1][col] if col < row-1 else 0

                l = 0 if leftVal <= 1 else (leftVal-1) / 2
                r = 0 if rightVal <= 1 else (rightVal-1) / 2

                memo[row][col] += l + r

                if row == query_row+1 and col == query_glass:
                    return min(memo[query_row+1][query_glass], 1)

        # print('memo', memo)

        return min(memo[query_row+1][query_glass], 1)


def test():
    params = [
        {
            "input": [1, 1, 1],
            "output": 0,
        },
        {
            "input": [2, 1, 1],
            "output": 0.50000,
        },
        {
            "input": [100000009, 33, 17],
            "output": 1.00000,
        },
    ]
    solution = Solution()

    for param in params:
        poured, query_row, query_glass = param["input"]
        result = solution.champagneTower(poured, query_row, query_glass)
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
