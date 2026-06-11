import heapq
from collections import Counter, defaultdict
from functools import cache
from json import dumps
from typing import List


class Solution:
    def getSortedHand(self, hand):
        hand = sorted(Counter(hand).items())
        res = ""
        for char, cnt in hand:
            res += char * cnt
        return res

    def checkBoard(self, s):
        N = len(s)

        for i in range(0, N, 2):
            char = s[i]
            cnt = int(s[i + 1])

            if cnt > 2:
                return self.checkBoard(s[:i] + s[i + 2 :])

            if i > 0 and s[i - 2] == s[i]:
                cnt += int(s[i - 1])

                newS = s[: i - 2] + char + str(cnt) + s[i + 2 :]
                if cnt > 2:
                    newS = s[: i - 2] + s[i + 2 :]

                return self.checkBoard(newS)

        return s

    def findMinStep(self, board: str, hand: str) -> int:
        visited = set()
        memo = {}

        def rec(board: str, hand: str):
            if len(board) == 0:
                return 0

            if len(board) > 0 and len(hand) == 0:
                return float("inf")

            memoKey = board + "_" + hand
            if memoKey in memo:
                return memo[memoKey]

            if memoKey in visited and memoKey not in memo:
                return float("inf")

            visited.add(memoKey)

            withCount = ""
            prev = 0
            N = len(board)
            for i in range(N):
                if board[i] != board[prev]:
                    withCount += board[prev] + str(i - prev)
                    prev = i

                if i == N - 1:
                    withCount += board[prev] + str(N - prev)

            res = float("inf")

            handObj = Counter(hand)
            for key in handObj:
                h = handObj.copy()
                h[key] -= 1
                if h[key] == 0:
                    del h[key]

                newHand = ""
                for char, cnt in sorted(h.items()):
                    newHand += char * cnt

                M = len(withCount)
                for id in range(0, M, 2):
                    char = withCount[id]
                    cnt = withCount[id + 1]

                    if char != key:
                        continue

                    cnt = int(cnt) + 1
                    checkedBoard = (
                        (withCount[:id] + withCount[id + 2 :])
                        if cnt > 2
                        else (withCount[:id] + char + str(cnt) + withCount[id + 2 :])
                    )
                    checkedBoard = self.checkBoard(checkedBoard)
                    newBoard = ""
                    for i in range(0, len(checkedBoard), 2):
                        char = checkedBoard[i]
                        cnt = int(checkedBoard[i + 1])
                        newBoard += char * cnt
                    r = rec(newBoard, newHand)

                    res = min(res, r + 1)

            memo[memoKey] = res

            return res

        res = rec(board, hand)

        return -1 if res == float("inf") else res


def test():
    params = [
        {
            "input": ["WRRBBW", "RB"],
            "output": -1,
        },
        {
            "input": ["WWRRBBWW", "WRBRW"],
            "output": 2,
        },
        {
            "input": ["G", "GGGGG"],
            "output": 2,
        },
        # RRWWRRBBRR -> RRWWRRBBR[W]R -> RRWWRRBB[B]RWR -> RRWWRRRWR -> RRWWWR -> RRR -> empty
        {
            "input": ["RRWWRRBBRR", "WB"],
            "output": 2,
        },
    ]
    solution = Solution()

    for param in params:
        board, hand = param["input"]
        result = solution.findMinStep(board, hand)
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
