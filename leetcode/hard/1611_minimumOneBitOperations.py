from typing import List
import json
from collections import deque, defaultdict
import math

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0

        i = -1
        k = 1
        while k <= n:
            k = k << 1
            i += 1

        k = int(2**i)
        diff = n ^ k

        return 2**(i+1) - 1 - self.minimumOneBitOperations(diff)

'''
[i-1] == 1
[i-2] == 0

3
011
001
000

6
0110
0010
0011
0001
0000

8
1000
1001
1011
1010
1110
1111
1101
1100
0100

2^3-1

4
100
101
111
110
010
011
001
010


https://en.wikipedia.org/wiki/Gray_code

'''


def test ():
    params = [
        {
            'input': 4,
            'output': 7,
        },
        {
            'input': 3,
            'output': 2,
        },
        {
            'input': 6,
            'output': 4,
        },

    ]
    solution = Solution()

    for param in params:
        s = param['input']
        result = solution.minimumOneBitOperations(s)
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
