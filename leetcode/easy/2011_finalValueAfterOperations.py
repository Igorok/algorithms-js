from typing import List
from json import dumps

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for v in operations:
            if v in ('--X', 'X--'):
                x -= 1
            else:
                x += 1
        return x


def test ():
    params = [
        {
            'input': ["--X","X++","X++"],
            'output': 1,
        },
        {
            'input': ["++X","++X","X++"],
            'output': 3,
        },
        {
            'input': ["X++","++X","--X","X--"],
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.finalValueAfterOperations(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
