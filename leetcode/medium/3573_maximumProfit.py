import json
from collections import defaultdict, deque
from typing import List
# from functools import cache


class Solution_0:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        N = len(prices)

        def dfs(id, status, operations, money):
            if id == N:
                if status == 'loan':
                    return float('-inf')
                return money

            if status == 'empty':
                if operations == k:
                    return money

                r1 = dfs(id + 1, status, operations, money)
                r2 = dfs(id + 1, 'hold', operations + 1, money - prices[id])
                r3 = dfs(id + 1, 'loan', operations + 1, money + prices[id])

                return max(r1, r2, r3)

            if status == 'hold':
                r1 = dfs(id + 1, status, operations, money)
                r2 = dfs(id + 1, 'empty', operations, money + prices[id])

                return max(r1, r2)

            if status == 'loan':
                r1 = dfs(id + 1, status, operations, money)
                r2 = dfs(id + 1, 'empty', operations, money - prices[id])

                return max(r1, r2)


            return 0

        return dfs(0, 'empty', 0, 0)


class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        N = len(prices)

        cntOfOps = N // 2 +2
        memo = []
        # empty, hold, loan
        for i in range(3):
            row = []
            for j in range(N):
                row.append([None] * cntOfOps)
            memo.append(row)

        def dfs(id, status, operations):
            if id == N:
                if status == 2:
                    return float('-inf')
                return 0

            if memo[status][id][operations] != None:
                return memo[status][id][operations]

            if status == 0:
                if operations == k:
                    return 0

                r1 = dfs(id + 1, status, operations)

                r2 = -prices[id]
                r2 += dfs(id + 1, 1, operations + 1)

                r3 = prices[id]
                r3 += dfs(id + 1, 2, operations + 1)

                memo[status][id][operations] = max(r1, r2, r3)

            elif status == 1:
                r1 = dfs(id + 1, status, operations)

                r2 = prices[id]
                r2 += dfs(id + 1, 0, operations)
                memo[status][id][operations] = max(r1, r2)

            elif status == 2:
                r1 = dfs(id + 1, status, operations)

                r2 = -prices[id]
                r2 += dfs(id + 1, 0, operations)
                memo[status][id][operations] = max(r1, r2)

            return memo[status][id][operations]

        return dfs(0, 0, 0)


'''

empty
hold
loan

[[12,16,19,19,8,1,19,13,9], 3],

12-19=7
19-8 = 11
1-19 = 18
36


'''


def test():
    params = [
        {
            "input": [[1,7,9,8,2], 2],
            "output": 14,
        },
        {
            "input": [[12,16,19,19,8,1,19,13,9], 3],
            "output": 36,
        },
        {
            "input": [
                [439905949,666304906,328728050,996405752,379313886,528209791,88582883,939135548,751069794,109146128,883868801,685035870,872864534,515610456,671402135,299270187,782796059,14959721,863144680,901085624,622229387,536656476,257303050,868839354,117275933,918430202,935695732,478547107,484151756,631419928,39696098,650941214,51074234,941181946,265314584,557086091,786537782,50596574,28828693,157162091,9857934,451956750,695591748,879988702,249629554,539569656,282083076,39183395,66614080,479066152,652564309,907349719,210005879,768785742,537258749,237393978,346271286,392541722,312074103,126562356,400828204,614474102,364762040,8363356,539354781,90084496,319405489,644955686,889207045,798527610,141688158,529097227,598399178,87898767,830035760,49071715,600386530,40425784,322514114,778707680,79388396],
                30
            ],
            "output": 17891684807,
        },
    ]
    solution = Solution()

    for param in params:
        prices, k = param["input"]
        result = solution.maximumProfit(prices, k)
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
