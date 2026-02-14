from typing import List
import json
from collections import deque, defaultdict

class Solution_0:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        aTotal = 0
        for i in range(n):
            if s[i] == 'a':
                aTotal += 1

        aCount = 0
        bCount = 0
        res = float('inf')

        for i in range(n):
            if s[i] == 'a':
                aCount += 1
            if s[i] == 'b':
                bCount += 1

            ac = aTotal - aCount
            r = bCount + ac
            if aCount == 0:
                r = min(r, aTotal)

            res = min(res, r)


        return res



class Solution_1:
    def minimumDeletions(self, s: str) -> int:
        N = len(s)

        @cache
        def dfs(id, isB):
            if id == N:
                return 0

            r = 0
            if s[id] == 'a':
                if isB:
                    return 1 + dfs(id+1, isB)
                else:
                    return dfs(id+1, isB)
            else:
                if isB:
                    return dfs(id+1, isB)
                else:
                    r1 = 1 + dfs(id+1, isB)
                    r2 = dfs(id+1, True)
                    return min(r1, r2)

            return 0

        return dfs(0, False)


class Solution:
    def minimumDeletions(self, s: str) -> int:
        N = len(s)
        aCount = [0] * N
        bCount = [0] * N

        aCount[0] = 1 if s[0] == 'a' else 0
        bCount[0] = 1 if s[0] == 'b' else 0

        for i in range(1, N):
            aCount[i] = aCount[i-1] if s[i] == 'b' else aCount[i-1]+1
            bCount[i] = bCount[i-1] if s[i] == 'a' else bCount[i-1]+1

        res = min(aCount[-1], bCount[-1])

        for i in range(0, N):
            prevA = 0 if i == 0 else aCount[i-1]
            prevB = 0 if i == 0 else bCount[i-1]

            nextA = aCount[-1] - prevA

            res = min(res, prevB + nextA)

        return res

'''

a a b a b b a b
1 2 2 3 3 3 4 4
0 0 1 1 2 3 3 4

a a a b b a b b

---


b b a a a a a b b
0 0 1 2 3 4 5 5 5
1 2 2 2 2 2 2 3 4

b b b b a a a a a
0 0 0 0 1 2 3 4 5
1 2 3 4 4 4 4 4 4
5 6 7 8

'''


def test ():
    params = [
        {
            'input': 'aababbab',
            'output': 2,
        },
        {
            'input': 'bbaaaaabb',
            'output': 2,
        },
        {
            'input': 'bbbbaa',
            'output': 2,
        },
        {
            'input': 'bbbbaaaaa',
            'output': 4,
        },
        {
            'input': 'abbbbaa',
            'output': 2,
        },
        {
            'input': 'ababababaaaaa',
            'output': 4,
        },
    ]
    solution = Solution()

    for param in params:
        s = param['input']
        result = solution.minimumDeletions(s)
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
