from typing import List


class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0

        for i in range(1, len(s)):
            prev = ord(s[i-1])
            cur = ord(s[i])
            res += abs(prev - cur)

        return res


def test ():
    params = [
        {
            'input': "hello",
            'output': 13,
        },
        {
            'input': "zaz",
            'output': 50,
        },

    ]
    solution = Solution()

    for param in params:
        result = solution.scoreOfString(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
