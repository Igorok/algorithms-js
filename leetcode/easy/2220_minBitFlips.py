from typing import List

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res = 0
        if start == goal: return 0

        while start != 0 or goal != 0:
            rs = start % 2
            rg = goal % 2

            start = start // 2
            goal = goal // 2

            if rs != rg:
                res += 1

        return res


def test ():
    params = [
        {
            'input': [10, 7],
            'output': 3,
        },
        {

            'input': [3, 4],
            'output': 3,
        },
        {

            'input': [10, 82],
            'output': 3,
        }
    ]
    solution = Solution()

    for param in params:
        start, goal = param['input']
        result = solution.minBitFlips(start, goal)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
