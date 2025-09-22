from typing import List
import json
from collections import deque
import heapq

class Router:

    def __init__(self, memoryLimit: int):
        self._limit = memoryLimit
        self._packets = set()
        self._queue = deque()
        self._destinations = {}

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        val = (source, destination, timestamp)
        if val in self._packets:
            return False

        if len(self._packets) == self._limit:
            dest = self._queue.popleft()
            src, tms = self._destinations[dest].popleft()
            self._packets.remove((src, dest, tms))

        self._packets.add(val)
        self._queue.append(destination)
        self._destinations[destination] = self._destinations.get(destination, deque())
        self._destinations[destination].append((source, timestamp))

        return True

    def forwardPacket(self) -> List[int]:
        if len(self._queue) == 0:
            return []

        dest = self._queue.popleft()
        src, tms = self._destinations[dest].popleft()
        self._packets.remove((src, dest, tms))

        return [src, dest, tms]

    def _get_start(self, arr, startTime, endTime):
        res = -1
        start = 0
        end = len(arr) - 1

        while start <= end:
            middle = (start + end) // 2
            if arr[middle][1] < startTime:
                start = middle + 1
            elif arr[middle][1] >= startTime and arr[middle][1] <= endTime:
                res = middle
                end = middle - 1
            else:
                end = middle - 1

        return res

    def _get_end(self, arr, startTime, endTime):
        res = -1
        start = 0
        end = len(arr) - 1

        while start <= end:
            middle = (start + end) // 2
            if arr[middle][1] > endTime:
                end = middle - 1
            elif arr[middle][1] >= startTime and arr[middle][1] <= endTime:
                res = middle
                start = middle + 1
            else:
                start = middle + 1

        return res

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        dest_q = self._destinations.get(destination, deque())

        start = self._get_start(dest_q, startTime, endTime)
        end = self._get_end(dest_q, startTime, endTime)

        if start == -1 or end == - 1:
            return 0

        return end - start + 1



def test ():
    params = [
        {
            'input': [
                ["Router","addPacket","addPacket","forwardPacket"],
                [[4],[3,4,1],[2,3,1],[]],
            ],
            'output': [None,True,True,[3,4,1]],
        },

        {
            'input': [
                ['Router', 'addPacket', 'addPacket', 'addPacket', 'addPacket', 'addPacket', 'forwardPacket', 'addPacket', 'getCount'],
                [[3], [1, 4, 90], [2, 5, 90], [1, 4, 90], [3, 5, 95], [4, 5, 105], [], [5, 2, 110], [5, 100, 110]]
            ],
            'output': [None, True, True, False, True, True, [2, 5, 90], True, 1],
        },
        {
            'input': [
                ['Router', 'addPacket', 'forwardPacket', 'forwardPacket'],
                [[2], [7, 4, 90], [], []]
            ],
            'output': [None, True, [7, 4, 90], []],
        }
    ]

    for param in params:
        commands = param['input'][0]
        data = param['input'][1]
        router = Router(*data[0])

        result = None
        for i in range(1, len(commands)):
            if commands[i] == 'addPacket':
                result = router.addPacket(*data[i])
            elif commands[i] == 'forwardPacket':
                result = router.forwardPacket(*data[i])
            elif commands[i] == 'getCount':
                result = router.getCount(*data[i])

            if json.dumps(param['output'][i]) == json.dumps(result):
                print('SUCCESS', '\n')
            else:
                print('ERROR', param['output'][i], result, '\n')




if __name__ == '__main__':
    test()
