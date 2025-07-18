from typing import List
from json import dumps
import heapq
from collections import deque

class Solution_0:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        part = n // 3
        res = float('inf')

        for i in range(part, n-part+1):
            left = sorted(nums[:i])[:part]
            right = sorted(nums[i:], reverse=True)[:part]
            r = sum(left) - sum(right)
            res = min(res, r)

        return res

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        part = n // 3
        res = float('inf')

        leftMemo = [float('inf')]*n
        leftSum = 0
        leftHeap = []
        for i in range(part):
            leftSum += nums[i]
            heapq.heappush(leftHeap, -nums[i])

        leftMemo[part-1] = leftSum

        for i in range(part, n-part+1):
            if -leftHeap[0] > nums[i]:
                leftSum += leftHeap[0] # leftSum - (-leftHeap[0])
                leftSum += nums[i]
                heapq.heappop(leftHeap)
                heapq.heappush(leftHeap, -nums[i])

            leftMemo[i] = leftSum


        rightMemo = [float('-inf')]*n
        rightSum = 0
        rightHeap = []
        for i in range(part):
            id = n - 1 - i
            rightSum += nums[id]
            heapq.heappush(rightHeap, nums[id])

        rightMemo[n - part] = rightSum

        for i in range(n-part-1, max(part-2, -1), -1):
            r = leftMemo[i] - rightSum
            res = min(res, r)

            if nums[i] > rightHeap[0]:
                rightSum -= rightHeap[0]
                rightSum += nums[i]
                heapq.heappop(rightHeap)
                heapq.heappush(rightHeap, nums[i])


        return res


def test ():
    params = [
        {
            'input': [34,30,13],
            'output': 4,
        },
        {
            'input': [16,46,43,41,42,14,36,49,50,28,38,25,17,5,18,11,14,21,23,39,23],
            'output': -14,
        },
        {
            'input': [3,1,2],
            'output': -1,
        },
        {
            'input': [7,9,5,8,1,3],
            'output': 1,
        },
        {
            'input': [1,2,6,3,5,7,8,4,9],
            'output': -18,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.minimumDifference(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

if __name__ == '__main__':
    test()
