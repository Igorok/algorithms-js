from typing import List


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        start = 1
        end = num // 2

        while start <= end:
            middle = (start + end) // 2
            square = middle**2
            if square == num:
                return True
            if square > num:
                end = middle - 1
            else:
                start = middle + 1

        return False


def test ():
    params = [
        {
            'input': 16,
            'output': True,
        },
        {
            'input': 14,
            'output': False,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.isPerfectSquare(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
