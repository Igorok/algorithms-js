from typing import List


class Solution:
    def isUgly(self, n: int) -> bool:
        num = n
        dividers = (2, 3, 5)

        while True:
            r = num
            for v in dividers:
                if r % v == 0:
                    r = r // v
            if r == num:
                break
            else:
                num = r

        return num in (0,1,2,3,5)


def test ():
    params = [
        {
            'input': 6,
            'output': True,
        },
        {
            'input': 1,
            'output': True,
        },
        {
            'input': 14,
            'output': False,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.isUgly(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
