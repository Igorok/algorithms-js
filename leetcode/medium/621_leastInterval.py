from typing import List
import json
from collections import deque
import heapq

class Solution_0:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        memo = {}

        for t in tasks:
            memo[t] = memo.get(t, 0) + 1

        taskQueue = [(-memo[t], t) for t in memo]
        heapq.heapify(taskQueue)

        # print(taskQueue)

        res = 0
        while taskQueue:
            maxCnt = -taskQueue[0][0]

            length = n+1
            table = [[None]*length for i in range(maxCnt)]

            pastCell = 0
            cnt = 0
            lbl = '0'
            for c in range(length):
                if not taskQueue and cnt == 0:
                    break
                for r in range(maxCnt):
                    if not taskQueue and cnt == 0:
                        break
                    if cnt == 0:
                        cnt, lbl = heapq.heappop(taskQueue)

                    table[r][c] = lbl
                    cnt += 1

                    if r == maxCnt - 1:
                        pastCell = c

            if cnt != 0:
                heapq.heappush(taskQueue, (cnt, lbl))

            res += (maxCnt-1)*length + pastCell+1

        return res



class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        memo = {}

        for t in tasks:
            memo[t] = memo.get(t, 0) + 1

        taskQueue = [(1, -memo[t], t) for t in memo]
        heapq.heapify(taskQueue)

        # print(taskQueue)

        days = 1
        while taskQueue:
            if days < taskQueue[0][0]:
                days = taskQueue[0][0]

            day, cnt, lbl = heapq.heappop(taskQueue)
            cnt += 1
            day += (n+1)

            if cnt != 0:
                heapq.heappush(taskQueue, (day, cnt, lbl))

            if taskQueue:
                days += 1

        return days

'''

3
a 3 b 3 c 2

- 1 2 3 4
1
5
9

- 1 2 3
1 a b -
4 a b -
7 a b

[["A","B","C","A"], 2]

a 2 b 1 c 1

- 1 2 3
1 a b c
4 a


'''




def test ():
    params = [
        {
            'input': [["A","A","A","B","B","B"], 2],
            'output': 8,
        },
        {
            'input': [["A","C","A","B","D","B"], 1],
            'output': 6,
        },
        {
            'input': [["A","A","A", "B","B","B"], 3],
            'output': 10,
        },
        {
            'input': [["A","B","C","A"], 2],
            'output': 4,
        },
    ]
    solution = Solution()

    for param in params:
        tasks, n = param['input']
        result = solution.leastInterval(tasks, n)
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
