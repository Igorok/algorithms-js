from typing import List
import json
from collections import deque, defaultdict
import heapq



class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        N = len(nums)
        res = []
        even = (k % 2) == 0
        length = k // 2
        if not even:
            length += 1
        valuesMap = {}
        minHeap = []
        bigHeap = [(nums[i], i) for i in range(k)]

        heapq.heapify(bigHeap)

        while len(minHeap) < length:
            val, id = heapq.heappop(bigHeap)
            heapq.heappush(minHeap,(-val, id))
            valuesMap[id] = val

        v = (-minHeap[0][0] + bigHeap[0][0]) / 2 if even else float(-minHeap[0][0])
        res.append(v)

        for i in range(1, N-k+1):
            if (i-1) in valuesMap:
                del valuesMap[i-1]

            heapq.heappush(bigHeap, (nums[i+k-1], i+k-1))

            while minHeap and minHeap[0][1] < i:
                heapq.heappop(minHeap)

            while bigHeap and bigHeap[0][1] < i:
                heapq.heappop(bigHeap)

            while bigHeap and minHeap and bigHeap[0][0] < (-minHeap[0][0]):
                if minHeap and minHeap[0][1] < i:
                    heapq.heappop(minHeap)
                    continue

                if bigHeap and bigHeap[0][1] < i:
                    heapq.heappop(bigHeap)
                    continue

                bigVal, bigId = heapq.heappop(bigHeap)
                minVal, minId = heapq.heappop(minHeap)

                del valuesMap[minId]
                valuesMap[bigId] = bigVal

                heapq.heappush(bigHeap, (-minVal, minId))
                heapq.heappush(minHeap, (-bigVal, bigId))


            while len(valuesMap) < length:
                bigVal, bigId = heapq.heappop(bigHeap)
                if bigId < i:
                    continue
                valuesMap[bigId] = bigVal
                heapq.heappush(minHeap, (-bigVal, bigId))

            while minHeap and minHeap[0][1] < i:
                heapq.heappop(minHeap)

            while bigHeap and bigHeap[0][1] < i:
                heapq.heappop(bigHeap)

            v = (-minHeap[0][0] + bigHeap[0][0]) / 2 if even else float(-minHeap[0][0])
            res.append(v)



        return res

'''
[1,3,-1,-3,5,3,6,7]
0 1  2  3 4 5 6 7
1,3,-1,-3,5,3,6,7
1 3, -1


'''


def test ():
    params = [
        {
            'input': [[1,3,-1,-3,5,3,6,7], 3],
            'output': [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000],
        },
        {
            'input': [[1,2,3,4,2,3,1,4,2], 3],
            'output': [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000],
        },
        {
            'input': [[1,1,3,2,0,0], 3],
            'output': [1.00000,2.00000,2.00000,0.00000],
        },
        {
            'input': [[9,7,0,3,9,8,6,5,7,6], 2],
            'output': [8.00000,3.50000,1.50000,6.00000,8.50000,7.00000,5.50000,6.00000,6.50000],
        },
    ]
    solution = Solution()

    for param in params:
        nums, k = param['input']
        result = solution.medianSlidingWindow(nums, k)
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
