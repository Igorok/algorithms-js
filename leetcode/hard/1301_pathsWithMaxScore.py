import heapq
from collections import Counter, defaultdict
from functools import cache
from json import dumps
from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        N = len(board)
        M = len(board[0])
        MOD = 10**9 + 7
        shifts = ((1,0),(0,1),(1,1))

        @cache
        def dfs(row, col):
            nonlocal N, M, shifts
            
            if row == N-1 and col == M-1:
                return (0, 1)

            # if board[row][col] == 'X':
            #     return [float('-inf'), 0]

            val = 0 if (row == 0 and col == 0) else int(board[row][col])
            res = [float('-inf'), 0]
            
            for sR, sC in shifts:
                newR = sR + row
                newC = sC + col

                if newR == -1 or newR == N or newC == -1 or newC == M:
                    continue
                if board[newR][newC] == 'X':
                    continue
                
                r = dfs(newR, newC)
                
                if r[0]+val < res[0]:
                    continue
                elif r[0]+val > res[0]:
                    res = [r[0]+val, r[1]]
                else:
                    res[1] = (res[1] + r[1]) % MOD

            return res

        res = dfs(0,0)
        if res[0] == float('-inf'):
            return [0,0]
            
        return res


'''
"E11",
"XXX",
"11S"


'''
        
def test():
    params = [
        {
            "input": ["E23","2X2","12S"],
            "output": [7,1],
        },
        {
            "input": ["E12","1X1","21S"],
            "output": [4,2],
        },
        {
            "input": ["E11","XXX","11S"],
            "output": [0,0],
        },
    ]
    solution = Solution()

    for param in params:
        board = param["input"]
        result = solution.pathsWithMaxScore(board)
        print(
            "SUCCESS" if result == param["output"] else "ERROR",
            "input",
            param["input"],
            "output",
            param["output"],
            "result",
            result,
            "\n",
        )


if __name__ == "__main__":
    test()
