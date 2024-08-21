from typing import List

class Solution:
    def strangePrinter(self, s: str) -> int:
        letters = set(s)
        return len(letters)



def test ():
    params = [
        {
            'input': 'aaaaabbbb',
            'output': 2,
        },
        {
            'input': 'aba',
            'output': 2,
        },
        {
            'input': 'abcabc',
            'output': 5,
        },
        {
            'input': 'aabaaabaa',
            'output': 3,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.strangePrinter(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

'''
[1,2,3,4,   5,6,7,8,9]
'''


if __name__ == '__main__':
    test()
