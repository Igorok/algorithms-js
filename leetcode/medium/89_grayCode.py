from typing import List
import json
from collections import deque, defaultdict
import math

class Solution:
    def grayCode_0(self, n: int) -> List[int]:
        length = 2**n
        middle = length // 2
        allNumbers = set([0])
        res = [0]

        def getBitSum(num):
            s = 0
            while num != 0:
                s += (num & 1)
                num = num >> 1
            return s

        def getPlusOneBit(num):
            nonlocal allNumbers

            prev = bin(num)[2:]
            zeros = '0'*(32-len(prev))
            prev = zeros + prev
            arr = []

            for i in range(31, -1, -1):
                if prev[i] == '0':
                    n = int(prev[:i] + '1' + prev[i+1:], 2)
                    if n >= length:
                        break
                    if not n in allNumbers:
                        arr.append(n)
            return arr

        def getMinusOneBit(num):
            nonlocal allNumbers

            prev = bin(num)[2:]
            zeros = '0'*(32-len(prev))
            prev = zeros + prev
            arr = []

            for i in range(31, -1, -1):
                if prev[i] == '1':
                    n = int(prev[:i] + '0' + prev[i+1:], 2)
                    if n >= length:
                        break
                    if not n in allNumbers:
                        arr.append(n)
            return arr

        def rec():
            nonlocal res, allNumbers

            if len(res) == length:
                return getBitSum(res[-1]) == 1

            arr = getMinusOneBit(res[-1]) + getPlusOneBit(res[-1])

            for num in arr:
                res.append(num)
                allNumbers.add(num)
                r = rec()
                if r:
                    return True
                else:
                    res.pop()
                    allNumbers.remove(num)

        rec()

        return res

    # def grayCode(self, n: int) -> List[int]:
    #     return [i ^ (i >> 1) for i in range(1 << n)]


    def grayCode(self, n: int) -> List[int]:
        res = [0]

        for i in range(0, n):
            l = len(res)
            val = 1 << i
            for j in range(l-1, -1, -1):
                res.append(val + res[j])

        return res


'''

https://en.wikipedia.org/wiki/Gray_code

0
---
10

00
10
---
100

000
010
110
100
---
1000

0000
0010
0110
0100
1100
1110
1010
1000

'''


def test ():
    params = [
        {
            'input': 2,
            'output': [0,1,3,2],
        },
        {
            'input': 1,
            'output': [0,1],
        },
        {
            'input': 3,
            'output': [0,1,3,2,6,7,5,4],
        },
        # {
        #     'input': 10,
        #     'output': [0,1,3,2,6,7,5,4],
        # },
    ]
    solution = Solution()

    for param in params:
        n = param['input']
        result = solution.grayCode(n)
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
