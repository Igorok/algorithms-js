from typing import List
import json
from collections import deque, defaultdict
from functools import lru_cache
import heapq


class Solution_0:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        countByNum = {}
        unique = []
        for num in nums:
            cnt = countByNum.get(num, 0)
            if cnt == 0:
                unique.append(num)
            countByNum[num] = cnt + 1

        unique.sort()
        n = len(unique)
        prefixSum = [0]*n
        prefixSum[0]=countByNum[unique[0]]

        for i in range(1, n):
            prefixSum[i] = prefixSum[i-1] + countByNum[unique[i]]

        def getMinId(left, right, val):
            res = -1
            while left <= right:
                middle = (left+right) // 2
                if unique[middle] >= val:
                    res = middle
                    right = middle - 1
                else:
                    left = middle + 1

            return res

        def getMaxId(left, right, val):
            res = -1
            while left <= right:
                middle = (left + right) // 2
                if unique[middle] <= val:
                    res = middle
                    left = middle + 1
                else:
                    right = middle -1
            return res

        res = 0
        for i in range(n):
            num = unique[i]
            leftId = getMinId(0, i, num - k)
            rightId = getMaxId(i, n-1, num + k)

            leftCount = 0 if leftId == 0 else prefixSum[leftId-1]
            available = prefixSum[rightId] - leftCount - countByNum[num]
            real = min(available, numOperations)

            res = max(res, countByNum[num] + real)


        return res


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        n = len(nums)
        nums.sort()
        cntByNums = {}

        for i in range(n):
            num = nums[i]
            cntByNums[num] = cntByNums.get(num, 0) + 1

        def getMinId(val):
            left = 0
            right = n-1
            res = -1
            while left <= right:
                middle = (left+right) // 2
                if nums[middle] >= val:
                    res = middle
                    right = middle - 1
                else:
                    left = middle + 1

            return res

        def getMaxId(val):
            left = 0
            right = n-1
            res = -1
            while left <= right:
                middle = (left + right) // 2
                if nums[middle] <= val:
                    res = middle
                    left = middle + 1
                else:
                    right = middle -1
            return res

        res = 0
        for num in range(nums[0], nums[-1] + 1):
            cnt = cntByNums.get(num, 0)

            leftId = getMinId(num - k)
            rightId = getMaxId(num + k)

            if leftId == -1:
                continue

            available = rightId - leftId + 1
            real = min(available, numOperations + cnt)
            res = max(res, real)


        return res

'''


k=2, no=4
4 1 3 1 3 2
1 2 3 4 5 6



'''

def test():
    params = [
        {
            "input": [[88,53], 27, 2],
            "output": 2,
        },
        {
            "input": [[1,4,5], 1, 2],
            "output": 2,
        },
        {
            "input": [[5,11,20,20], 5, 1],
            "output": 2,
        },
    ]
    solution = Solution()

    for param in params:
        nums, k, numOperations = param["input"]
        result = solution.maxFrequency(nums, k, numOperations)
        correct = json.dumps(result) == json.dumps(param["output"])

        msg = "SUCCESS" if correct else "ERROR"
        msg += "\n"
        if not correct:
            msg += "input " + json.dumps(param["input"]) + "\n"
            msg += "output " + json.dumps(param["output"]) + "\n"
            msg += "result " + json.dumps(result) + "\n"

        print(msg)


if __name__ == "__main__":
    test()
