from typing import List
import json
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        n2 = n**2
        visited = [[-1]*n for i in range(n)]
        visited[-1][0] = 1

        def getNumByLoc(y, x):
            y = n - y - 1
            num = y * n
            num += x + 1 if (y % 2) == 0 else n - x
            return num

        def getLocByNum(num):
            y = num // n
            rem = num % n
            if rem == 0:
                y -= 1
                rem = n
            x = rem - 1 if ((y % 2) == 0) else n - rem
            return (n - y - 1, x)

        # arr = []
        # for i in range(n):
        #     arr.append([])
        #     for j in range(n):
        #         num = getNumByLoc(i, j)
        #         arr[-1].append({
        #             num,
        #             getLocByNum(num),
        #         })

        stepsQueue = deque()
        stepsQueue.append((1, 0))

        while stepsQueue:
            num, steps = stepsQueue.popleft()
            y, x = getLocByNum(num)

            steps += 1

            for val in range(num + 1, min(num + 7, n2+1)):
                if val == n2:
                    return steps

                y, x = getLocByNum(val)
                if visited[y][x] == 1:
                    continue
                visited[y][x] = 1

                if board[y][x] == -1:
                    stepsQueue.append((val, steps))
                    continue

                jump = board[y][x]
                if jump == n2:
                    return steps
                y, x = getLocByNum(jump)
                # Second jump is not visited. I can apply second jump only step by step.
                # if visited[y][x] == 1:
                #     continue
                # visited[y][x] = 1
                stepsQueue.append((jump, steps))


        return -1

'''

[
[-1,-1],
[-1, 3]
]



[
[-1, 1, 2,-1],
[ 2,13,15,-1],
[-1,10,-1,-1],
[-1, 6, 2, 8]
]

[
[-1,-1,-1,46,47,-1,-1,-1],
[51,-1,-1,63,-1,31,21,-1],
[-1,-1,26,-1,-1,38,-1,-1],
[-1,-1,11,-1,14,23,56,57],
[11,-1,-1,-1,49,36,-1,48],
[-1,-1,-1,33,56,-1,57,21],
[-1,-1,-1,-1,-1,-1,2,-1],
[-1,-1,-1,8,3,-1,6,56]
]









'''

def test ():
    params = [
        {
            'input': [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]],
            'output': 4,
        },
        {
            'input': [[-1,-1],[-1,3]],
            'output': 1,
        },
        {
            'input': [[-1,1,2,-1],[2,13,15,-1],[-1,10,-1,-1],[-1,6,2,8]],
            'output': 2,
        },

        {
            'input': [[-1,-1,-1,46,47,-1,-1,-1],[51,-1,-1,63,-1,31,21,-1],[-1,-1,26,-1,-1,38,-1,-1],[-1,-1,11,-1,14,23,56,57],[11,-1,-1,-1,49,36,-1,48],[-1,-1,-1,33,56,-1,57,21],[-1,-1,-1,-1,-1,-1,2,-1],[-1,-1,-1,8,3,-1,6,56]],
            'output': 4,
        },
        {
            'input': [[-1,-1,27,13,-1,25,-1],[-1,-1,-1,-1,-1,-1,-1],[44,-1,8,-1,-1,2,-1],[-1,30,-1,-1,-1,-1,-1],[3,-1,20,-1,46,6,-1],[-1,-1,-1,-1,-1,-1,29],[-1,29,21,33,-1,-1,-1]],
            'output': 4,
        },


    ]
    solution = Solution()

    for param in params:
        result = solution.snakesAndLadders(param['input'])
        correct = json.dumps(result) == json.dumps(param['output'])

        msg = 'SUCCESS' if json.dumps(result) == json.dumps(param['output']) else 'ERROR'
        msg += '\n'
        if not correct:
            msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()
