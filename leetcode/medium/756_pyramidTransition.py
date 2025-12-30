import json
from collections import defaultdict, deque
from typing import List
# from functools import cache


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        n = len(bottom)
        left = {}
        for text in allowed:
            x = text[0]
            y = text[1]
            z = text[2]

            if x not in left:
                left[x] = {}

            if y not in left[x]:
                left[x][y] = []

            left[x][y].append(z)

        piramid = []
        piramid.append(list(bottom))
        for i in range(n-1, 0, -1):
            piramid.append([None] * i)


        # print(
        #     'left', left,
        #     'piramid', piramid,
        # )

        cache = {}

        def dfs(row, col):
            if row == n-1:
                return True

            text = ''.join(piramid[row])
            if col > 0:
                text += ''.join(piramid[row+1][:col])
            key = f'{row}_{col}_{text}'

            # print('key', key)

            if key in cache:
                return cache[key]


            l = piramid[row][col]
            if l not in left:
                return False

            r = piramid[row][col+1]
            if r not in left[l]:
                return False

            res = False
            for t in left[l][r]:
                piramid[row+1][col] = t
                nextRow = row
                nextCol = col + 1

                if nextCol == len(piramid[row]) - 1:
                    nextRow = row + 1
                    nextCol = 0

                if dfs(nextRow, nextCol):
                    res = True
                    break

                piramid[row+1][col] = None

            cache[key] = res
            return res

        return dfs(0, 0)


def test():
    params = [
        {
            "input": ["BCD", ["BCC","CDE","CEA","FFF"]],
            "output": True,
        },
        {
            "input": ["AAAA", ["AAB","AAC","BCD","BBE","DEF"]],
            "output": False,
        },
        {
            "input": ["ABCD", ["ABC","BCA","CDA","ABD","BCE","CDF","DEA","EFF","AFF"]],
            "output": True,
        },
    ]
    solution = Solution()

    for param in params:
        bottom, allowed = param["input"]
        result = solution.pyramidTransition(bottom, allowed)
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
