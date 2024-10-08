from typing import List


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        s = 0

        length = len(columnTitle)
        for i in range(length):
            num = ord(columnTitle[length - 1 - i]) - ord('A') + 1
            print(columnTitle[length - 1 - i], num)

            if i == 0:
                s += num
            else:
                v = num * 26**i
                s += v

        return s


def test ():
    params = [
        {
            'input': 'A',
            'output': 1,
        },
        {
            'input': 'AB',
            'output': 28,
        },
        {
            'input': 'ZY',
            'output': 701,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.titleToNumber(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
