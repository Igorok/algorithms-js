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
        stack = []

        N = len(s)
        for i in range(N):
            if not len(stack):
                stack = [[s[i], 1]]
                continue

            if len(stack) and stack[-1][0] == s[i]:
                stack[-1][1] += 1
                continue

            if len(stack) and stack[-1][0] != s[i]:
                while len(stack) and stack[-1][1] > 2:
                    stack.pop()

                if len(stack) and stack[-1][0] == s[i]:
                    stack[-1][1] += 1
                else:
                    stack.append([s[i], 1])

        while len(stack) and stack[-1][1] > 2:
            stack.pop()

        res = ""
        for char, cnt in stack:
            res += char * cnt

        return res

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

            res = float("inf")

            N = len(board)
            handObj = Counter(hand)

            for handChar in handObj:
                h = handObj.copy()
                h[handChar] -= 1
                if h[handChar] == 0:
                    del h[handChar]

                newHand = ""
                for char, cnt in sorted(h.items()):
                    newHand += char * cnt

                for id in range(N):
                    # 1
                    cond1 = id > 0 and board[id-1] == handChar
                    # 2
                    cond2 = (id == 0 or board[id-1] != handChar) and board[id] == handChar
                    # 3
                    cond3 = id > 0 and board[id-1] == board[id] and board[id] != handChar 
                    
                    newBoard = board[:id] + handChar + board[id:]
                    newBoard = self.checkBoard(newBoard)

                    if (cond1 or cond2 or cond3) and newBoard + '_' + newHand not in visited:
                        r = rec(newBoard, newHand)
                        res = min(res, r + 1)

            memo[memoKey] = res

            return res

        hand = self.getSortedHand(hand)
        res = rec(board, hand)

        return -1 if res == float("inf") else res
  

'''

so brute forse insertion for every board position is not working here.
There is some tricky rules for insertion.
Can you explain it?


                        
["RRGGBBYYWWRRGGBB", "RGBYW"]
"RRGGBBYYWWRRGGBB", "RGBYW"
"RR GG BB YY WW RR GG BB", "RGBYW"


RRGGBBRRGGBB
RGB

["RRWWRRBBRR", "WB"]

"RR WW RR BB RR", "WB"
"R B R WW RR BB RR", "W"
"R B R WWW RR BB RR", ""
"R B RRR BB RR", ""
"R BBB RR", ""
"RRR", ""
"", ""



Do you know leetcode issue "488. Zuma Game"?
How it possible to get 2 from ["RRWWRRBBRR", "WB"]?

'''

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
        {
            "input": ["RRWWRRBBRR", "WB"],
            "output": 2,
        },
        {
            "input": ["RRGGBBYYWWRRGGBB", "RGBYW"],
            "output": -1,
        },
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
