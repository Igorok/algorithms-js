import json
from collections import defaultdict, deque
from typing import List
# from functools import cache
import math


class Solution_0:
    def separateSquares(self, squares: List[List[int]]) -> float:
        squares.sort(key = lambda x: x[1])

        totalArea = 0
        bottomY = squares[0][1]
        topY = -1
        for x, y, l in squares:
            totalArea += l**2
            topY = max(topY, y+l)

        target = round(totalArea / 2, 5)
        target = totalArea / 2

        def getArea(line):
            area = 0
            for x, y, l in squares:
                bottom = max(0, min(line, y+l) - y)
                area += bottom * l
            return round(area, 5)


        bottom = 0
        top = 100
        res = 0
        while bottom <= top:
            percent = (top + bottom) // 2
            line = bottomY + (topY - bottomY) * percent / 100
            area = getArea(line)

            print(
                'percent', percent,
                'line', line,
                'area', area,
                'target', target,
            )

            if area == target:
                res = line
                top = percent - 1
            elif area > target:
                top = percent - 1
            else:
                bottom = percent + 1


        return res


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        squares.sort(key = lambda x: x[1])

        totalArea = 0
        bottomY = squares[0][1]
        topY = -1
        for x, y, l in squares:
            totalArea += l**2
            topY = max(topY, y+l)

        target = totalArea / 2

        def getArea(line):
            area = 0
            for x, y, l in squares:
                bottom = max(0, min(line, y+l) - y)
                area += bottom * l
            return area


        top = topY
        bottom = bottomY
        for i in range(100):
            line = (top + bottom) / 2
            area = getArea(line)

            print(
                'line', line,
                'area', area,
                'target', target,
            )

            if area >= target:
                top = line
            else:
                bottom = line


        return bottom



def test():
    params = [
        # {
        #     "input": [[0,0,1],[2,2,1]],
        #     "output": 1.00000,
        # },
        # {
        #     "input": [[0,0,2],[1,1,1]],
        #     "output": 1.16667,
        # },
        {
            "input": [[23,29,3],[28,29,4]],
            "output": 30.78571,
        },
    ]
    solution = Solution()

    for param in params:
        squares = param["input"]
        result = solution.separateSquares(squares)
        correct = json.dumps(result) == json.dumps(param["output"])

        msg = "SUCCESS" if correct else "ERROR"
        msg += "\n"
        if not correct:
            # msg += "input " + json.dumps(param["input"]) + "\n"
            msg += "output " + json.dumps(param["output"]) + "\n"
            msg += "result " + json.dumps(result) + "\n"

        print(msg)


if __name__ == "__main__":
    test()
