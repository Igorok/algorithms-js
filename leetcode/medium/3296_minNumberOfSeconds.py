from typing import List
from json import dumps
from collections import deque
import heapq


class Solution_0:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        workerTimes.sort()

        def isOk(timeLimit):
            nonlocal workerTimes, mountainHeight

            res = 0
            for workTimer in workerTimes:
                local = 0
                i = 1
                while local + (i * workTimer) <= timeLimit:
                    local += (i * workTimer)
                    i += 1
                res += i - 1

            return res >= mountainHeight

        res = 0

        minFinished = 1

        localWeight = 0
        localTime = 1
        while localWeight < mountainHeight:
            localTime += localTime * workerTimes[0]
            localWeight += 1

        while minFinished <= localTime:
            middle = (minFinished + localTime) // 2
            if isOk(middle):
                res = middle
                localTime = middle - 1
            else:
                minFinished = middle + 1


        return res

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        workers = [(timer, timer, 1) for timer in workerTimes]
        heapq.heapify(workers)

        res = 0
        totalHeight = 0

        while totalHeight < mountainHeight:
            localTime, timer, id = heapq.heappop(workers)
            res = max(res, localTime)

            totalHeight += 1
            id += 1
            localTime += timer * id

            heapq.heappush(workers, (localTime, timer, id))

        return res


'''

workerTimes[i]
1 * workerTimes[i] + 2 * workerTimes[i] + ... + n * workerTimes[i]

xn = (1 + 2 + ... + n) * workerTimes[i]
weight = n
time = (1 + 2 + ... + n) * workerTimes[i]

an = a1 + (n-1)*d
Sn = n * (2a1 + d(n-1)) / 2
Sn = n * (a1 + an) / 2

d = 1
an = a1 + n - 1
Sn = n * (2a1 + n - 1) / 2

---

Sn = n * (2a1 + n - 1) / 2
Sn * 2 = 2a1 * n + n**2 - n
Sn / 2a1 = n + (n**2 - n) / 2a1

---

(1 + 2 + ... + n) * workerTimes[i] <= maxTime
(1 + 2 + ... + n) <= maxTime // workerTimes[i]

Sn <= maxTime // workerTimes[i]
n * (2a1 + d(n-1)) / 2 <= (maxTime // workerTimes[i])


totalTime
start = 0
end = n+1
while start <= end
    time = (1+...+i) *  workerTime

n ???

'''



def test ():
    params = [
        {
            'input': [4, [2,1,1]],
            'output': 3,
        },
        {
            'input': [10, [3,2,2,4]],
            'output': 12,
        },
        {
            'input': [5, [1]],
            'output': 15,
        },
        {
            'input': [99, [1,57]],
            'output': 3916,
        },
    ]
    solution = Solution()

    for param in params:
        mountainHeight, workerTimes = param['input']
        result = solution.minNumberOfSeconds(mountainHeight, workerTimes)

        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
