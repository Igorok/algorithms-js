from collections import deque
from typing import List
from json import dumps

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        n = len(tasks)
        m = len(workers)
        tasks.sort()
        workers.sort()

        def checkWorkers(taskId: int) -> bool:
            workersQueue = deque()
            workerId = m - 1
            pillCount = pills

            for i in range(taskId, -1, -1):
                while workerId >= 0 and workers[workerId] + strength >= tasks[i]:
                    workersQueue.appendleft(workers[workerId])
                    workerId -= 1

                if not workersQueue:
                    return False

                if workersQueue[-1] >= tasks[i]:
                    workersQueue.pop()
                elif pillCount == 0:
                    return False
                else:
                    workersQueue.popleft()
                    pillCount -= 1;


            return True

        res = 0
        left = 0
        right = min(n, m) - 1

        while (left <= right):
            middle = (left + right) // 2
            if (checkWorkers(middle)):
                res = middle + 1
                left = middle + 1
            else:
                right = middle - 1

        return res

def test ():
    params = [
        {
            'input': [[3,2,1], [0,3,3], 1, 1],
            'output': 3,
        },
        {
            'input': [[5,4], [0,0,0], 1, 5],
            'output': 1,
        },
        {
            'input': [[10,15,30], [0,10,10,10,10], 3, 10],
            'output': 2,
        },
    ]
    solution = Solution()

    for param in params:
        tasks, workers, pills, strength = param['input']
        result = solution.maxTaskAssign(tasks, workers, pills, strength)

        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
