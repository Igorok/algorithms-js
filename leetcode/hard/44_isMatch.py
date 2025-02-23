from typing import List
import json
from collections import deque

class Solution:
    def isMatch_0(self, s: str, p: str) -> bool:
        lengthP = len(p)
        lengthS = len(s)
        cache = {}

        res = False
        def isMatch(y, x):
            if (lengthS, lengthP) in cache:
                return cache[(lengthS, lengthP)]
            if (y, x) in cache:
                return cache[(y, x)]

            if x == lengthP and y == lengthS:
                cache[(y, x)] = True
                return True

            if x == lengthP and y < lengthS:
                cache[(y, x)] = False
                return False

            if x < lengthP and y == lengthS:
                for i in range(x, lengthP):
                    if p[i] != '*':
                        cache[(y, x)] = False
                        return False
                cache[(y, x)] = True
                return True

            if s[y] == p[x] or p[x] == '?':
                r = isMatch(y + 1, x + 1)
                cache[(y, x)] = r
                return r

            if p[x] == '*':
                i = y
                while i <= lengthS:
                    r = isMatch(i, x + 1)
                    if cache[(i, x+1)] == True:
                        cache[(y, x)] = r
                        return True
                    i += 1

                cache[(y, x)] = False
                return False

            cache[(y, x)] = False
            return False

        return isMatch(0, 0)

    def isMatch(self, s: str, p: str) -> bool:
        lengthP = len(p)
        lengthS = len(s)
        cache = {}

        res = False
        def isMatch(y, x):
            if (lengthS, lengthP) in cache:
                return cache[(lengthS, lengthP)]
            if (y, x) in cache:
                return cache[(y, x)]

            if x == lengthP and y == lengthS:
                cache[(y, x)] = True
                return True

            if x == lengthP and y < lengthS:
                cache[(y, x)] = False
                return False

            if x < lengthP and y == lengthS:
                for i in range(x, lengthP):
                    if p[i] != '*':
                        cache[(y, x)] = False
                        return False
                cache[(y, x)] = True
                return True

            if s[y] == p[x] or p[x] == '?':
                r = isMatch(y + 1, x + 1)
                cache[(y, x)] = r
                return r

            if p[x] == '*':
                cache[(y, x)] = isMatch(y, x + 1) or isMatch(y + 1, x)
                return cache[(y, x)]

            cache[(y, x)] = False
            return False

        return isMatch(0, 0)


def test ():
    params = [
        # {
        #     'input': [
        #         "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        #         "*aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa*"
        #     ],
        #     'output': False,
        # },
        {
            'input': [
                "aababbbbaaabaabaabbbbbaabbaabaaaabaaabbbaaaaabbbaaaabaaababbbbbbabbbabaababbbaaaaaaabaaaabbbaabbbaaabaaaababbababbaabaaaaabaaababbaababbabbbbabaabababbabbabbababbbbaaaabbbaabbaabbaabababbbbaaaabbabaaabbab",
                "*bbb*b*****a*abaab****a****b***a*ab*bb***b**bb*b*aab*aaa*a*b*bbbb*a*a*****ba**bb*b*****b*a*bb*******aa"
            ],
            'output': False,
        },
        {
            'input': [
                "bbbbaababbbbaabaaabbbbbbabbabbaaabaabbbaaaaaababababbbbbaabbaababbbbbabbababbaabaaabbbababaabbabbbaabbbabbbaabbabbbabbbbabbaabbbbbbaabababbaaaababbbaaabbbbaaabbbbabaabaaababbabbbabaaabbbbbbbbaabaabbabb",
                "b*ab*b****b*a**b**b****abbba**a*baa****b*ab****bbabaaaab***ab****aba***a******aa*ba*bba****aa******b*b**",
            ],
            'output': False,
        },

        {
            'input': ["adceb", "*a*b"],
            'output': True,
        },
        {
            'input': ["aa", "a"],
            'output': False,
        },
        {
            'input': ["aa", "*"],
            'output': True,
        },
        {
            'input': ["cb", "?a"],
            'output': False,
        },
        {
            'input': ["aa", "a?"],
            'output': True,
        },
        {
            'input': ["cb", "??"],
            'output': True,
        },
        {
            'input': ["caaaaaab", "c*b"],
            'output': True,
        },
        {
            'input': ["cb", "c*b"],
            'output': True,
        },
        {
            'input': ["cbbbbbbb", "c*b"],
            'output': True,
        },
    ]
    solution = Solution()

    for param in params:
        s, p = param['input']
        result = solution.isMatch(s, p)
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
