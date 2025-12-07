from typing import List
from collections import deque
from functools import cache


class Solution_0:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 7 + 10**9
        N = len(nums)

        @cache
        def dfs(id, minVal, maxVal):
            nonlocal N, MOD

            if id == N:
                return 1

            res = 0

            # continue
            minVal = min(minVal, nums[id])
            maxVal = max(maxVal, nums[id])
            if maxVal - minVal <= k:
                res = (res + dfs(id+1, minVal, maxVal)) % MOD

            # start new
            res = (res + dfs(id+1, nums[id], nums[id])) % MOD

            return res

        return dfs(0, -k, k)

class Solution_1:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 7 + 10**9
        N = len(nums)

        combinations = [0] * N

        for right in range(N):
            minVal = nums[right]
            maxVal = nums[right]

            for left in range(right, -1, -1):
                minVal = min(minVal, nums[left])
                maxVal = max(maxVal, nums[left])
                if maxVal - minVal > k:
                    break

                prev = 1 if left == 0 else combinations[left-1]
                combinations[right] = (combinations[right] + prev) % MOD


        return combinations[-1]


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 7 + 10**9
        N = len(nums)
        combinations = [0]*N
        prefix = [0]*N

        minIds = deque()
        maxIds = deque()

        left = 0

        for right in range(N):
            while minIds and nums[minIds[-1]] >= nums[right]:
                minIds.pop()
            while maxIds and nums[maxIds[-1]] <= nums[right]:
                maxIds.pop()

            minIds.append(right)
            maxIds.append(right)

            while nums[maxIds[0]] -  nums[minIds[0]] > k:
                if minIds[0] == left:
                    minIds.popleft()
                if maxIds[0] == left:
                    maxIds.popleft()
                left += 1

            prevSum = 1 if right == 0 else prefix[right-1]
            excludeSum = 0
            if left - 2 == -2:
                excludeSum = 0
            elif left - 2 == -1:
                excludeSum = 1
            else:
                excludeSum = prefix[left - 2]

            combinations[right] = (prevSum - excludeSum) % MOD
            prefix[right] = (prevSum + combinations[right]) % MOD


        # print(
        #     'combinations', combinations,
        #     'prefix', prefix,
        # )

        return combinations[-1]

'''
[9,4,1,3,7], 4]

9,4,1,3,7
1 1 2 4 6

---

[[3,3,4], 0]
3,3,4
1 2 2

---

[9,4,1,3,7], 4]
- - 9,4,1,3,7
0 1 1 1 2 4 6
0 1 2 3 5 9 15

---

[[3,3,4], 0]
3,3,4
1 2 2
2 4 6

---

[2,9,5,4,20], 12

- 2,9,5,4,20
1 1 2 4 8 8



- - 2,9,5,4,20
0 1 1 2 4 8 16-8
0 1 2 4 8 16 24



combinations
[1, 2, 4, 8, 15] prefix
[2, 4, 8, 16, 31]



'''



def test ():
    params = [
        # {
        #     'input': [[9,4,1,3,7], 4],
        #     'output': 6,
        # },
        # {
        #     'input': [[3,3,4], 0],
        #     'output': 2,
        # },
        {
            'input': [[2,9,5,4,20], 12],
            'output': 8,
        },
    ]
    solution = Solution()

    for param in params:
        nums, k = param['input']
        result = solution.countPartitions(nums, k)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
