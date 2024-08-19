from typing import List


class Solution:
    def minSteps_(self, n: int) -> int:
        if n == 1:
            return 0

        cache = {}
        def rec(current, copied):
            if current == n:
                return 0
            elif current > n:
                return 1001
            elif (current, copied) in cache:
                return cache[(current, copied)]

            r1 = 1 + rec(current + copied, copied)
            r2 = 2 + rec(current + current, current)
            cache[(current, copied)] = min(r1, r2)

            return cache[(current, copied)]

        return 1 + rec(1, 1)

    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        x = 1
        r = 1
        o = 1
        while r < n:
            r += x
            o += 1
            if n % r == 0 and r != n:
               x = r
               o += 1

        return o

'''
3
c a
p aa
p aaa

20
c a
p aa
c aa
p aaaa
c aaaa
p aaaaaaaa
p aaaaaaaaaaaa
p aaaaaaaaaaaaaaaa
p aaaaaaaaaaaaaaaaaaaa

20
1 x1 0
2 x2







'''


def test ():
    params = [
        {
            'input': 3,
            'output': 3,
        },
        {
            'input': 1,
            'output': 0,
        },
        {
            'input': 6,
            'output': 5,
        },
        {
            'input': 20,
            'output': 9,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.minSteps(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
