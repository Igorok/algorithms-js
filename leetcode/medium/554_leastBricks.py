import json
from collections import defaultdict, deque
from typing import List


class Solution_0:
    def leastBricks(self, wall: List[List[int]]) -> int:
        height = len(wall)
        width = sum(wall[0])

        edges = [0]*(width + 1)

        for row in range(height):
            border = 0
            for brick in wall[row]:
                border += brick
                edges[border] += 1

        res = height
        for col in range(1, width):
            crossed = edges[col]
            res = min(res, height - crossed)

        return res


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        height = len(wall)
        width = sum(wall[0])

        edges = {}

        for row in range(height):
            border = 0
            for brick in wall[row]:
                border += brick
                edges[border] = edges.get(border, 0) + 1

        res = height
        for edge in edges:
            if edge == width:
                continue
            crossed = edges[edge]
            res = min(res, height - crossed)

        return res

'''
[
[1,1],
[2],
[1,1]
]

1,1
2 2
1,1

'''

def test():
    params = [
        {
            "input": [
                [1, 2, 2, 1],
                [3, 1, 2],
                [1, 3, 2],
                [2, 4],
                [3, 1, 2],
                [1, 3, 1, 1],
            ],
            "output": 2,
        },
        {
            "input": [[1], [1], [1]],
            "output": 3,
        },
        {
            "input": [[1,1],[2],[1,1]],
            "output": 1,
        },
    ]
    solution = Solution()

    for param in params:
        wall = param["input"]
        result = solution.leastBricks(wall)
        correct = json.dumps(result) == json.dumps(param["output"])

        msg = "SUCCESS" if correct else "ERROR"
        msg += "\n"
        if not correct:
            msg += "input " + json.dumps(param["input"]) + "\n"
            msg += "output " + json.dumps(param["output"]) + "\n"
            msg += "result " + json.dumps(result) + "\n"

        print(msg)


if __name__ == "__main__":
    test()
