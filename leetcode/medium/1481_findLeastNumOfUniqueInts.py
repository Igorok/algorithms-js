from typing import List
import heapq
import math
from collections import defaultdict, deque

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cntByNums = {}
        for num in arr:
            cntByNums[num] = cntByNums.get(num, 0) + 1

        sorted_by_key = sorted(cntByNums.items(), key=lambda x: x[1])

        N = len(sorted_by_key)
        for i in range(N):
            cnt = sorted_by_key[i][1]
            if cnt > k:
                return N - i
            k -= cnt


        return 0

def test ():
    params = [
        {
            'input': [[5,5,4], 1],
            'output': 1,
        },
        {
            'input': [[4,3,1,1,3,3,2], 3],
            'output': 2,
        },
    ]
    solution = Solution()

    for param in params:
        arr, k = param['input']
        result = solution.findLeastNumOfUniqueInts(arr, k)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
