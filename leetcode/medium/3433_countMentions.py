from typing import List
import json
from collections import deque, defaultdict, Counter
import heapq
import math
from functools import cache
from functools import cmp_to_key






class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        def comparator(a, b):
            t1 = int(a[1])
            t2 = int(b[1])

            if t1 == t2:
                if a[0] == 'OFFLINE':
                    return -1
                if b[0] == 'OFFLINE':
                    return 1

            return t1 - t2

        events.sort(key=cmp_to_key(comparator))

        # print('events', events)

        offline = [-100] * numberOfUsers
        res = [0] * numberOfUsers

        for type, ts, data in events:
            ts = int(ts)
            if type == 'OFFLINE':
                id = int(data)
                offline[id] = ts
                continue

            if data == 'ALL':
                for i in range(numberOfUsers):
                    res[i] += 1
                continue

            if data == 'HERE':
                for i in range(numberOfUsers):
                    if offline[i] + 60 > ts:
                        continue
                    res[i] += 1
                continue

            for id in data.split(' '):
                id = int(id[2:])
                res[id] += 1


        return res




def test ():
    params = [
        {
            'input': [2, [["MESSAGE","71","HERE"],["MESSAGE","10","id1 id0"],["OFFLINE","11","0"]]],
            'output': [2,2],
        },
        {
            'input': [2, [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","12","ALL"]]],
            'output': [2,2],
        },
        {
            'input': [2, [["OFFLINE","10","0"],["MESSAGE","12","HERE"]]],
            'output': [0,1],
        },
        {
            'input': [2, [["MESSAGE","71","HERE"],["MESSAGE","10","id1 id0"],["MESSAGE","10","HERE"],["OFFLINE","10","0"]]],
            'output': [2,3],
        },
    ]
    solution = Solution()

    for param in params:
        numberOfUsers, events  = param['input']
        result = solution.countMentions(numberOfUsers, events)
        correct = json.dumps(result) == json.dumps(param['output'])

        msg = 'SUCCESS' if correct else 'ERROR'
        msg += '\n'
        if not correct:
            # msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()
