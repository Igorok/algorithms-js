from typing import List

class Solution:
    def strangePrinter(self, s: str) -> int:
        letters = []
        for i in range(len(s)):
            if i+1 == len(s) or s[i] != s[i+1]:
                letters.append(s[i])

        cache = {}
        def rec(start, end):
            if start > end:
                return 0

            if (start, end) in cache:
                return cache[(start, end)]

            prints = 1 + rec(start + 1, end)

            for i in range(start + 1, end + 1):
                if s[i] == s[start]:
                    parts = rec(start, i - 1) + rec(i + 1, end)
                    prints = min(parts, prints)


            cache[(start, end)] = prints
            return prints

        return rec(0, len(s) - 1)



def test ():
    params = [
        {
            'input': 'aaaaabbbb',
            'output': 2,
        },
        {
            'input': 'aba',
            'output': 2,
        },
        {
            'input': 'abcabc',
            'output': 5,
        },
        {
            'input': 'aabaaabaa',
            'output': 3,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.strangePrinter(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

'''
[1,2,3,4,   5,6,7,8,9]
'''


if __name__ == '__main__':
    test()
