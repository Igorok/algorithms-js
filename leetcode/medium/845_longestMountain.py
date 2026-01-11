from typing import List
import heapq
import math
from collections import defaultdict


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        N = len(arr)
        status = 0
        left = 0
        res = 0

        for right in range(1, N):
            if status == 0:
                if arr[right-1] < arr[right]:
                    continue
                if arr[right-1] == arr[right]:
                    left = right
                else:
                    if right-1 > left:
                        status = 1
                    else:
                        left = right
            else:
                if arr[right-1] == arr[right]:
                    res = max(res, right - left)
                    left = right
                    status = 0
                if arr[right-1] < arr[right]:
                    res = max(res, right - left)
                    left = right-1
                    status = 0
                else:
                    continue

        if status == 1:
            res = max(res, N - left)

        return 0 if res < 3 else res


def test ():
    params = [
        {
            'input': [2,1,4,7,3,2,5],
            'output': 5,
        },
        {
            'input': [2,2,2],
            'output': 0,
        },
        {
            'input': [2,1,4,7,3,2,5,6,7,8,9,10,11,12,13,14,1],
            'output': 12,
        },
        {
            'input': [0,1,0,0,1,0,0,1,1,0,0,0,1,1,0,1,0,1,0,1,0,0,0,1,0,0,1,1,0,1,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0,1,1,1,1,0,0,0,1,0,0,1,1,0,0,0,1,0,0,1,1,0,0,0,0,1,0,0,1,1,1,1,1,1,1,0,1,1,0,1,1,1,0,0,0,1,0,1,1],
            'output': 3,
        },
    ]
    solution = Solution()

    for param in params:
        arr = param['input']
        result = solution.longestMountain(arr)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
