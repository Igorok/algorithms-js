from typing import List
from json import dumps
import heapq


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        acc = []
        gLength = len(nums)
        start = end = nums[0][0]

        for i in range(gLength):
            num = nums[i][0]
            start = min(start, num)
            end = max(end, num)
            heapq.heappush(acc, (num, i, 0))

        res = [start, end]

        while True:
            num, grId, id = heapq.heappop(acc)
            nId = id + 1
            if nId == len(nums[grId]):
                return res

            newNum = nums[grId][nId]

            start = min(newNum, acc[0][0])
            end = max(end, newNum)

            if res[1] - res[0] > end - start:
                res = [start, end]

            heapq.heappush(acc, (newNum, grId, nId))


        return res

'''

[8,10,12,15],
[2,4,6,10,13,14],
[9,10,15,17,19]



[8,10,12,15],[2,4,6,10,13,14],[9,10,15,17,19]

'''


def test ():
    params = [
        {
            'input': [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]],
            'output': [20,24],
        },
        {
            'input': [[1,2,3],[1,2,3],[1,2,3]],
            'output': [1,1],
        },
        {
            'input': [[8,10,12,15], [2,4,6,10,13,14], [9,10,15,17,19]],
            'output': [10,10],
        },
    ]

    solution = Solution()
    for param in params:
        result = solution.smallestRange(param['input'])
        print(
            'SUCCESS' if dumps(result) == dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
