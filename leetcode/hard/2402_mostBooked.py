from typing import List
import json
import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetingsInRoom = [0]*n
        rooms = [(0, i) for i in range(n)]
        heapq.heapify(rooms)
        meetings = sorted(meetings)

        id = 0
        time = 0
        l = len(meetings)
        while id < l:
            if time < rooms[0][0]:
                time = rooms[0][0]

            if id < l and time < meetings[id][0]:
                time = meetings[id][0]

            while time > rooms[0][0]:
                room = heapq.heappop(rooms)
                heapq.heappush(rooms, (time, room[1]))

            while time >= rooms[0][0] and id < l and time >= meetings[id][0]:
                room = heapq.heappop(rooms)
                duration = meetings[id][1] - meetings[id][0]
                heapq.heappush(rooms, (time + duration, room[1]))
                meetingsInRoom[room[1]] += 1
                id += 1

            time += 1

        res = 0

        for i in range(n):
            if meetingsInRoom[i] > meetingsInRoom[res]:
                res = i

        return res


'''
[[2, 13], [3, 12], [7, 10], [17, 19], [18, 19]]


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
