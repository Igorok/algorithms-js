import sys
sys.setrecursionlimit(1500)
from typing import List
import json
from collections import deque, defaultdict
import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort()
        eventsQueue = []
        id = 0
        now = 1
        res = 0

        while id < n or eventsQueue:
            while id < n and events[id][1] < now:
                id += 1

            if not eventsQueue and id < n:
                now = max(now, events[id][0])

            while eventsQueue and eventsQueue[0] < now:
                heapq.heappop(eventsQueue)

            while id < n and events[id][0] == now:
                heapq.heappush(eventsQueue, events[id][1])
                id += 1

            if eventsQueue and eventsQueue[0] >= now:
                heapq.heappop(eventsQueue)
                res += 1

            now += 1


        return res



def test ():
    params = [
        {
            'input': [[1,5],[1,5],[1,5],[2,3],[2,3]],
            'output': 5,
        },
        {
            'input': [[1,2],[2,3],[3,4]],
            'output': 3,
        },
        {
            'input': [[1,2],[2,3],[3,4],[1,2]],
            'output': 4,
        },
    ]
    solution = Solution()

    for param in params:
        events = param['input']
        result = solution.maxEvents(events)
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
