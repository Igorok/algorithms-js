from typing import List
from json import dumps

class Solution_0:
    def findKthBit_1(self, n: int, k: int) -> str:
        res = '0'
        for i in range(1, n):
            part = ''
            for char in res:
                c = '1' if char == '0' else '0'
                part = c + part
            res += '1' + part

        return res[k - 1]

    def findKthBit(self, n: int, k: int) -> str:
        length = 2**n - 1

        def rec(length, k):
            if length == 1:
                return '0'

            middle = 1 + length // 2
            if k == middle:
                return '1'
            elif k < middle:
                return rec(middle - 1, k)
            else:
                id = length - k + 1
                res = rec(middle - 1, id)
                return '1' if res == '0' else '0'

        return rec(length, k)


class Solution_0:
    def findKthBit(self, n: int, k: int) -> str:
        text = '0'
        def reverse(text):
            text = list(text)
            text.reverse()
            return ''.join(text)

        def invert(text):
            res = ['0'] * len(text)
            for i in range(len(text)):
                res[i] = '0' if text[i] == '1' else '1'
            return res

        for i in range(n):
            text = text + '1' + reverse(invert(text))
            if len(text) > k:
                break

        print(text)

        return text[k-1]


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        text = '0'
        def reverse(text):
            text = list(text)
            text.reverse()
            return ''.join(text)

        def invert(text):
            res = ['0'] * len(text)
            for i in range(len(text)):
                res[i] = '0' if text[i] == '1' else '1'
            return res

        for i in range(n):
            text = text + '1' + reverse(invert(text))
            if len(text) > k:
                break

        print(text)

        return text[k-1]


'''
0111001
011100110110001
'''

def test ():
    params = [
        {
            'input': [3, 1],
            'output': '0',
        },
        {
            'input': [4, 11],
            'output': '1',
        },
        {
            'input': [20, 1000000],
            'output': '1',
        },
    ]
    solution = Solution()

    for param in params:
        n, k = param['input']
        result = solution.findKthBit(n, k)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
