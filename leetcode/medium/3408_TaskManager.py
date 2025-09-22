from typing import List
from json import dumps
import heapq
from collections import deque

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.queue = list()
        self.tasks = dict()

        for u, t, p in tasks:
            self.queue.append((-p, -t))
            self.tasks[t] = {
                'p': p,
                'u': u,
            }

        heapq.heapify(self.queue)

    def _isValid(self):
        if len(self.queue) == 0:
            return True
        p = -self.queue[0][0]
        t = -self.queue[0][1]

        return t in self.tasks and self.tasks[t]['p'] == p

    def _clean(self):
        while not self._isValid():
            heapq.heappop(self.queue)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.tasks[taskId] = {
            'p': priority,
            'u': userId,
        }
        self._clean()
        heapq.heappush(self.queue, (-priority, -taskId))


    def edit(self, taskId: int, newPriority: int) -> None:
        self.tasks[taskId]['p'] = newPriority
        self._clean()
        heapq.heappush(self.queue, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        del self.tasks[taskId]
        self._clean()

    def execTop(self) -> int:
        self._clean()
        if len(self.queue) == 0:
            return -1
        item = heapq.heappop(self.queue)
        p = -item[0]
        t = -item[1]
        u = self.tasks[t]['u']
        del self.tasks[t]
        return u

'''

[[1, 101, 10], [2, 102, 20], [3, 103, 15]]


'''


def test ():
    params = [
        {
            'input': [
                ["TaskManager", "add", "edit", "execTop", "rmv", "add", "execTop"],
                [
                    [[1, 101, 10], [2, 102, 20], [3, 103, 15]],
                    [4, 104, 5],
                    [102, 8],
                    [],
                    [101],
                    [5, 105, 15],
                    []
                ],
            ],
            'output': [None, None, None, 3, None, None, 5],
        },
    ]

    for param in params:
        commands, data = param['input']

        taskManager = TaskManager(data[0])

        for i in range(1, len(commands)):
            command = commands[i]
            argument = data[i]

            if command == 'add':
                taskManager.add(argument[0], argument[1], argument[2])
            elif command == 'edit':
                taskManager.edit(argument[0], argument[1])
            elif command == 'rmv':
                taskManager.rmv(argument[0])
            elif command == 'execTop':
                r = taskManager.execTop()
                print(
                    'SUCCESS' if r == param['output'][i] else 'ERROR',
                    '\n input', command, argument,
                    '\n output', param['output'][i],
                    '\n result', r,
                    '\n',
                )


if __name__ == '__main__':
    test()
