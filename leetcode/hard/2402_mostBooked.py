from typing import List
import json
import heapq
from collections import defaultdict


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        M = len(meetings)
        meetings.sort()

        meetQueue = []
        roomsQueue = [i for i in range(n)]
        heapq.heapify(roomsQueue)

        cnt = defaultdict(int)
        res = 0
        t = 0

        for i in range(M):
            start, end = meetings[i]
            t = max(t, start)

            while meetQueue and meetQueue[0][0] <= t:
                time, room = heapq.heappop(meetQueue)
                heapq.heappush(roomsQueue, room)

            roomId = -1
            if roomsQueue:
                roomId = heapq.heappop(roomsQueue)
            else:
                time, _room = heapq.heappop(meetQueue)
                t = max(t, time)
                roomId = _room

            tEnd = t + end - start
            heapq.heappush(meetQueue, (tEnd, roomId))


            cnt[roomId] += 1

            if cnt[roomId] > cnt[res] or (cnt[roomId] == cnt[res] and roomId < res):
                res = roomId

        return res

'''
[4, [[18,19],[3,12],[17,19],[2,13],[7,10]]]

[[2, 13], [3, 12], [7, 10], [17, 19], [18, 19]]
0 - 2,13
1 - 3,12
2 - 7,10
3 - 17,19
---


'''


def test ():
    params = [
        {
            'input': [4, [[18,19],[3,12],[17,19],[2,13],[7,10]]],
            'output': 0,
        },
        {
            'input': [2, [[0,10],[1,5],[2,7],[3,4]]],
            'output': 0,
        },
        {
            'input': [3, [[1,20],[2,10],[3,5],[4,9],[6,8]]],
            'output': 1,
        },
    ]
    solution = Solution()

    for param in params:
        n, meetings = param['input']
        result = solution.mostBooked(n, meetings)
        print(
            'SUCCESS' if json.dumps(result) == json.dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
