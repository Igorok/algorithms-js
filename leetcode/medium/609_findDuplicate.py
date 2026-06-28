import heapq
import math
from collections import Counter, defaultdict
from functools import cache
from json import dumps
from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content = defaultdict(list)

        for path in paths:
            data = path.split(" ")
            if len(data) == 0:
                continue

            p = data[0] + "/"
            data = data[1:]

            for val in data:
                start = val.find("(")
                n = val[0:start]
                v = val[start + 1 : len(val) - 1]
                content[v].append(p + n)

        # print(content)

        res = []

        for data in content.values():
            if len(data) > 1:
                res.append(data)

        return res


def test():
    params = [
        {
            "input": [
                "root/a 1.txt(abcd) 2.txt(efgh)",
                "root/c 3.txt(abcd)",
                "root/c/d 4.txt(efgh)",
                "root 4.txt(efgh)",
            ],
            "output": [
                ["root/a/2.txt", "root/c/d/4.txt", "root/4.txt"],
                ["root/a/1.txt", "root/c/3.txt"],
            ],
        },
        {
            "input": [
                "root/a 1.txt(abcd) 2.txt(efgh)",
                "root/c 3.txt(abcd)",
                "root/c/d 4.txt(efgh)",
            ],
            "output": [
                ["root/a/2.txt", "root/c/d/4.txt"],
                ["root/a/1.txt", "root/c/3.txt"],
            ],
        },
    ]
    solution = Solution()

    for param in params:
        paths = param["input"]
        result = solution.findDuplicate(paths)
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
