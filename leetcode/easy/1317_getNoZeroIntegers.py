from typing import List


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            n1 = str(i)
            n2 = str(n - i)
            if '0' in n1 or '0' in n2:
                continue

            return [i, n-i]

        return [1, 1]


def test ():
    params = [
        {
            'input': 2,
            'output': [1,1],
        },
        {
            'input': 11,
            'output': [2,9],
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.getNoZeroIntegers(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
