import json
from collections import defaultdict, deque
from typing import List
# from functools import cache

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])

        res = 0

        for r in range(N-2):
            for c in range(M-2):
                nums = set()
                rowS = [0]*3
                colS = [0]*3
                for i in range(3):
                    for j in range(3):
                        num = grid[r+i][c+j]
                        if num > 9 or num < 1:
                            break

                        rowS[i] += num
                        colS[j] += num
                        nums.add(num)

                if len(nums) != 9:
                    continue

                if rowS[0] != rowS[1] or rowS[1] != rowS[2]:
                    continue

                if colS[0] != rowS[0] or colS[0] != colS[1] or colS[1] != colS[2]:
                    break

                d1 = grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2]
                if d1 != colS[0]:
                    continue
                d2 = grid[r+2][c] + grid[r+1][c+1] + grid[r][c+2]
                if d2 != d1:
                    continue

                res += 1


        return res


def test():
    params = [
        {
            "input": [[4,3,8,4],[9,5,1,9],[2,7,6,2]],
            "output": 1,
        },
        {
            "input": [[8]],
            "output": 0,
        },
        {
            "input": [[5,5,5],[5,5,5],[5,5,5]],
            "output": 0,
        },
    ]
    solution = Solution()

    for param in params:
        grid = param["input"]
        result = solution.numMagicSquaresInside(grid)
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
