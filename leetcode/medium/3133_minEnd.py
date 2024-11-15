from typing import List
from json import dumps
import heapq


'''

4 = 100
5 iteration
00100
00101
00110
00111
01100

changes in zeros:
001
010
011
100

final result of combinations equal to n-1
if we know this trick, we can put bits from n-1 into zeros place

'''

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        print('x', bin(x))


        combArr = list(bin(n-1)[2:])
        xArr = list(bin(x)[2:])
        rem = ['0']*(64 - len(xArr))
        xArr = rem + xArr

        print(
            'combArr', combArr,
            'xArr', xArr,

        )

        id = 63
        for i in range(len(combArr) - 1, -1, -1):
            while xArr[id] != '0':
                id -= 1
            xArr[id] = combArr[i]
            id -= 1

        res = int('0b'+''.join(xArr), 2)
        print('xArr', '0b'+''.join(xArr))
        print('xArr', int('0b'+''.join(xArr), 2))

        return res


def test ():
    params = [
        {
            'input': [3, 4],
            'output': 6,
        },
        {
            'input': [2, 7],
            'output': 15,
        },
        {
            'input': [5, 4],
            'output': 12,
        },
        {
            'input': [6715154, 7193485],
            'output': 55012476815,
        },  
    ]
    solution = Solution()

    for param in params:
        n, x = param['input']
        result = solution.minEnd(n, x)
        print(
            'SUCCESS' if dumps(result) == dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
