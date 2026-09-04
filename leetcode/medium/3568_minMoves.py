import json
from collections import deque
from functools import cache
from typing import List

"""
20*20*50 = 20_000

'S': Starting position of the student
'L': Litter that must be collected (once collected, the cell becomes empty)
'R': Reset area that restores the student's energy to full capacity, regardless of their current energy level (can be used multiple times)
'X': Obstacle the student cannot pass through
'.': Empty space


3568. Minimum Moves to Clean the Classroom




"L.S",
"RXL"
3

"L.L",
"LXS"
3

I understand, it can be only 10 litter cells. And I have changed a cache. But solution still very slow.

"""


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        N = len(classroom)
        M = len(classroom[0])
        shifts = ((1, 0), (-1, 0), (0, 1), (0, -1))

        littByLoc = {}
        littCnt = 0
        finalMask = 0

        start = None
        for r in range(N):
            for c in range(M):
                if classroom[r][c] == "S":
                    start = [r, c]
                elif classroom[r][c] == "L":
                    littCnt += 1
                    littByLoc[(r, c)] = littCnt
                    finalMask = finalMask | (1 << littCnt)

        if finalMask == 0:
            return 0

        # print("start", start, "finalMask", finalMask)

        stepsQueue = deque()
        stepsQueue.append((start[0], start[1], 0, energy, 0))
        memo = {}
        memo[f"{start[0]}_{start[1]}_{0}"] = energy

        while stepsQueue:
            row, col, mask, enrg, step = stepsQueue.popleft()

            # print(row, col, classroom[row][col], mask)

            if classroom[row][col] == "L":
                id = littByLoc[(row, col)]
                mask = mask | (1 << id)
            if mask == finalMask:
                return step

            if classroom[row][col] == "R":
                enrg = energy

            if enrg == 0:
                continue

            for sR, sC in shifts:
                newR = row + sR
                newC = col + sC

                # print("newR", newR, "newC", newC)

                if (
                    newR == N
                    or newR == -1
                    or newC == M
                    or newC == -1
                    or classroom[newR][newC] == "X"
                ):
                    continue

                # key = (newR, newC, _enrg, _mask)
                key = f"{newR}_{newC}_{mask}"
                if key in memo and memo[key] >= enrg - 1:
                    continue

                memo[key] = enrg - 1
                stepsQueue.append((newR, newC, mask, enrg - 1, step + 1))

        return -1


def test():
    params = [
        {
            "input": [["S.", "XL"], 2],
            "output": 2,
        },
        {
            "input": [["LS", "RL"], 4],
            "output": 3,
        },
        {
            "input": [["L.S", "RXL"], 3],
            "output": -1,
        },
        {
            "input": [["SR"], 1],
            "output": 0,
        },
        {
            "input": [["LSR"], 2],
            "output": 1,
        },
        {
            "input": [["L.L", "LXS"], 3],
            "output": -1,
        },
        {
            "input": [
                [
                    "XL..XLLL.XR.",
                    "XXLRXXLXRXXL",
                    "LLX.LRXRRX.S",
                    "XRX.XRX....R",
                    ".X.RR.X.RX..",
                    "RR.R.RRR.X.R",
                    "XX.XXXXX...X",
                    "XRRXXXX...R.",
                    ".R.X.RX.XR.X",
                    "XRX..XXXRX.X",
                    "X..XR.XR.XX.",
                    "R...XX.R..RX",
                    ".X.XRX..XR..",
                ],
                44,
            ],
            "output": -1,
        },
        {
            "input": [
                [
                    "S...................",
                    "....................",
                    "....................",
                    "....................",
                    ".....RL........RR...",
                    "....................",
                    "......L....R..L.....",
                    ".....L..............",
                    ".........L........LL",
                    "....................",
                    "....................",
                    "....................",
                    "........L...........",
                    "....................",
                    "....................",
                    "....................",
                    "....L...............",
                    "....................",
                    ".....R..............",
                    "..............L.....",
                ],
                20,
            ],
            "output": 71,
        },
    ]
    solution = Solution()

    for param in params:
        classroom, energy = param["input"]
        result = solution.minMoves(classroom, energy)
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
