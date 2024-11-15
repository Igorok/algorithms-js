from typing import List
from json import dumps
import heapq

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        used = [-1]*10
        res = []

        def rec(arr, s):
            nonlocal res

            if len(arr) == k:
                if s == n:
                    res.append(arr)
                return
            if s >= n:
                return

            for i in range(arr[-1] + 1, 10):
                rec(arr + [i], s + i)


        for i in range(1, 10):
            rec([i], i)

        return res

def test ():
    params = [
        {
            'input': [3, 7],
            'output': [[1,2,4]],
        },
        {
            'input': [3, 9],
            'output': [[1,2,6],[1,3,5],[2,3,4]],
        },
        {
            'input': [4, 1],
            'output': [],
        },
    ]
    solution = Solution()

    for param in params:
        k, n = param['input']
        result = solution.combinationSum3(k, n)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
