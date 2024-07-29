import math
from typing import List
from collections import deque, defaultdict

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj = defaultdict(list)
        for ednge in edges:
            fr, to = ednge
            adj[fr].append(to)
            adj[to].append(fr)

        result = -1
        nodesTime = defaultdict(list)
        nodesQueue = deque([(1, 0)])


        while len(nodesQueue):
            val = nodesQueue.popleft()
            print('val', val)
            node, currentTime = val

            print(
                'node', node,
                'currentTime', currentTime,
            )

            if (node == n):
                if (result == -1):
                    result = currentTime
                    print(
                        'result', result,
                    )
                elif currentTime != result:
                    return currentTime

            period = math.floor(currentTime / change)
            print(
                'period', period,
                'math.remainder(period, 2)', period % 2,
            )
            if (period % 2 == 1):
                currentTime = change * (period + 1)
                print(
                    'change * (period + 1)', change * (period + 1),
                )

            for nei in adj[node]:
                if len(nodesTime[nei]) == 0 or (
                    len(nodesTime[nei]) == 1
                    and currentTime + time != nodesTime[nei][0]
                ):
                    print(
                        'nei', nei,
                        'currentTime + time', currentTime + time,
                    )
                    nodesTime[nei].append(currentTime + time)
                    nodesQueue.append((nei, currentTime + time))


'''


val (1, 0)
node 1 currentTime 0
period 0
nei 2
nei 3
nei 4

val (4, 3)
node 4 currentTime 3
period 0
nei 1
nei 3
nei 5

val (5, 6)
node 5 currentTime 6
result 6
period 1
change * (period + 1) 10
nei 4

val (4, 13)
node 4 currentTime 13
period 2
nei 1
nei 3
nei 5

val (5, 16)
node 5 currentTime 16
ERROR n 5 edges [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]] time 3 change 5 output 13 result 16






'''



def main ():
    solution = Solution()

    params = [
        {
            'n': 5,
            'edges': [[1,2],[1,3],[1,4],[3,4],[4,5]],
            'time': 3,
            'change': 5,
            'output': 13,
        },
        {
            'n': 2,
            'edges': [[1,2]],
            'time': 3,
            'change': 2,
            'output': 11,
        }
    ]

    for item in params:
        result: int = solution.secondMinimum(item['n'], item['edges'], item['time'], item['change'])
        print(
            'SUCCESS' if item['output'] == result else 'ERROR',
            'n', item['n'],
            'edges', item['edges'],
            'time', item['time'],
            'change', item['change'],
            'output', item['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    main()