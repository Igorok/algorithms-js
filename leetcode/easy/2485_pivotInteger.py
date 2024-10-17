from typing import List
import math

class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1

        prefix = [None]*(n+1)
        prefix[0] = 0
        postfix = [None]*(n+1)
        postfix[-1] = n

        for i in range(1, n+1):
            prefix[i] = i + prefix[i - 1]

        for i in range(n-1, -1, -1):
            postfix[i] = i + postfix[i + 1]
            if (postfix[i] == prefix[i]):
                return i


        print(
            'prefix', prefix,
            'postfix', postfix,
        )

        return -1


def test ():
    params = [
        {
            'input': 8,
            'output': 6,
        },
        {
            'input': 1,
            'output': 1,
        },
        {
            'input': 4,
            'output': -1,
        },


    ]
    solution = Solution()

    for param in params:
        result = solution.pivotInteger(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
