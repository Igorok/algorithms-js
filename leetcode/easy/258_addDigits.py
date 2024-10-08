from typing import List


class Solution:
    def addDigits(self, num: int) -> int:
        result = num

        while result >= 10:
            s = 0
            r = result
            while r != 0:
                s += r % 10
                r = r // 10
            result = s

        return result


def test ():
    params = [
        {
            'input': 38,
            'output': 2,
        },
        {
            'input': 0,
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.addDigits(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
