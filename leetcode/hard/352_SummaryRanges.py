from typing import List
import json
from collections import deque, defaultdict
from sortedcontainers import SortedList

class SummaryRanges:

    def __init__(self):
        self.nums = SortedList()
        self.parents = {}
        self.intervals = {}

    def getParent(self, value):
        if self.parents[value] == value:
            return value

        parent = self.getParent(self.parents[value])
        self.parents[value] = parent

        return parent


    def setParent(self, value1, value2):
        parent1 = self.getParent(value1)
        parent2 = self.getParent(value2)

        l1 = self.intervals[parent1][1] - self.intervals[parent1][0]
        l2 = self.intervals[parent2][1] - self.intervals[parent2][0]

        if l1 >= l2:
            self.parents[parent2] = parent1
            self.intervals[parent1] = [
                min(self.intervals[parent1][0], self.intervals[parent2][0]),
                max(self.intervals[parent1][1], self.intervals[parent2][1]),
            ]
            return parent1

        self.parents[parent1] = parent2
        self.intervals[parent2] = [
            min(self.intervals[parent1][0], self.intervals[parent2][0]),
            max(self.intervals[parent1][1], self.intervals[parent2][1]),
        ]

        return parent2


    def merge(self, value1, value2):
        parent1 = self.getParent(value1)
        parent2 = self.getParent(value2)

        self.nums.discard(parent1)
        self.nums.discard(parent2)

        newParent = self.setParent(value1, value2)
        self.nums.add(newParent)


    def addNum(self, value: int) -> None:
        if value in self.parents:
            return

        self.parents[value] = value
        self.intervals[value] = [value, value]

        if (value - 1) not in self.intervals and (value + 1) not in self.intervals:
            self.nums.add(value)
            return

        if (value-1) in self.parents:
            self.merge(value, value-1)

        if (value+1) in self.parents:
            self.merge(value, value+1)


    def getIntervals(self) -> List[List[int]]:
        res = []
        for num in self.nums:
            interval = self.intervals.get(num, [])
            res.append(interval)
        return res


def test ():
    params = [
        {
            'input': [
                ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"],
                [[], [1], [], [3], [], [7], [], [2], [], [6], []]
            ],
            'output': [None, None, [[1, 1]], None, [[1, 1], [3, 3]], None, [[1, 1], [3, 3], [7, 7]], None, [[1, 3], [7, 7]], None, [[1, 3], [6, 7]]],
        },
    ]

    for param in params:
        solution = SummaryRanges()
        commands, data = param['input']

        for i in range(1, len(commands)):
            result = None
            if commands[i] == 'addNum':
                result = solution.addNum(data[i][0])
            else:
                result = solution.getIntervals()


            correct = json.dumps(result) == json.dumps(param['output'][i])

            msg = 'SUCCESS' if correct else 'ERROR'
            msg += '\n'
            if not correct:
                msg += 'input ' + json.dumps(commands[i]) + ' '+ json.dumps(data[i]) +'\n'
                msg += 'output ' + json.dumps(param['output'][i]) + '\n'
                msg += 'result ' + json.dumps(result) + '\n'

            print(msg)


if __name__ == '__main__':
    test()
