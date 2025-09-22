from typing import List
from json import dumps
from collections import deque

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []

        n = len(s)
        def dfs(id, acc):
            if id == n:
                res.append(''.join(acc))
                return

            if s[id].isdigit():
                acc.append(s[id])
                dfs(id+1, acc)
                acc.pop()
                return

            acc.append(s[id].lower())
            dfs(id+1, acc)
            acc.pop()

            acc.append(s[id].upper())
            dfs(id+1, acc)
            acc.pop()

        dfs(0, [])

        return res


def test ():
    params = [
        {
            'input': 'a1b2',
            'output': ["a1b2","a1B2","A1b2","A1B2"],
        },
        {
            'input': '3z4',
            'output': ["3z4","3Z4"],
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.letterCasePermutation(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
