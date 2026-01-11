from typing import List
import heapq
import math
from collections import defaultdict, deque


class Solution_0:
    def addOperators(self, num: str, target: int) -> List[str]:
        N = len(num)

        def dfs(left, right):
            nonlocal N, num
            if left == N:
                return {}

            n = int(num[left:right+1])
            if right + 1 == N:
                return { n: [str(n)] }

            r1 = dfs(right+1, right+1)
            res = {}

            for k in r1:
                val = n*k
                res[val] = res.get(val, [])
                for s in r1[k]:
                    res[val].append(f'{n}*{s}')

                val = n+k
                res[val] = res.get(val, [])
                for s in r1[k]:
                    res[val].append(f'{n}+{s}')

                val = n-k
                res[val] = res.get(val, [])
                for s in r1[k]:
                    res[val].append(f'{n}-{s}')

            if right < N-1 and num[left] != '0':
                r1 = dfs(left, right+1)

                for k in r1:
                    res[k] = res.get(k, [])
                    res[k] += r1[k]

            return res


        res = dfs(0, 0)

        return res.get(target, [])


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        N = len(num)

        memo = {}
        def dfs(left, right):
            nonlocal N, num, memo
            ops = ['*', '+', '-']

            if left == N:
                return []

            if left in memo:
                return memo[left]

            n = num[left:right+1]

            if right+1 == N:
                return [[n]]

            res = []

            r = dfs(right+1, right+1)

            for item in r:
                for op in ops:
                    res.append([n, op] + item)

            if num[left] != '0':
                r = dfs(left, right+1)
                for item in r:
                    res.append(item)

            memo[left] = res

            return res

        comb = dfs(0,0)

        def check(data):
            nonlocal target
            arr = []

            i = 0
            while i < len(data):
                val = data[i]
                if val in '+-':
                    arr.append(val)
                    i+= 1
                elif val == '*':
                    n1 = arr.pop()
                    n2 = int(data[i+1])
                    arr.append(n1*n2)
                    i += 2
                else:
                    arr.append(int(data[i]))
                    i += 1

            r = arr[0]
            i = 1
            while i < len(arr):
                if arr[i] == '+':
                    r += arr[i+1]
                if arr[i] == '-':
                    r -= arr[i+1]
                i += 2

            return target == r

        res = []
        for val in comb:
            if check(val):
                res.append(''.join(val))

        return res




def test ():
    params = [
        {
            'input': ["123", 6],
            'output': ["1*2*3","1+2+3"],
        },
        {
            'input': ["232", 8],
            'output': ["2*3+2","2+3*2"],
        },
        {
            'input': ["3456237490", 9191],
            'output': [],
        },
        {
            'input': ["111", 1],
            'output': ["1*1*1","1+1-1","1-1+1"],
        },
        {
            'input': ["1", 1],
            'output': ["1"],
        },
    ]
    solution = Solution()

    for param in params:
        num, target = param['input']
        result = solution.addOperators(num, target)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
