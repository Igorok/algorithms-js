from typing import List
import heapq

class Solution:
    def totalCost_1(self, costs: List[int], k: int, candidates: int) -> int:
        candQueue = []
        start = 0
        end = len(costs) - 1

        for i in range(candidates):
            if start < end:
                heapq.heappush(candQueue, (costs[start], True))
                heapq.heappush(candQueue, (costs[end], False))
                start += 1
                end -= 1
            if start == end:
                heapq.heappush(candQueue, (costs[start], True))
                start += 1

        res = 0
        for i in range(k):
            cost, isStart = heapq.heappop(candQueue)
            res += cost
            if start <= end:
                if isStart:
                    heapq.heappush(candQueue, (costs[start], True))
                    start +=1
                else:
                    heapq.heappush(candQueue, (costs[end], False))
                    end -=1
        return res



    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        leftQ = []
        rightQ = []
        start = 0
        end = len(costs) - 1

        for i in range(candidates):
            if start == end:
                heapq.heappush(leftQ, costs[start])
                start += 1
            if start < end:
                heapq.heappush(leftQ, costs[start])
                heapq.heappush(rightQ, costs[end])
                start += 1
                end -= 1

        res = 0
        def getLeft():
            nonlocal res, start

            res += leftQ[0]
            heapq.heappop(leftQ)
            if start <= end:
                heapq.heappush(leftQ, costs[start])
                start += 1

        def getRight():
            nonlocal res, end

            res += rightQ[0]
            heapq.heappop(rightQ)
            if start <= end:
                heapq.heappush(rightQ, costs[end])
                end -= 1


        for i in range(k):
            if len(leftQ) == 0:
                getRight()
                continue
            if len(rightQ) == 0:
                getLeft()
                continue

            lv = leftQ[0]
            rv = rightQ[0]

            if lv <= rv:
                getLeft()
            elif rv < lv:
                getRight()
            else:
                if start <= end:
                    if costs[start] < costs[end]:
                        getLeft()
                    else:
                        getRight()
                else:
                    getLeft()
        return res



def test ():
    params = [
        {
            'input': [
                [17,12,10,2,7,2,11,20,8], 3, 4
            ],
            'output': 11,
        },
        {
            'input': [
                [1,2,4,1], 3, 3
            ],
            'output': 4,
        },
        {
            'input': [
                [31,25,72,79,74,65,84,91,18,59,27,9,81,33,17,58],
                11, 2
            ],
            'output': 423,
        },
        {
            'input': [
                [10,1,11,10], 2, 1,
            ],
            'output': 11,
        },
        {
            'input': [
                [10,10,1,10,10,10], 3, 1,
            ],
            'output': 21,
        },
        {
            'input': [
                [10,10,1,9,9,9], 3, 1,
            ],
            'output': 21,
        },
        {
            'input': [
                [57,33,26,76,14,67,24,90,72,37,30], 11, 2
            ],
            'output': 526,
        },
        {
            'input': [
                [2,1,2], 1, 1
            ],
            'output': 2,
        },
    ]
    solution = Solution()

    for param in params:
        costs, k, candidates = param['input']
        result = solution.totalCost(costs, k, candidates)

        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
