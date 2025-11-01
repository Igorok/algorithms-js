from typing import List
import math

class Solution:
    def maximumSwap(self, num: int) -> int:
        data = list(str(num))
        n = len(data)
        rightMax = [None]*n
        rightMax[n-1] = (data[-1], n-1)

        for i in range(n-2, -1, -1):
            rightMax[i] = rightMax[i+1] if rightMax[i+1][0] >= data[i] else (data[i], i)

        for i in range(n):
            if data[i] < rightMax[i][0]:
                id = rightMax[i][1]
                data[i], data[id] = data[id], data[i]
                break

        return int(''.join(data))


def test ():
    params = [
        {
            'input': 2736,
            'output': 7236,
        },
        {
            'input': 9973,
            'output': 9973,
        },
        {
            'input': 985438,
            'output': 988435,
        },
        {
            'input': 1993,
            'output': 9913,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.maximumSwap(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
