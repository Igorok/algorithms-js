import sys
sys.setrecursionlimit(1500)
from typing import List
import json
from collections import deque, defaultdict
import heapq
import math

class Solution:
    def isInterleave_0(self, s1: str, s2: str, s3: str) -> bool:
        def rec(s1, c1, s2, c2, s3):
            if abs(c1 - c2) > 2:
                return False

            if s1 == s2 and s2 == s3 and s3 == '':
                return True

            if (len(s1) == 0 and s2 == s3) or (len(s2) == 0 and s1 == s3):
                return True

            if (len(s1) == 0 and s2 != s3) or (len(s2) == 0 and s1 != s3):
                return False

            if s1 and s1[0] == s3[0] and rec(s1[1:], c1+1, s2, c2, s3[1:]):
                return True

            if s2 and s2[0] == s3[0] and rec(s1, c1, s2[1:], c2+1, s3[1:]):
                return True

            return False

        return rec(s1, 0, s2, 0, s3)

    def isInterleave_1(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        cache = {}
        def rec(s1, c1, s2, c2, s3):
            if (s1, c1, s2, c2, s3) in cache:
                return cache[(s1, c1, s2, c2, s3)]

            if abs(c1 - c2) > 2:
                cache[(s1, c1, s2, c2, s3)] = False
                return False

            if (not s1 and s2 == s3) or (not s2 and s1 == s3):
                cache[(s1, c1, s2, c2, s3)] = True
                return True

            if (not s1 and s2 != s3) or (not s2 and s1 != s3):
                cache[(s1, c1, s2, c2, s3)] = False
                return False

            params1 = []
            params2 = []
            for i in range(1, min(len(s1), len(s3))+1):
                if s1[:i] == s3[:i] and rec(s1[i:], c1+1, s2, c2, s3[i:]):
                    params1.append((s1[i:], c1+1, s2, c2, s3[i:]))

            for i in range(1, min(len(s2), len(s3))+1):
                if s2[:i] == s3[:i] and rec(s1, c1, s2[i:], c2+1, s3[i:]):
                    params2.append((s1, c1, s2[i:], c2+1, s3[i:]))

            while params1 or params2:
                if params1:
                    p = params1.pop()
                    if rec(p[0], p[1], p[2], p[3], p[4]):
                        cache[(s1, c1, s2, c2, s3)] = True
                        return True

                if params2:
                    p = params2.pop()
                    if rec(p[0], p[1], p[2], p[3], p[4]):
                        cache[(s1, c1, s2, c2, s3)] = True
                        return True

            cache[(s1, c1, s2, c2, s3)] = False
            return False

        return rec(s1, 0, s2, 0, s3)

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        cache = {}
        def rec(s1, c1, s2, c2, s3, isFirst, isSecond):
            if (s1, s2, s3) in cache:
                return cache[(s1, s2, s3)]

            if abs(c1 - c2) > 2:
                return False

            if (not s1 and s2 == s3) or (not s2 and s1 == s3):
                return True

            if (not s1 and s2 != s3) or (not s2 and s1 != s3):
                return False

            if s1 and s1[0] == s3[0]:
                count = c1 if isFirst else c1+1
                r = rec(s1[1:], count, s2, c2, s3[1:], True, False)
                if r:
                    cache[(s1, s2, s3)] = True
                    return True

            if s2 and s2[0] == s3[0]:
                count = c2 if isSecond else c2+1
                r = rec(s1, c1, s2[1:], count, s3[1:], False, True)
                if r:
                    cache[(s1, s2, s3)] = True
                    return True

            cache[(s1, s2, s3)] = False
            return False

        return rec(s1, 0, s2, 0, s3, False, False)


'''
aabcc
dbbca
aadbbcbcac

aa bc c
dbbc a
aa dbbc bc a c

---

aabcc
dbbca
aadbbbaccc

aa b cc
dbb ca
aa dbb b accc

---

a abc
a bad
a a bad abc


'''

def test ():
    params = [
        {
            'input': ["aaaa", "aa", "aaa"],
            'output': False,
        },
        {
            'input': ["aabcc", "dbbca", "aadbbcbcac"],
            'output': True,
        },
        {
            'input': ["aabcc", "dbbca", "aadbbbaccc"],
            'output': False,
        },
        {
            'input': ["", "", ""],
            'output': True,
        },
        {
            'input': ["abc", "cde", "abcdec"],
            'output': True,
        },
        {
            'input': ["", "abc", "abc"],
            'output': True,
        },
        {
            'input': ["aabc", "abad", "aabadabc"],
            'output': True,
        },
        {
            'input': [
                "abababababababababababababababababababababababababababababababababababababababababababababababababbb",
                "babababababababababababababababababababababababababababababababababababababababababababababababaaaba",
                "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababbb"
            ],
            'output': False,
        },
    ]
    solution = Solution()

    for param in params:
        s1, s2, s3 = param['input']

        result = solution.isInterleave(s1, s2, s3)
        correct = json.dumps(result) == json.dumps(param['output'])

        msg = 'SUCCESS' if json.dumps(result) == json.dumps(param['output']) else 'ERROR'
        msg += '\n'
        if not correct:
            msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()
