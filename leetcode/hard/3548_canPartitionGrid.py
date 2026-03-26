from typing import List
from json import dumps
from collections import deque
import heapq

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        self.grid = grid
        N = len(grid)
        M = len(grid[0])

        cntTotal = {}
        sumOfGrid = []

        for row in range(N):
            sumOfGrid.append([])

            for col in range(M):
                val = grid[row][col]

                sumOfGrid[row].append(val)

                if row > 0:
                    sumOfGrid[row][col] += sumOfGrid[row-1][col]
                if col > 0:
                    sumOfGrid[row][col] += sumOfGrid[row][col-1]
                if row > 0 and col > 0:
                    sumOfGrid[row][col] -= sumOfGrid[row-1][col-1]

                cntTotal[val] = cntTotal.get(val, 0) + 1

        cntLocal = {}
        for row in range(N-1):
            for col in range(M):
                val = grid[row][col]
                cntLocal[val] = cntLocal.get(val, 0) + 1

                # last column, check sum
                if col != M-1:
                    continue

                top = sumOfGrid[row][-1]
                bottom = sumOfGrid[-1][-1] - top

                if top == bottom:
                    return True

                if top > bottom:
                    if row == 0:
                        if (top - grid[0][0] == bottom or top - grid[0][-1] == bottom):
                            return True
                        continue

                    diff = top - bottom
                    if diff in cntLocal:
                        if M == 1 and (grid[0][0] != diff and grid[row][col] != diff):
                                continue
                        return True

                if bottom > top:
                    if row == N-2:
                        if (bottom - grid[-1][0] == top or bottom - grid[-1][-1] == top):
                            return True
                        continue

                    diff = bottom - top
                    if diff in cntTotal and cntTotal[diff] > cntLocal.get(diff, 0):
                        if M == 1 and (grid[row+1][0] != 1 and grid[-1][0] != 1):
                                continue
                        return True

        cntLocal = {}
        for col in range(M-1):
            for row in range(N):
                val = grid[row][col]
                cntLocal[val] = cntLocal.get(val, 0) + 1

                if row != N-1:
                    continue

                left = sumOfGrid[row][col]
                right = sumOfGrid[-1][-1] - left

                if left == right:
                    return True


                if left > right:
                    if col == 0:
                        if left - grid[0][0] == right or left - grid[-1][0] == right:
                            return True
                        continue

                    diff = left - right
                    if diff in cntLocal:
                        if N == 1 and (grid[0][0] != diff and grid[0][col] != diff):
                                continue
                        return True

                if right > left:
                    if col == M-2:
                        if right - grid[0][-1] == left or right - grid[-1][-1] == left:
                            return True
                        continue

                    diff = right - left
                    if diff in cntTotal and cntTotal[diff] > cntLocal.get(diff, 0):
                        if N == 1 and (grid[0][col+1] != diff and grid[0][-1] != diff):
                                continue
                        return True

        cntLocal = None

        return False

'''
[[1,1,1],[1,2,4],[2,3,5],[1,1,1]]


[
[4,1,8],
[3,2,6]
]

I can calculate all sum for every square
1) I should know where is the difference in top or bottom?
2) I should know is it connected or not?

2) It is not connected if:
    it is 1*n I can remove only 2 cells left and right, I don't need to save locations for every number
    it is 1*1 and I can not remove this cell at all

1) I can calculate total count of every number.
I can calculate count of numbers for every row. But I have no value for every column?
I can make 3*n*m - for total, for row, for column, and I will have everything, but slow.



'''

def test ():
    params = [
        {
            'input': [[1,4],[2,3]],
            'output': True,
        },
        {
            'input': [[1,2],[3,4]],
            'output': True,
        },
        {
            'input': [
                [1,2,4],
                [2,3,5]],
            'output': False,
        },
        {
            'input': [[4,1,8],[3,2,6]],
            'output': False,
        },
        {
            'input': [[1,1,1],[1,2,4],[2,3,5],[1,1,1]],
            'output': True,
        },
        {
            'input': [[10,5,4,5]],
            'output': False,
        },
        {
            'input': [[10],[5],[4],[5]],
            'output': False,
        },
        {
            'input': [[25372],[100000],[100000]],
            'output': True,
        },
    ]
    solution = Solution()

    for param in params:
        grid = param['input']
        result = solution.canPartitionGrid(grid)

        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            # 'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
