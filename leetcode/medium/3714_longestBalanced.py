from typing import List
from collections import deque, defaultdict
from functools import cache
import re

class Solution:
    def longestBalanced(self, s: str) -> int:
        N = len(s)
        res = 0

        abCnt = {'a': 0, 'b': 0}
        acCnt = {'a': 0, 'c': 0}
        bcCnt = {'b': 0, 'c': 0}
        abDiffId = {0: -1}
        acDiffId = {0: -1}
        bcDiffId = {0: -1}

        singleCnt = 0
        diffCnt = {(0,0): -1}
        aCnt = 0
        bCnt = 0
        cCnt = 0
        aPrefix = [0]*N
        bPrefix = [0]*N
        cPrefix = [0]*N


        for i in range(N):
            # one char
            prev = '*' if i == 0 else s[i-1]
            singleCnt = 1 if s[i] != prev else singleCnt + 1
            res = max(res, singleCnt)

            #two chars
            if s[i] == 'a':
                bcDiffId = {0: i}
                bcCnt = {'b': 0, 'c': 0}

                abCnt['a'] += 1
                acCnt['a'] += 1

                if (abCnt['a'] - abCnt['b']) not in abDiffId:
                    abDiffId[(abCnt['a'] - abCnt['b'])] = i
                else:
                    res = max(res, i - abDiffId[(abCnt['a'] - abCnt['b'])])

                if (acCnt['a'] - acCnt['c']) not in acDiffId:
                    acDiffId[(acCnt['a'] - acCnt['c'])] = i
                else:
                    res = max(res, i - acDiffId[(acCnt['a'] - acCnt['c'])])

            elif s[i] == 'b':
                acDiffId = {0: i}
                acCnt = {'a': 0, 'c': 0}

                abCnt['b'] += 1
                bcCnt['b'] += 1

                if (abCnt['a'] - abCnt['b']) not in abDiffId:
                    abDiffId[(abCnt['a'] - abCnt['b'])] = i
                else:
                    res = max(res, i - abDiffId[(abCnt['a'] - abCnt['b'])])

                if (bcCnt['b'] - bcCnt['c']) not in bcDiffId:
                    bcDiffId[(bcCnt['b'] - bcCnt['c'])] = i
                else:
                    res = max(res, i - bcDiffId[(bcCnt['b'] - bcCnt['c'])])
            else:
                abDiffId = {0: i}
                abCnt = {'a': 0, 'b': 0}

                acCnt['c'] += 1
                bcCnt['c'] += 1

                if (acCnt['a'] - acCnt['c']) not in acDiffId:
                    acDiffId[(acCnt['a'] - acCnt['c'])] = i
                else:
                    res = max(res, i - acDiffId[(acCnt['a'] - acCnt['c'])])

                if (bcCnt['b'] - bcCnt['c']) not in bcDiffId:
                    bcDiffId[(bcCnt['b'] - bcCnt['c'])] = i
                else:
                    res = max(res, i - bcDiffId[(bcCnt['b'] - bcCnt['c'])])

            # thee chars
            if s[i] == 'a':
                aCnt += 1
            elif s[i] == 'b':
                bCnt += 1
            else:
                cCnt += 1

            aPrefix[i] = aCnt
            bPrefix[i] = bCnt
            cPrefix[i] = cCnt

            abDiff = aCnt - bCnt
            bcDiff = bCnt - cCnt

            if (abDiff, bcDiff) not in diffCnt:
                diffCnt[(abDiff, bcDiff)] = i
            else:
                id = diffCnt[(abDiff, bcDiff)]
                aPrev = 0 if id == -1 else aPrefix[id]
                aDiff = aPrefix[i] - aPrev

                bPrev = 0 if id == -1 else bPrefix[id]
                bDiff = bPrefix[i] - bPrev

                cPrev = 0 if id == -1 else cPrefix[id]
                cDiff = cPrefix[i] - cPrev

                if aDiff == bDiff and bDiff == cDiff:
                    res = max(res, i - id)

        return res
'''

aaabbcbcc
10_000
3333

aaabbbbbbccccc

_ a a a b b c b c c
0 1 2 3 3 3 3 3 3 3
0 0 0 0 1 2 2 3 3 3
0 0 0 0 0 0 1 1 2 3

a b c a a c b
1 1 1 2 3 3 3
0 1 1 1 1 1 2
0 0 1 1 1 2 2

b c a a a b c
0 0 1 2 3 3 3
1 1 1 1 1 2 2
0 1 1 1 1 1 2

a a a c a a a a
1 2 3 3 4 5 6 7
0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 1

a b c a b c a a a a b c a b c a b c
1 1 1 2 2 2 3 4 5 6 6 6 7 7 7 8 8 8
0 1 1 1 2 2 2 2 2 2 3 3 3 4 4 4 5 5
0 0 1 1 1 2 2 2 2 2 2 3 3 3 4 4 4 5

a b c
1 1 1
0 1 1
0 0 1


a a b c c
1 2 2 2 2
0 0 1 1 1
0 0 0 1 2


a a a a a a b b a a a a  a  a  b  b
1 2 3 4 5 6 6 6 7 8 9 10 11 12 12 12
0 0 0 0 0 0 1 2 2 2 2 2  2  2  3  4
1 2 3 4 5 6 5 4 5 6 7 8  9  10 9  8


'''

def test ():
    params = [
        {
            'input': 'abbac',
            'output': 4,
        },
        {
            'input': 'aabcc',
            'output': 3,
        },
        {
            'input': 'aba',
            'output': 2,
        },
        {
            'input': 'aaabbcbcc',
            'output': 9,
        },
        {
            'input': 'aaabbbbbbcccccc',
            'output': 12,
        },
        {
            'input': 'abbbbbbbbc',
            'output': 8,
        },
        {
            'input': 'abc',
            'output': 3,
        },
        {
            'input': 'cbbbc',
            'output': 3,
        },
    ]
    solution = Solution()

    for param in params:
        nums = param['input']
        result = solution.longestBalanced(nums)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            # 'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
