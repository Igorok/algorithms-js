from typing import List
import json
from collections import deque, defaultdict
import math

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        arr = sorted(ranks)

        def canRepair(limit):
            res = 0
            for rank in arr:
                n2 = limit // rank
                n = math.floor(math.sqrt(n2))
                res += n

                if res >= cars:
                    return True

            return res >= cars

        '''
        limit = arr[0] * cars**2
        for i in range(1, limit):
            if canRepair(i):
                return i
        '''

        start = 1
        end = arr[0] * cars**2
        res = end
        while start <= end:
            m = (start + end) // 2
            if canRepair(m):
                res = m
                end = m - 1
            else:
                start = m + 1


        return res


'''
rank r can repair n cars in r * n**2 minutes

r   c   time
4   1   4
2   1   2
3   1   3
1   1   1
4 car

r   c   time
4   2   16
2   2   8
3   2   12
1   4   16
10 car

---

14
10 7 1
10 1 1 1 1
7 7





'''


def test ():
    params = [
        {
            'input': [[4,2,3,1], 10],
            'output': 16,
        },
        {
            'input': [[5,1,8], 6],
            'output': 16,
        },
    ]
    solution = Solution()

    for param in params:
        ranks, cars = param['input']
        result = solution.repairCars(ranks, cars)
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
