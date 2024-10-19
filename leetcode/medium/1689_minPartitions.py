from typing import List
from json import dumps

class Solution:
    def minPartitions(self, n: str) -> int:
        res = 0
        while n != '':
            upd = ''
            for char in n:
                num = int(char)
                if num != 0:
                    num -= 1
                if num == 0 and upd == '':
                    continue
                else:
                    upd += str(num)
            n = upd
            res += 1

        return res

def test ():
    params = [
        {
            'input': "320", # 110 + 110 + 100
            'output': 3,
        },
        {
            'input': "32",
            'output': 3,
        },
        {
            'input': "82734",
            'output': 8,
        },
        {
            'input': "27346209830709182346",
            'output': 9,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.minPartitions(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
