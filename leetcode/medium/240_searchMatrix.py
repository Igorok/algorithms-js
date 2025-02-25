from typing import List
import json
from collections import deque, defaultdict
import heapq

class Solution:
    def searchMatrix_0(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == target:
                    return True

        return False

    def searchMatrix_1(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        def findInRow(y):
            start = 0
            end = m-1

            while start <= end:
                middle = (start + end) // 2
                if matrix[y][middle] == target:
                    return True
                elif matrix[y][middle] < target:
                    start = middle + 1
                else:
                    end = middle - 1
            return False

        def findFirstY():
            i = 0
            while matrix[m-1][0] < target and i < n:
                i += 1
            return i

        def findLastY():
            i = n-1
            while matrix[i][0] > target and i > -1:
                i -= 1
            return i

        y1 = findFirstY()
        y2 = findLastY()

        if y1 > y2:
            return False

        for i in range(y1, y2+1):
            if findInRow(i):
                return True

        return False


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        def findInRow(y):
            start = 0
            end = m-1

            while start <= end:
                middle = (start + end) // 2
                if matrix[y][middle] == target:
                    return True
                elif matrix[y][middle] < target:
                    start = middle + 1
                else:
                    end = middle - 1
            return False

        def findFirstY():
            start = 0
            end = n-1
            y = 0

            while start <= end:
                middle = (start + end) // 2

                if matrix[middle][m-1] == target:
                    return middle
                elif matrix[middle][m-1] < target:
                    y = middle
                    start = middle + 1
                else:
                    end = middle - 1
            return y

        def findLastY():
            start = 0
            end = n-1
            y = n-1

            while start <= end:
                middle = (start + end) // 2

                if matrix[middle][0] == target:
                    return middle
                elif matrix[middle][0] > target:
                    y = middle
                    end = middle - 1
                else:
                    start += 1

            return y

        y1 = findFirstY()
        y2 = findLastY()

        if y1 > y2:
            return False

        for i in range(y1, y2+1):
            if findInRow(i):
                return True

        return False


def test ():
    params = [
        {
            'input': [[[1,4],[2,5]], 5],
            'output': True,
        },
        {
            'input': [
                [
                    [1,4,7,11,15],
                    [2,5,8,12,19],
                    [3,6,9,16,22],
                    [10,13,14,17,24],
                    [18,21,23,26,30]
                ],
                5
            ],
            'output': True,
        },
        {
            'input': [[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20],
            'output': False,
        },
    ]
    solution = Solution()

    for param in params:
        matrix, target = param['input']
        result = solution.searchMatrix(matrix, target)
        correct = json.dumps(result) == json.dumps(param['output'])

        msg = 'SUCCESS' if correct else 'ERROR'
        msg += '\n'
        if not correct:
            msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()
