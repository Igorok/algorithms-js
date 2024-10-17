from typing import List
from json import dumps
import random
import time

class Solution:
    def minimumSteps_(self, s: str) -> int:
        steps = 0

        arr = list(s)
        for i in range(1, len(s)):
            change = False
            for j in range(len(s) - i):
                if arr[j] == '1' and arr[j+1] == '0':
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    steps += 1
                    change = True
            if not change:
                break

        # print('arr', arr)

        return steps


    def minimumSteps(self, s: str) -> int:
        steps = 0

        zero = -1
        one = -1

        for i in range(len(s)):
            if s[i] == '0':
                if zero == -1:
                    zero = i
                if one != -1:
                    steps += i - one
                    zero = one
                    one += 1
            else:
                if one == -1:
                    one = i

        return steps



'''.git/

01010101
0 -
0 1
2 1 = 1


1100100111
2
1100001111
4
1000011111
4
0000111111


'''


def test():
    solution = Solution()
    for i in range(3):
        t1 = time.time()
        string = ''
        for i in range(1000):
            k = random.randint(0, 1)
            string += str(k)
        t2 = time.time()

        print('generation', t2 - t1)
        print('string', string)

        t1 = time.time()
        r1 = solution.minimumSteps_(string)
        t2 = time.time()

        t3 = time.time()
        r2 = solution.minimumSteps(string)
        t4 = time.time()

        print(
            'SUCCESS' if r1 == r2 else 'ERROR',
            'r1', r1,
            'time', t2 - t1,
            'r2', r2,
            'time', t4 - t3,
            '\n',
        )


if __name__ == '__main__':
    test()
