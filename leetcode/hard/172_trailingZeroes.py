from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def trailingZeroes_0(self, n: int) -> int:
        res = 0
        num = 1
        for i in range(1, n+1):
            num *= i
            print(
                'i', i, 'num', num,
                '\n',
            )

            r = 0
            val = num
            while (val % 10) == 0:
                val = val // 10
                r += 1
            res = max(res, r)

        return res

    def trailingZeroes(self, n: int) -> int:
        return n//5 + n//25 + n//125 + n//625 + n //3125

'''

i 1 num 1
i 2 num 2
i 3 num 6
i 4 num 24
i 5 num 120
i 6 num 720
i 7 num 5040
i 8 num 40320
i 9 num 362880
i 10 num 3628800
i 11 num 39916800
i 12 num 479001600
i 13 num 6227020800
i 14 num 87178291200
i 15 num 1307674368000
i 16 num 20922789888000
i 17 num 355687428096000
i 18 num 6402373705728000
i 19 num 121645100408832000
i 20 num 2432902008176640000
i 21 num 51090942171709440000
i 22 num 1124000727777607680000
i 23 num 25852016738884976640000
i 24 num 620448401733239439360000
i 25 num 15511210043330985984000000
i 26 num 403291461126605635584000000
i 27 num 10888869450418352160768000000
i 28 num 304888344611713860501504000000
i 29 num 8841761993739701954543616000000
i 30 num 265252859812191058636308480000000


'''

def test ():
    params = [
        {
            'input': 10000,
            'output': 249,
        },
        {
            'input': 1000,
            'output': 249,
        },
        {
            'input': 1574,
            'output': 390,
        },
        {
            'input': 20,
            'output': 4,
        },
        {
            'input': 3,
            'output': 0,
        },
        {
            'input': 5,
            'output': 1,
        },
        {
            'input': 0,
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        n = param['input']
        result = solution.trailingZeroes(n)
        correct = json.dumps(result) == json.dumps(param['output'])

        msg = 'SUCCESS' if correct else 'ERROR'
        msg += '\n'
        if not correct:
            msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()
