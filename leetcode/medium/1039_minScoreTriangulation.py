from multiprocessing import Value
from typing import List
import math


class Solution_0:
    def minScoreTriangulation(self, values: List[int]) -> int:
        cache = {}

        def dfs(values) -> int:
            # print("values", values)
            values.sort(key=lambda x: x[1])

            key = "_".join(str(v[1]) for v in values)
            if key in cache:
                print(key)
                return cache[key]

            n = len(values)
            if n == 3:
                cache[key] = values[0][0] * values[1][0] * values[2][0]
                return cache[key]

            res = float("inf")
            limit = math.ceil(n / 2)

            for i in range(limit):
                for j in range(i + 2, n):
                    if i == 0 and j == n - 1:
                        continue
                    r1 = dfs(values[i : j + 1])
                    r2 = dfs(values[j:n] + values[0 : i + 1])

                    res = min(res, r1 + r2)

            cache[key] = res
            return cache[key]

        data = [(values[i], i) for i in range(len(values))]
        return dfs(data)


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        cache = {}

        def dfs(start, end):
            if (start, end) in cache:
                return cache[(start, end)]

            res = float("inf")

            for middle in range(start + 1, end):
                r0 = values[start] * values[middle] * values[end]
                r1 = dfs(start, middle) if middle - start > 1 else 0
                r2 = dfs(middle, end) if end - middle > 1 else 0

                res = min(res, r0 + r1 + r2)

            cache[(start, end)] = res
            return res

        return dfs(0, n - 1)


"""
count = n-2
----b
a---------c
---e---d


---2
4 ---1
--4


"""


def test():
    params = [
        {
            "input": [2, 1, 4, 4],
            "output": 24,
        },
        {
            "input": [1, 2, 3],
            "output": 6,
        },
        {
            "input": [3, 7, 4, 5],
            "output": 144,
        },
        {
            "input": [1, 3, 1, 4, 1, 5],
            "output": 13,
        },
        {
            "input": [
                69,
                22,
                21,
                27,
                26,
                62,
                69,
                81,
                55,
                85,
                95,
                40,
                91,
                33,
                72,
                88,
                86,
            ],
            "output": 1334781,
        },
    ]
    solution = Solution()

    for param in params:
        values = param["input"]
        result = solution.minScoreTriangulation(values)

        print(
            "SUCCESS" if result == param["output"] else "ERROR",
            "input",
            param["input"],
            "output",
            param["output"],
            "result",
            result,
            "\n",
        )


if __name__ == "__main__":
    test()
