from typing import List
from json import dumps
from collections import deque

class Solution:
    def maxChunksToSorted(self, arr):
        n = len(arr)
        # Deque to store the maximum elements of each chunk
        stack = deque()

        for i in range(n):
            # Case 1: Current element is larger, starts a new chunk
            if not stack or arr[i] > stack[-1]:
                stack.append(arr[i])
            else:
                # Case 2: Merge chunks
                max_element = stack[-1]
                while stack and arr[i] < stack[-1]:
                    stack.pop()
                stack.append(max_element)

        return len(stack)


def test ():
    params = [
        {
            'input': [4, 3, 1, 2,],
            'output': 1,
        },
        {
            'input': [4, 3, 1, 2, 5, 6, 7, 1, 2, 5, 8, 9],
            'output': 3,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.maxChunksToSorted(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
