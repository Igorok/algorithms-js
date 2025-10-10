from typing import List
from json import dumps
from collections import defaultdict, deque
import heapq


class Solution_0:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        m = len(mana)
        prev = [0]*n

        for i in range(n):
            start = 0 if i == 0 else prev[i-1]
            prev[i] = start + skill[i] * mana[0]

        for i in range(1, m):
            curr = [0]*n
            for j in range(n):
                start = max(prev[j], (0 if j == 0 else curr[j-1]))
                curr[j] = start + skill[j] * mana[i]

            for j in range(n-2, -1, -1):
                curr[j] = curr[j+1] - skill[j+1] * mana[i]

            prev = curr

        return prev[-1]


class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        m = len(mana)

        prefix = [0]*(n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + skill[i]

        res = 0
        for i in range(1, m):
            maxTime = 0
            for j in range(n):
                currentStarted = prefix[j+1] * mana[i-1]
                prevCompleted = prefix[j] * mana[i]
                maxTime = max(maxTime, res + currentStarted - prevCompleted)
            res = maxTime

        res += prefix[-1] * mana[-1]

        return res


'''
[[1,5,2,4], [5,1,4,2]]

- 0  - 1   5   2   4
5 0  - 5   30  40  60
1 52 - 53  58  60  64
4 5  - 10  55  63  80
2


- 1 6  8  12
5 5 30 40 60
1 1 6  8  12
4
2



'''

def test ():
    params = [
        {
            'input': [[1,5,2,4], [5,1,4,2]],
            'output': 110,
        },
        {
            'input': [[1,1,1], [1,1,1]],
            'output': 5,
        },
        {
            'input': [[1,2,3], [1,2,1]],
            'output': 16,
        },
        {
            'input': [[1,10,3,6,6,8], [1,5,2,2,7]],
            'output': 397,
        },
    ]
    solution = Solution()

    for param in params:
        skill, mana = param['input']
        result = solution.minTime(skill, mana)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

if __name__ == '__main__':
    test()
