from typing import List
from json import dumps
import heapq
from collections import deque

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        visited = [-1]*n
        couples = []
        resLoop = 0

        # looking for a loop
        def dfsLoop(node):
            localNodes = {}

            def rec(i, length):
                nonlocal resLoop
                visited[i] = 1
                localNodes[i] = length
                # resLoop = max(resLoop, length)

                nei = favorite[i]
                if nei in localNodes:
                    loop = length - localNodes[nei] + 1
                    resLoop = max(resLoop, loop)
                    if loop == 2:
                        couples.append((i, nei))
                    return
                if visited[nei] == 1:
                    return
                rec(nei, length + 1)

            rec(node, 1)

        for i in range(n):
            if visited[i] == 1:
                continue
            dfsLoop(i)

        if len(couples) == 0:
            return resLoop

        # looking for a sides of every couple
        resCouples = 0
        inveredFavorite = {}
        for i in range(n):
            f = favorite[i]
            arr = inveredFavorite.get(f, [])
            arr.append(i)
            inveredFavorite[f] = arr

        def dfsCouple(left, right):
            def rec(node):
                length = 0
                if not node in inveredFavorite:
                    return 1
                for nei in inveredFavorite[node]:
                    if (node == left and nei == right) or (node == right and nei == left):
                        continue
                    length = max(length, rec(nei))
                return length + 1


            leftLength = rec(left)
            rightLength = rec(right)

            return leftLength + rightLength

        for left, right in couples:
            resCouples += dfsCouple(left, right)

        return max(resLoop, resCouples)

'''
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
1,0,3,2,5,6,7,4,9,8,11,10,11,12,10

0 1 2 3  4  5 6 7 8 9 10 11 12 13 14 15
7,0,7,13,11,6,8,5,9,8,9, 14,15,7, 11,6

0 1 2 3 4 5 6 7 8 9  10 11
1,2,3,4,5,6,3,8,9,10,11,8

'''


def test ():
    params = [
        {
            'input': [2,2,1,2],
            'output': 3,
        },
        {
            'input': [1,2,0],
            'output': 3,
        },
        {
            'input': [3,0,1,4,1],
            'output': 4,
        },
        {
            'input': [1,0,0,2,1,4,7,8,9,6,7,10,8],
            'output': 6,
        },
        {
            'input': [1,0,3,2,5,6,7,4,9,8,11,10,11,12,10],
            'output': 11,
        },
        {
            'input': [7,0,7,13,11,6,8,5,9,8,9,14,15,7,11,6],
            'output': 11,
        },
        {
            'input': [1,2,3,4,5,6,3,8,9,10,11,8],
            'output': 4,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.maximumInvitations(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

if __name__ == '__main__':
    test()
