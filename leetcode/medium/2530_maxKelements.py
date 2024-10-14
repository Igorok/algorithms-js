from typing import List
import heapq
from math import ceil

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        def heapify(arr):
            arr = [-v for v in arr]
            heapq.heapify(arr)
            return arr

        def pop(arr):
            v = heapq.heappop(arr)
            return -v

        def push(arr, val):
            heapq.heappush(arr, -val)

        maxValues = heapify(nums)

        maxK = 0
        for i in range(k):
            val = pop(maxValues)
            maxK += val
            push(maxValues, ceil(val / 3))

        return maxK


def test ():
    params = [
        {
            'input': [[10,10,10,10,10], 5],
            'output': 50,
        },
        {
            'input': [[1,10,3,3,3], 3],
            'output': 17,
        },
    ]
    solution = Solution()

    for param in params:
        nums, k = param['input']

        result = solution.maxKelements(nums, k)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

if __name__ == '__main__':
    test()
