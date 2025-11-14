from typing import List
import json
from collections import deque, defaultdict
import heapq
from functools import lru_cache


class Solution_0:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        length = len(strs)

        data = []
        for word in strs:
            item = [0, 0]
            for char in word:
                if char == '0':
                    item[0] += 1
                else:
                    item[1] += 1
            data.append(item)


        cache = {}
        res = 0
        def dfs(visited, acc, count):
            nonlocal res, length, cache

            key = '_'.join([str(num) for num in visited])
            if key in cache:
                return

            cache[key] = 1

            if acc[0] <= m and acc[1] <= n:
                res = max(res, count)

            for i in range(length):
                if visited[i] == 1:
                    continue

                if acc[0] + data[i][0] <= m and acc[1] + data[i][1] <= n:
                    acc[0] += data[i][0]
                    acc[1] += data[i][1]
                    visited[i] = 1

                    dfs(visited, acc, count + 1)

                    acc[0] -= data[i][0]
                    acc[1] -= data[i][1]
                    visited[i] = 0


        dfs([0]*length, [0,0], 0)

        return res


class Solution_1:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        length = len(strs)
        res = 0
        data = []
        for word in strs:
            item = [0, 0]
            for char in word:
                if char == '0':
                    item[0] += 1
                else:
                    item[1] += 1
            data.append(item)

        def dfs(id, acc, count):
            nonlocal res, length, strs

            if acc[0] <= m and acc[1] <= n:
                res = max(res, count)

            if id == length:
                return

            dfs(id+1, acc.copy(), count)
            if acc[0] + data[id][0] <= m and acc[1] + data[id][1] <= n:
                _acc = acc.copy()
                _acc[0] += data[id][0]
                _acc[1] += data[id][1]
                dfs(id+1, _acc, count + 1)

        dfs(0, [0,0], 0)

        return res


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        length = len(strs)
        data = []
        for word in strs:
            item = [0, 0]
            for char in word:
                if char == '0':
                    item[0] += 1
                else:
                    item[1] += 1
            data.append(item)

        cache = {}

        def dfs(id, zero, one):
            nonlocal res, length, strs

            key = f'{id}_{zero}_{one}'
            if key in cache:
                return cache[key]

            if id == length:
                return 0

            r = dfs(id+1, zero, one)

            if zero + data[id][0] <= m and one + data[id][1] <= n:
                r1 = 1 + dfs(id+1, zero + data[id][0], one + data[id][1])
                r = max(r, r1)

            cache[key] = r
            return cache[key]

        res = dfs(0, 0, 0)

        return res




def test ():
    params = [
        {
            'input': [["0","11","1000","01","0","101","1","1","1","0","0","0","0","1","0","0110101","0","11","01","00","01111","0011","1","1000","0","11101","1","0","10","0111"], 9, 80],
            'output': 17,
        },
        {
            'input': [["0","1101","01","00111","1","10010","0","0","00","1","11","0011"], 63, 36],
            'output': 12,
        },
        {
            'input': [["10001110","11000","111110"], 6, 6],
            'output': 1,
        },
        {
            'input': [["10","0001","111001","1","0"], 5, 3],
            'output': 4,
        },
        {
            'input': [["10","0","1"], 1, 1],
            'output': 2,
        },
    ]
    solution = Solution()

    for param in params:
        strs, m, n = param['input']
        result = solution.findMaxForm(strs, m, n)
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
