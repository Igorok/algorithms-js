from typing import List
import json
from collections import deque, defaultdict
from functools import lru_cache
import math

class Solution_0:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        prices.sort()

        @lru_cache(None)
        def dfs(r1: int, c1: int, r2: int, c2: int) -> int:
            if r1 >= r2 or c1 >= c2:
                return 0

            res = 0

            for h, w, p in prices:
                if h > r2 - r1 or w > c2 - c1:
                    continue

                # 1
                res1 = p
                res1 += dfs(r1, c1+w, r1+h, c2)
                res1 += dfs(r1+h, c1, r2, c2)

                # 2
                res2 = p
                res2 += dfs(r1, c1+w, r2, c2)
                res2 += dfs(r1+h, c1, r2, c1+w)

                res = max(res, res1, res2)

            return res

        return dfs(0, 0, m, n)

class Solution_1:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        prices.sort()

        heights = []
        heightsAndWidths = {}
        for h, w, p in prices:
            heightsAndWidths[h] = heightsAndWidths.get(h, [])

            if heightsAndWidths[h] and heightsAndWidths[h][-1][0] == w:
                heightsAndWidths[h][-1][1] = max(heightsAndWidths[h][-1][1], p)
            elif heightsAndWidths[h] and heightsAndWidths[h][-1][1] >= p:
                continue
            else:
                heightsAndWidths[h].append([w, p])

            if not heights or heights[-1] != h:
                heights.append(h)

            if heightsAndWidths[h] and len(heights) > 2:
                prev = heightsAndWidths[heights[-2]]
                left = 0
                right = len(prev) - 1
                prevPrice = -1
                currWidth = heightsAndWidths[h][-1][0]
                currPrice = heightsAndWidths[h][-1][1]
                while left <= right:
                    middle = (left + right) // 2
                    if prev[middle][0] <= currWidth:
                        prevPrice = prev[middle][1]
                        left = middle + 1
                    else:
                        right = middle -1

                if prevPrice >= currPrice:
                    heightsAndWidths[h].pop()

            if not heightsAndWidths[h]:
                del heightsAndWidths[h]
                heights.pop()

        # print(
        #     'heights', heights,
        #     'heightsAndWidths', heightsAndWidths,
        # )

        @lru_cache(None)
        def dfs(height, width):
            if height == 0 or width == 0:
                return 0

            res = 0
            for h in heights:
                if h > height:
                    break

                for w, p in heightsAndWidths.get(h, []):
                    if w > width:
                        break

                    res1 = p
                    res1 += dfs(height-h, width)
                    res1 += dfs(h, width-w)

                    res2 = p
                    res2 += dfs(height-h, w)
                    res2 += dfs(height, width-w)

                    res = max(res, res1, res2)

            return res

        return dfs(m, n)

class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        priceData = [[0]*(n+1) for i in range(m+1)]
        for h, w, p in prices:
            priceData[h][w] = p

        @lru_cache(None)
        def dfs(height, width):
            price = priceData[height][width]

            for i in range(1, min(math.ceil(height/2)+1, height)):
                price = max(price, dfs(i, width) + dfs(height-i, width))

            for i in range(1, min(math.ceil(width/2)+1, width)):
                price = max(price, dfs(height, i) + dfs(height, width - i))

            return price

        return dfs(m, n)


'''

[9, 7, [[4, 3, 2], [4, 4, 18], [5, 3, 16], [8, 7, 6]]]

0 0 0 0 x 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 x 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0


[[2,2,5][1,1,1]]

'''



def test ():
    params = [
        {
            'input': [3, 5, [[1,4,2],[2,2,7],[2,1,3]]],
            'output': 19,
        },
        {
            'input': [4, 6, [[3,2,10],[1,4,2],[4,1,3]]],
            'output': 32,
        },
        {
            'input': [9, 7, [[4,3,2],[5,3,16],[4,4,18],[8,7,6]]],
            'output': 54,
        },
    ]
    solution = Solution()

    for param in params:
        m, n, prices = param['input']
        result = solution.sellingWood(m, n, prices)
        correct = json.dumps(result) == json.dumps(param['output'])

        msg = 'SUCCESS' if correct else 'ERROR'
        msg += '\n'
        if not correct:
            msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()
