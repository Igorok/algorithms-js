from typing import List
from json import dumps


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        def noCollision(a, b):
            return (a > 0 and b > 0) or (a < 0 and b < 0) or (a < 0 and b > 0)

        for ast in asteroids:
            if len(stack) == 0 or noCollision(stack[-1], ast):
                stack.append(ast)
                continue

            while len(stack) > 0 and not noCollision(stack[-1], ast):
                if abs(stack[-1]) == abs(ast):
                    stack.pop()
                    break
                if abs(stack[-1]) < abs(ast):
                    stack.pop()
                    if len(stack) == 0 or noCollision(stack[-1], ast):
                        stack.append(ast)
                        break
                if abs(stack[-1]) > abs(ast):
                    break

        return stack


def test ():
    params = [
        {
            'input': [5,10,-5],
            'output': [5,10],
        },
        {
            'input': [8,-8],
            'output': [],
        },
        {
            'input': [10,2,-5],
            'output': [10],
        },
        {
            'input': [-2,-1,1,2],
            'output': [-2,-1,1,2],
        },
        {
            'input': [-2,-2,1,-2],
            'output': [-2,-2,-2],
        },

    ]
    solution = Solution()

    for param in params:
        result = solution.asteroidCollision(param['input'])
        print(
            'SUCCESS' if dumps(result) == dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
