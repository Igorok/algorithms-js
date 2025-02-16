from typing import List
from json import dumps
import heapq
from collections import deque, defaultdict

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        profitByCapital = defaultdict(list)
        possibleProfit = []

        maxCap = -1
        for i in range(len(profits)):
            p = profits[i]
            c = capital[i]
            if p == 0:
                continue
            profitByCapital[c].append(p)

            maxCap = max(maxCap, c)

            if c <= w:
                heapq.heappush(possibleProfit, -p)


        while k > 0 and possibleProfit:
            profit = -heapq.heappop(possibleProfit)

            if w < maxCap:
                for i in range(w+1, w+profit+1):
                    if i in profitByCapital:
                        for num in profitByCapital[i]:
                            heapq.heappush(possibleProfit, -num)

            w += profit
            possibleProfit = possibleProfit[:k]
            k -= 1


        return w

    def findMaximizedCapital_1(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        profitByCapital = []
        possibleProfit = []


        maxCap = -1
        for i in range(len(profits)):
            p = profits[i]
            c = capital[i]
            if p == 0:
                continue

            if c <= w:
                heapq.heappush(possibleProfit, -p)
            else:
                heapq.heappush(profitByCapital, (c, p))


        while k > 0 and possibleProfit:
            profit = -heapq.heappop(possibleProfit)
            w += profit
            k -= 1

            while profitByCapital and profitByCapital[0][0] <= w:
                c, p = heapq.heappop(profitByCapital)
                heapq.heappush(possibleProfit, -p)





        return w




def test ():
    params = [
        {
            'input': [2, 0, [1,2,3], [0,1,1]],
            'output': 4,
        },
        {
            'input': [3, 0, [1,2,3], [0,1,2]],
            'output': 6,
        },
    ]
    solution = Solution()

    for param in params:
        k, w, profits, capital = param['input']
        result = solution.findMaximizedCapital(k, w, profits, capital)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

if __name__ == '__main__':
    test()
