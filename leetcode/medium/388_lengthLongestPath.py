from typing import List
import heapq
import math
from collections import defaultdict, deque


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        N = len(input)
        res = 0
        stack = []
        id = 0
        name = ''
        level = 0

        while id < N:
            if input[id] != '\n':
                name += input[id]
                id += 1
                continue

            while level < len(stack):
                stack.pop()

            stack.append(name)
            name = ''
            if '.' in stack[-1]:
                r = '/'.join(stack)
                res = max(res, len(r))

            if input[id] == '\n':
                id += 1
                level = 0

                while id < N and input[id] == '\t':
                    id += 1
                    level += 1

        if name:
            while level < len(stack):
                stack.pop()

            stack.append(name)
            name = ''
            if '.' in stack[-1]:
                r = '/'.join(stack)
                res = max(res, len(r))


        return res

'''
dir
    \n\tsubdir1
    \n\tsubdir2
        \n\t\tfile.ext

"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"

dir
    \n\tsubdir1
        \n\t\tfile1.ext
        \n\t\tsubsubdir1
    \n\tsubdir2
        \n\t\tsubsubdir2
            \n\t\t\tfile2.ext

'''

def test ():
    params = [
        {
            'input': "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext",
            'output': 20,
        },
        {
            'input': "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext",
            'output': 32,
        },
        {
            'input': "a",
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        input = param['input']
        result = solution.lengthLongestPath(input)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            # 'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
