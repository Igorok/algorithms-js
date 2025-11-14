from typing import List
import json
from collections import deque, defaultdict
import heapq
from functools import lru_cache


class Solution_0:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        def processAcc(acc, left, right):
            if left > right or left == n:
                return 0

            if left == right:
                return 1 if nums[left] > 0 else 0

            res = 0
            if acc:
                res += 1

            for i in acc:
                nums[i] = 0
                res += dfs(left, i)
                left = i + 1

            res += dfs(left, right)

            return res

        def dfs(left, right):
            if left > right or left == n:
                return 0

            if left == right:
                return 1 if nums[left] > 0 else 0

            res = 0
            acc = []
            l = left

            for i in range(left, right):
                if nums[i] == 0:
                    res += processAcc(acc, l, i)
                    acc = []
                    l = i + 1
                    continue

                if not acc or nums[i] == nums[acc[0]]:
                    acc.append(i)
                elif nums[i] < nums[acc[0]]:
                    acc = [i]

            res += processAcc(acc, l, right)


            return res



        return dfs(0, len(nums))


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        stack = []

        for num in nums:
            if num == 0:
                stack = []
                continue

            while stack and stack[-1] > num:
                stack.pop()

            if not stack or stack[-1] < num:
                res += 1
            stack.append(num)

        return res





'''
1,2,1,2,1,2
1 - 1 - 1

1 2 3 4 3 2 3 1 2

'''

def test ():
    params = [
        {
            'input': [0,2],
            'output': 1,
        },
        {
            'input': [3,1,2,1],
            'output': 3,
        },
        {
            'input': [1,2,1,2,1,2],
            'output': 4,
        },
    ]
    solution = Solution()

    # params.append({
    #     'input': [i for i in range(1, 10**5)],
    #     'output': 50001,
    # })

    for param in params:
        nums = param['input']
        result = solution.minOperations(nums)
        correct = json.dumps(result) == json.dumps(param['output'])

        msg = 'SUCCESS' if correct else 'ERROR'
        msg += '\n'
        if not correct:
            # msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()
