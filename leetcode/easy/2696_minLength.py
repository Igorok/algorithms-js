from typing import List

class Solution:
    def minLength(self, s: str) -> int:
        ab = 'AB'
        cd = 'CD'
        def rec(s):
            minS = ''
            points = []
            for i in range(len(s) - 1):
                if s[i:i+2] == ab or s[i:i+2] == cd:
                    points.append((i, i+1))

            if len(points) == 0:
                return s
            else:
                start = 0
                for l, r in points:
                    if l == start:
                        start = r + 1
                    else:
                        minS += s[start:l]
                        start = r + 1
                if start < len(s):
                    minS += s[start:len(s)]

                print(points)
                print(minS)

                return rec(minS)

        minS = rec(s)

        return len(minS)

    def minLength(self, s: str) -> int:
        if len(s) <= 2 and s != 'AB' and s != 'CD':
            return len(s)

        stack = []

        for i in range(len(s)):
            if len(stack) > 0 and stack[-1] + s[i] in ('AB', 'CD'):
                stack.pop()
            else:
                stack.append(s[i])

        return len(stack)


def test ():
    params = [
        {
            'input': 'ABFCACDB',
            'output': 2,
        },
        {
            'input': 'ACBBD',
            'output': 5,
        },

    ]
    solution = Solution()

    for param in params:
        result = solution.minLength(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
