import json
from collections import defaultdict, deque
from typing import List


budget = 5
total = [0]*(budget+1)
child = [budget-i for i in range(budget+1)]
# for bud in range(budget, -1, -1):
for bud in range(budget+1):
    for left in range(bud + 1):
        right = bud - left
        total[bud] = max(total[bud], total[left] + child[right])

print('total', total)

'''

why `for b in range(budget, -1, -1):` is working but `for b in range(budget+1):` is not working?

0 5
1 4
2 3
3 2
4 1
5 0
0 4
1 3
2 2
3 1
4 0
0 3
1 2
2 1
3 0
0 2
1 1
2 0
0 1
1 0
0 0

---

0 0
0 1
1 0
0 2
1 1
2 0
0 3
1 2
2 1
3 0
0 4
1 3
2 2
3 1
4 0
0 5
1 4
2 3
3 2
4 1
5 0


'''

class Solution:
    def maxProfit(self, n, present, future, hierarchy, budget):
        adj = [[] for i in range(n+1)]
        for boss, worker in hierarchy:
            adj[boss].append(worker)

        def dfs(id):
            memoBare = [0] * (budget+1)
            memoSale = [0] * (budget+1)

            priceBare = present[id-1]
            priceSale = priceBare // 2

            profitBare = future[id-1] - priceBare
            profitSale = future[id-1] - priceSale

            childBare = [0] * (budget+1)
            childSale = [0] * (budget+1)

            for nei in adj[id]:
                _chBare, _chSale = dfs(nei)
                for bud in range(budget, -1, -1):
                    for left in range(bud + 1):
                        right = bud - left
                        childBare[bud] = max(childBare[bud], childBare[left] + _chBare[right])
                        childSale[bud] = max(childSale[bud], childSale[left] + _chSale[right])

            for bud in range(budget + 1):
                # bare
                memoBare[bud] = childBare[bud]
                remainder = bud - priceBare
                if remainder >= 0:
                    memoBare[bud] = max(memoBare[bud], childSale[remainder] + profitBare)
                # sale
                memoSale[bud] = childBare[bud]
                remainder = bud - priceSale
                if remainder >= 0:
                    memoSale[bud] = max(memoSale[bud], childSale[remainder] + profitSale)

            return memoBare, memoSale

        resBare, resSale = dfs(1)

        return max(resBare)

'''
[3, [4,6,8], [7,9,11], [[1,2],[1,3]], 10]

4
3-9; 4-11;

0
6-9; 8-11;

---

    1
  2   3
4 5   6 7



'''


def test():
    params = [
        {
            "input": [2, [1,2], [4,3], [[1,2]], 3],
            "output": 5,
        },
        {
            "input": [2, [3,4], [5,8], [[1,2]], 4],
            "output": 4,
        },
        {
            "input": [3, [4,6,8], [7,9,11], [[1,2],[1,3]], 10],
            "output": 10,
        },
        {
            "input": [3, [5,2,3], [8,5,6], [[1,2],[2,3]], 7],
            "output": 12,
        },
        {
            "input": [
                3,
                [6,4,23],
                [50,48,17],
                [[1,3],[1,2]],
                28,
            ],
            "output": 96,
        },
    ]
    solution = Solution()

    for param in params:
        n, present, future, hierarchy, budget = param["input"]
        result = solution.maxProfit(n, present, future, hierarchy, budget)
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
