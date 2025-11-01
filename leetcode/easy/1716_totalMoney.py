from typing import List


class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        days = n % 7

        res = 0
        for i in range(1, weeks + 1):
            # s = (a1+an)* n/2
            res += (i + i+6)*7/2

        for i in range(days):
            res += weeks + 1 + i

        return int(res)


def test ():
    params = [
        {
            'input': 4,
            'output': 10,
        },
        {
            'input': 10,
            'output': 37,
        },
        {
            'input': 20,
            'output': 96,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.totalMoney(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
