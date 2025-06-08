from typing import List
import json
from collections import deque

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:

        myBoxes = set()
        myKeys = set()
        boxesQueue = deque()

        for box in initialBoxes:
            if status[box] == 1:
                boxesQueue.append(box)
            else:
                myBoxes.add(box)

        res = 0
        while boxesQueue:
            box = boxesQueue.popleft()
            res += candies[box]

            for childBox in containedBoxes[box]:
                if status[childBox] == 1:
                    boxesQueue.append(childBox)
                    continue

                if status[childBox] == 0 and childBox in myKeys:
                    boxesQueue.append(childBox)
                    myKeys.remove(childBox)
                    continue

                myBoxes.add(childBox)

            for key in keys[box]:
                if key in myBoxes:
                    boxesQueue.append(key)
                    myBoxes.remove(key)
                else:
                    myKeys.add(key)

        return res


def test ():
    params = [
        {
            'input': [
                [1,0,1,0],
                [7,5,4,100],
                [[],[],[1],[]],
                [[1,2],[3],[],[]],
                [0],
            ],
            'output': 16,
        },
        {
            'input': [
                [1,0,0,0,0,0],
                [1,1,1,1,1,1],
                [[1,2,3,4,5],[],[],[],[],[]],
                [[1,2,3,4,5],[],[],[],[],[]],
                [0],
            ],
            'output': 6,
        },
    ]
    solution = Solution()

    for param in params:
        status, candies, keys, containedBoxes, initialBoxes = param['input']
        result = solution.maxCandies(status, candies, keys, containedBoxes, initialBoxes)
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
