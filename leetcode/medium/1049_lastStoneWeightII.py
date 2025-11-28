from typing import List
import json
from collections import deque
import heapq
import math

class Solution_0:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stones.sort()
        cache = {}


        def dfs(arr):
            if not arr:
                return 0
            if len(arr) == 1:
                return arr[0]

            key = '_'.join([str(n) for n in arr])
            if key in cache:
                return cache[key]

            res = float('inf')

            for i in range(len(arr)-1):
                _arr = arr.copy()
                stone1 = _arr[i]
                del _arr[i]

                for j in range(i, len(_arr)):
                    __arr = _arr.copy()
                    stone2 = __arr[j]
                    del __arr[j]

                    if stone1 != stone2:
                        __arr.append(abs(stone1- stone2))
                        __arr.sort()

                    r = dfs(__arr)
                    res = min(r, res)

            cache[key] = res

            return res



        return dfs(stones)


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stones.sort()
        N = len(stones)
        total = sum(stones)
        left = math.ceil(total / 2)
        right = total - left

        print(
            'left', left,
            'right', right,
            'total', total,
        )


        real = 0
        memo = [[float('inf')] * N for i in range(left+1)]
        for size in range(stones[0], left + 1):
            for i in range(N):
                stone = stones[i]
                if i > 0:
                    memo[size][i] = memo[size][i-1]

                if stone > size:
                    continue

                if stone == size:
                    memo[size][i] = 1
                    real = size
                    continue

                diff = size - stone
                cnt = float('inf') if i == 0 else memo[diff][i-1]

                memo[size][i] = min(cnt + 1, memo[size][i])

                if memo[size][i] != float('inf'):
                    real = size


        # print(
        #     'memo', memo,
        # )
        remainder = total-real
        print(
            'total', total,
            'real', real,
            'remainder', remainder,
            'diff', abs(remainder - total)
        )


        return abs(total - real - real)


'''

2**30 = 1_073_741_824

'''

def test ():
    params = [
        {
            'input': [53,54,3,61,67],
            'output': 2,
        },
        {
            'input': [1,2],
            'output': 1,
        },
        {
            'input': [2,7,4,1,8,1],
            'output': 1,
        },
        {
            'input': [31,26,33,21,40],
            'output': 5,
        },
        # {
        #     'input': [1,1,2,3,5,8,13,21,34,55,89,14,23,37,61,98],
        #     'output': 1,
        # },
    ]
    solution = Solution()

    for param in params:
        stones = param['input']
        result = solution.lastStoneWeightII(stones)
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
