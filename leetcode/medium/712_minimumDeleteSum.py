from typing import List
import heapq
import math
from collections import defaultdict, deque

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        N = len(s1)
        M = len(s2)

        total = 0
        for i in range(N):
            total += ord(s1[i])
        for i in range(M):
            total += ord(s2[i])

        memo = [[-1]*M for i in range(N)]

        def dfs(id1, id2):
            if id1 == N or id2 == M:
                return 0

            if memo[id1][id2] != -1:
                return memo[id1][id2]

            res = 0
            if s1[id1] == s2[id2]:
                res += ord(s1[id1])
                res += dfs(id1+1, id2+1)

            r1 = dfs(id1+1, id2)
            if r1 > res:
                res = r1
            r1 = dfs(id1, id2+1)
            if r1 > res:
                res = r1

            memo[id1][id2] = res

            return res

        subSrtSum = dfs(0, 0)

        return total - subSrtSum*2

'''
- s e a
e 0 1 1
a 0 1 2
t 0 1 2
'''

def test ():
    params = [
        {
            'input': ["sea", "eat"],
            'output': 231,
        },
        {
            'input': ["delete", "leet"],
            'output': 403,
        },
    ]
    solution = Solution()

    for param in params:
        s1, s2 = param['input']
        result = solution.minimumDeleteSum(s1, s2)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
