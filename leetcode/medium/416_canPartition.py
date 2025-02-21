from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def canPartition_0(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if (totalSum % 2) == 1:
            return False

        sortedNums = sorted(nums)
        start = 0
        end = len(sortedNums) - 1
        partSum = 0
        while start <= end:
            last = sortedNums[end]
            first = sortedNums[start]

            if partSum + last == totalSum / 2:
                return True

            if totalSum / 2 > partSum + last:
                partSum += last
                end -= 1
                continue

            if totalSum / 2 == partSum + first:
                return True

            partSum += first
            start += 1

        return False

    def canPartition_1(self, nums: List[int]) -> bool:
        sortedNums = nums
        totalSum = sum(nums)

        if (totalSum % 2) == 1:
            return False
        halfSum = totalSum // 2

        memo = [[0]*(halfSum + 1) for n in sortedNums]

        for i in range(len(sortedNums)):
            num = sortedNums[i]
            for s in range(len(memo[i])):
                if s < num:
                    if i > 0 and memo[i-1][s] == 1:
                        memo[i][s] = 1
                    continue

                if s == num:
                    memo[i][s] = 1
                    continue

                if i == 0:
                    break;

                diff = s - num
                if memo[i-1][diff] or memo[i-1][s]:
                    memo[i][s] = 1

            if memo[i][-1] == 1:
                return True

        return False

    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)

        if (totalSum % 2) == 1:
            return False
        halfSum = totalSum // 2

        prev = [0]*(halfSum+1)

        for i in range(len(nums)):
            curr = [0] * (halfSum + 1)
            num = nums[i]
            for s in range(halfSum+1):
                if s < num:
                    if i > 0 and prev[s] == 1:
                        curr[s] = 1
                    continue

                if s == num:
                    curr[s] = 1
                    continue

                if i == 0:
                    break;

                diff = s - num
                if prev[diff] or prev[s]:
                    curr[s] = 1

            if curr[-1] == 1:
                return True
            prev = curr

        return False



'''
26 + 14 = 40
[14,9,8,4,3,2]
2, 3, 4, 8, 9, 14
14+4+2=20
3+9+8=20

2, 3, 4, 8, 9, 14
20
14 9 8 4 3 2
6
9 8 4 3 2
2
9 8 3 2
2

  0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
2 0 0 2 2 2 2 2 2 2 2 2  2  2  2
3 0 0 2 3 3 5 5 5 5 5 5  5  5  5
4 0 0 2 3 4 5 6 7 7 9 9  9  9  9
8 0 0 2 3 4 5 6 7 8 9 10 11 12 13 14 15 15 17 17 17 17
9 0 0 2 3 4 5 6 7 8 9 9  11 12 13 15 15 16 17 18 19 20
14

1 2 5 = 8
  0 1 2 3 4
1 0 1 0 0 0
2 0 1 1 1 0
5 0 1 1 1 0


'''


def test ():
    params = [
        {
            'input': [1,2,5],
            'output': False,
        },
        {
            'input': [14,9,8,4,3,2],
            'output': True,
        },
        {
            'input': [1,5,11,5],
            'output': True,
        },
        {
            'input': [1,2,3,5],
            'output': False,
        },
        {
            'input': [1,1,1,1,1,5],
            'output': True,
        },
    ]
    solution = Solution()

    for param in params:
        nums = param['input']
        result = solution.canPartition(nums)
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
