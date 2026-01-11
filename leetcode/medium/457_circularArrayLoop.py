from typing import List
import heapq
import math
from collections import defaultdict, deque

class Solution_0:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        N = len(nums)
        # parents = [-1] * N

        def dfs(id, parents, positive):
            nonlocal N

            nextId = (nums[id] + id + N) % N

            if nextId == id or bool(nums[id] > 0) != positive:
                return False

            if parents[nextId] != -1:
                return parents[nextId] == id

            parents[nextId] = id

            return dfs(nextId, parents, positive)

        for id in range(N):
            r = dfs(id, [-1]*N, nums[id] > 0)
            # r = dfs(id, parents)
            if r:
                return r

        return False

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        N = len(nums)
        memo = [[None, None] for i in range(N)]

        def dfs(id, parents, positive):
            nonlocal N

            p = 1 if positive else 0
            if memo[id][p] != None:
                return memo[id][p]

            nextId = (nums[id] + id + N) % N

            if nextId == id or bool(nums[id] > 0) != positive:
                memo[id][p] = False
                return memo[id][p]

            if parents[nextId] != -1:
                memo[id][p] = True
                return memo[id][p]

            parents[nextId] = id

            memo[id][p] = dfs(nextId, parents, positive)

            return memo[id][p]

        for id in range(N):
            r = dfs(id, [-1]*N, nums[id] > 0)
            # r = dfs(id, parents)
            if r:
                return r

        return False


def test ():
    params = [
        {
            'input': [2,-1,1,2,2],
            'output': True,
        },
        {
            'input': [-1,-2,-3,-4,-5,6],
            'output': False,
        },
        {
            'input': [1,-1,5,1,4],
            'output': True,
        },
        {
            'input': [-2,1,-1,-2,-2],
            'output': False,
        },
        {
            'input': [1,1,2],
            'output': True,
        },

    ]
    solution = Solution()

    for param in params:
        nums = param['input']
        result = solution.circularArrayLoop(nums)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
