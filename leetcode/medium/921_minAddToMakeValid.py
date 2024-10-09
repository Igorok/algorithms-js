from typing import List

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openned = 0
        closed = 0
        for char in s:
            if char == '(':
                openned += 1
            else:
                if openned == 0:
                    closed += 1
                else:
                    openned -= 1

        return closed + openned


def test ():
    params = [
        {
            'input': "())",
            'output': 1,
        },
        {
            'input': "(((",
            'output': 3,
        },
        {
            'input': "(()())",
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.minAddToMakeValid(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

if __name__ == '__main__':
    test()
