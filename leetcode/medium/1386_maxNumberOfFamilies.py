
from typing import List
import json
from collections import Counter
from functools import cache

'''
Do you know this leetcode issue - "1386. Cinema Seat Allocation"?
Can you explain, what i don't understand?

n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
Output: 4
[0,1,1,0,0,0,0,1,0,0,]
[0,0,0,0,0,1,0,0,0,0,]
[1,0,0,0,0,0,0,0,0,1,]
I can get 4 positions in 1 row - (4,5,6,7)
I can get 4+4 positions in 2 row - (1,2,3,4)+(7,8,9,10)
I can get 4+4 positions in 3 row - (2,3,4,5)+(6,7,8,9)

n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
Output: 4
[0,0,0,1,0,0,1,0,0,0,]
[0,0,0,0,0,0,0,0,0,0,]
[0,0,0,0,0,0,0,0,0,0,]
[0,0,1,0,0,1,0,0,0,0,]
I can get 2 by 4 in row number 2
I can get 2 by 4 in row number 3
I can get 1 by 4 in row number 4
I have 5 places

Is it not example?
```
A four-person group must be assigned to four seats in the same row. The group can be seated in one of the following seat blocks:
seats 2, 3, 4, 5
seats 4, 5, 6, 7
seats 6, 7, 8, 9
```
Only this places available for siting?

I so tired by this leetcode crap, i waste half of hour to understand the description. I want to read a book about llm but my free hour is finished because of idiots description of no difficult task.


'''


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reservedSeats.sort()
        reservedSeats.append([n, 0])

        def calculate(arr):
            r = 0
            prev = 0
            for i in range(11):
                if arr[i] == 1:
                    prev = i
                    continue

                if i == 5 and prev <= 1:
                    r += 1
                    prev = 5
                if i == 7 and prev <= 3:
                    r += 1
                    prev = 7
                if i == 9 and prev <= 5:
                    r += 1
                    prev = 9

            return r

        prevRow = 0
        row = [1]*11
        res = 0
        for r,s in reservedSeats:
            if r == prevRow:
                row[s] = 1
                continue
            res += calculate(row)
            diff = r - prevRow - 1
            if diff > 0:
                res += 2*diff
            prevRow = r
            row = [0]*11
            row[s] = 1


        res += calculate(row)

        return res


def test ():
    params = [
        {
            'input': [3, [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]],
            'output': 4,
        },
        {
            'input': [2, [[2,1],[1,8],[2,6]]],
            'output': 2,
        },
        {
            'input': [4, [[4,3],[1,4],[4,6],[1,7]]],
            'output': 4,
        },
        {
            'input': [3, [[2,3]]],
            'output': 5,
        },
    ]
    solution = Solution()

    for param in params:
        n, reservedSeats = param['input']
        result = solution.maxNumberOfFamilies(n, reservedSeats)
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
