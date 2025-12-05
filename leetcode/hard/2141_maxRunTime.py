from typing import List
import json
from collections import deque
import heapq
import math

class Solution_0:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort(key = lambda x: -x)
        M = len(batteries)

        def isOk(num):
            nonlocal n

            id = 0
            remainder = 0

            for i in range(n):
                acc = 0
                if remainder > 0:
                    acc = remainder
                    remainder = 0

                idStart = id
                while acc < num and id < M:
                    acc += batteries[id]
                    id += 1

                if acc < num:
                    return False

                if acc > num and id - idStart > 1:
                    remainder = acc - n


            return True


        total = sum(batteries)
        # print('total', total)


        maxPossible = total // n
        minPossible = 0

        res = 0

        while minPossible <= maxPossible:
            middle = (minPossible + maxPossible) // 2

            if isOk(middle):
                res = middle
                minPossible = middle + 1
            else:
                maxPossible = middle - 1


        return res


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        M = len(batteries)
        batteries.sort()
        total = sum(batteries)

        acc = [0]*n
        for i in range(n):
            v = batteries[M-1-i]
            acc[n-1-i] = v
            total -= v

        res = acc[0]

        for i in range(n-1):
            diff = acc[i+1] - acc[i]
            required = (i+1) * diff
            if required > total:
                possible = total // (i+1)
                res = acc[i] + possible
                return res

            total -= required
            res = acc[i+1]

        if total:
            possible = total // n
            res = acc[n-1] + possible

        return res

'''
2
3 3 3

---

[3, [10,10,3,5]]
28; 28//3 = 9
3 5 10 10;
18(9) 9 10

10; 10; 5; 3
10; 10; 8;

---


2
3 3 3
3+3(2); 2+3

---

57
[12, [89, 83, 78, 70, 67, 53, 41, 35, 35, 32, 31, 29, 24, 16, 11, 6]]

89,
83,
78,
70,
67,
53, 41, = 94; 94 - 57 = 37
35, + 37 = 72
35, 32, 31, 29, 24, 16, 11, 6


'''



def test ():
    params = [
        {
            'input': [12, [11,89,16,32,70,67,35,35,31,24,41,29,6,53,78,83]],
            'output': 43,
        },
        {
            'input': [2, [10,3,5]],
            'output': 8,
        },
        {
            'input': [3, [10,10,3,5]],
            'output': 8,
        },
        {
            'input': [2, [3,3,3]],
            'output': 4,
        },
        {
            'input': [2, [1,1,1,1]],
            'output': 2,
        },
    ]
    solution = Solution()

    for param in params:
        n, batteries = param['input']
        result = solution.maxRunTime(n, batteries)
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
