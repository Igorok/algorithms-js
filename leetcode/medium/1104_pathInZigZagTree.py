from typing import List
from json import dumps
from collections import defaultdict, deque
import heapq


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        if label == 1:
            return [1]

        tree = [
            [1],
        ]
        id = -1
        while id == -1:
            tree.append([])
            height = len(tree)
            length = 2 ** (height - 1)
            num = 2 ** (height - 1)

            for i in range(length):
                val = num + i
                if val == label:
                    id = i
                tree[height-1].append(val)

            if (height % 2) == 0:
                tree[height-1].reverse()
                if id != -1:
                    id = len(tree[height-1]) - id - 1

        res = []

        for i in range(len(tree)-1, -1, -1):
            res.append(tree[i][id])
            id = id // 2

        res.reverse()

        return res


def test ():
    params = [
        {
            'input': 14,
            'output': [1,3,4,14],
        },
        {
            'input': 26,
            'output': [1,2,6,10,26],
        },
    ]
    solution = Solution()

    for param in params:
        label = param['input']
        result = solution.pathInZigZagTree(label)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

if __name__ == '__main__':
    test()
