from typing import List
from json import dumps
import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        total = 0
        classQueue = []
        for p, t in classes:
            if p == t:
                total += 1
                continue

            profit = (p+1)/(t+1) - p/t
            classQueue.append((-profit, p, t))

        heapq.heapify(classQueue)

        while len(classQueue) > 0 and extraStudents > 0:
            profit, p, t = heapq.heappop(classQueue)
            profit = -profit

            extraStudents -= 1
            p += 1
            t += 1
            profit = (p+1)/(t+1) - p/t

            heapq.heappush(classQueue, (-profit, p, t))

        for profit, p, t in classQueue:
            total += p / t

        return total / len(classes)

'''
(5/6 + 5/7 + 2/10 + 3/9) / 4


[[[2,4],[3,9],[4,5],[2,10]], 4],

(2/4 + 3/9 + 4/5 + 2/10) / 4

'''

def test ():
    params = [
        {
            'input': [[[2,4],[3,9],[4,5],[2,10]], 4],
            'output': 0.53485,
        },
        {
            'input': [ [[1,2],[3,5],[2,2]], 2],
            'output': 0.78333,
        },

    ]
    solution = Solution()

    for param in params:
        classes, extraStudents = param['input']
        result = solution.maxAverageRatio(classes, extraStudents)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
