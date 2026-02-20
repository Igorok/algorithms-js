from typing import List
import json
from collections import deque, defaultdict
import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        N = len(matrix)
        merged = []

        for row in matrix:
            i = 0
            j = 0
            current = []
            while i < len(merged) and j < len(row):
                if merged[i] <= row[j]:
                    current.append(merged[i])
                    i += 1
                else:
                    current.append(row[j])
                    j += 1

            while i < len(merged):
                current.append(merged[i])
                i += 1

            while j < len(row):
                current.append(row[j])
                j += 1

            merged = current


        return merged[k-1]





def test ():
    params = [
        {
            'input': [[[1,5,9],[10,11,13],[12,13,15]], 8],
            'output': 13,
        },
        {
            'input': [[[-5]], 1],
            'output': -5,
        },
    ]
    solution = Solution()

    for param in params:
        matrix, k = param['input']
        result = solution.kthSmallest(matrix, k)
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
