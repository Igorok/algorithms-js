from typing import List
import json
import heapq


class Solution_0:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        N = len(nums)

        minWidth = k-1
        largest = []

        def getRemovedSum(left):
            nonlocal N, largest

            right = min(N, left + dist +1)
            width = right - left
            diff = width - (k-1)

            if diff == 0:
                return 0

            removed = []
            removedSum = 0
            while largest and len(removed) < diff:
                v, id = heapq.heappop(largest)
                if id < left:
                    continue
                if id == left:
                    removed.append((v, id))
                    continue
                removedSum += -v
                removed.append((v, id))

            for i in range(len(removed)):
                heapq.heappush(largest, removed[i])

            return removedSum

        tmp = 0
        for i in range(1, 1+dist+1):
            tmp += nums[i]
            largest.append((-nums[i], i))

        heapq.heapify(largest)

        removedSum = getRemovedSum(1)
        res = nums[0] + tmp - removedSum

        for left in range(2, N-minWidth+1):
            tmp -= nums[left-1]
            if left+dist < N:
                tmp += nums[left+dist]
                heapq.heappush(largest, (-nums[left+dist], left+dist))

            removedSum = getRemovedSum(left)
            res = min(res, nums[0] + tmp - removedSum)

        return res


class Solution_1:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        N = len(nums)
        minWidth = k-1
        heapSmall = []
        heapBig = []
        minCosts = set()
        minSum = 0

        for right in range(1, min(1 + dist + 1, N)):
            heapBig.append((nums[right], right))

        heapq.heapify(heapBig)

        def getMinSum(left):
            nonlocal minSum, minCosts, heapSmall, heapBig, k, N, dist

            if left in minCosts:
                minCosts.remove(left)
                minSum -= nums[left]

            while (heapBig and len(minCosts) < k - 2) or (heapBig and heapSmall and -heapSmall[0][0] > heapBig[0][0]):
                while heapSmall and heapSmall[0][1] <= left:
                    v, id = heapq.heappop(heapSmall)
                    if id in minCosts:
                        minCosts.remove(id)
                        minSum -= -v

                while heapBig and heapBig[0][1] <= left:
                    heapq.heappop(heapBig)

                if heapSmall and heapBig and -heapSmall[0][0] > heapBig[0][0]:
                    small = heapq.heappop(heapSmall)
                    big = heapq.heappop(heapBig)

                    minSum -= -small[0]
                    minCosts.remove(small[1])

                    minSum += big[1]
                    minCosts.add(big[1])

                    heapq.heappush(heapSmall, (-big[0], big[1]))
                    heapq.heappush(heapBig, (-small[0], small[1]))
                    continue

                if heapBig:
                    v, id = heapq.heappop(heapBig)
                    heapq.heappush(heapSmall, (-v, id))
                    minSum += nums[id]
                    minCosts.add(id)

            return minSum + nums[left]

        res = getMinSum(1)

        for left in range(2, N-minWidth+1):
            right = left + dist

            if left-1 in minCosts:
                minCosts.remove(left-1)
                minSum -= nums[left-1]

            if right < N:
                heapq.heappush(heapBig, (nums[right], right))

            r = getMinSum(left)
            res = min(res, r)


        return res + nums[0]


class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        N = len(nums)
        minWidth = k-1
        heapSmall = []
        heapBig = []
        minCosts = set()
        minSum = 0

        for right in range(1, min(1 + dist + 1, N)):
            heapBig.append((nums[right], right))

        heapq.heapify(heapBig)

        def getMinSum(left):
            nonlocal minSum, minCosts, heapSmall, heapBig, k, N, dist

            if left-1 in minCosts:
                minCosts.remove(left-1)
                minSum -= nums[left-1]

            while heapSmall and heapSmall[0][1] < left:
                heapq.heappop(heapSmall)
            while heapBig and heapBig[0][1] < left:
                heapq.heappop(heapBig)

            while (heapBig and len(minCosts) < k - 1) or (heapBig and heapSmall and -heapSmall[0][0] > heapBig[0][0]):
                while heapSmall and heapSmall[0][1] < left:
                    heapq.heappop(heapSmall)
                while heapBig and heapBig[0][1] < left:
                    heapq.heappop(heapBig)

                if heapSmall and heapBig and -heapSmall[0][0] > heapBig[0][0]:
                    small = heapq.heappop(heapSmall)
                    big = heapq.heappop(heapBig)

                    minSum -= -small[0]
                    minCosts.remove(small[1])

                    minSum += big[0]
                    minCosts.add(big[1])

                    heapq.heappush(heapSmall, (-big[0], big[1]))
                    heapq.heappush(heapBig, (-small[0], small[1]))
                    continue

                if heapBig:
                    v, id = heapq.heappop(heapBig)
                    heapq.heappush(heapSmall, (-v, id))
                    minSum += v
                    minCosts.add(id)

            if left not in minCosts:
                v, id = heapq.heappop(heapSmall)
                minCosts.remove(id)
                minSum -= -v

                minCosts.add(left)
                minSum += nums[left]

                heapq.heappush(heapSmall, (-nums[left], left))
                heapq.heappush(heapBig, (-v, id))

            return minSum

        res = getMinSum(1)

        for left in range(2, N-minWidth+1):
            right = left + dist

            if right < N:
                heapq.heappush(heapBig, (nums[right], right))

            r = getMinSum(left)
            res = min(res, r)


        return res + nums[0]


'''
[10,1,2,2,2,1], k = 4, dist = 3
0  1 2 3 4 5
10,1,2,2,2,1
10,
1,2,2,
2,
1


5 1 3 8 2 2 2



'''



def test ():
    params = [
        {
            'input': [[1,3,2,6,4,2], 3, 3],
            'output': 5,
        },
        {
            'input': [[10,1,2,2,2,1], 4, 3],
            'output': 15,
        },
        {
            'input': [[10,8,18,9], 3, 1],
            'output': 36,
        },
        {
            'input': [[5, 1, 3, 8, 2, 2, 2], 4, 2],
            'output': 11,
        },
        {
            'input': [[1,6,3,5], 3, 2],
            'output': 9,
        },
    ]
    solution = Solution()

    for param in params:
        nums, k, dist = param['input']
        result = solution.minimumCost(nums, k, dist)
        print(
            'SUCCESS' if json.dumps(result) == json.dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
