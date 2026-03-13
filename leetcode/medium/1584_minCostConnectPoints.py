from typing import List
from json import dumps
from collections import deque
import heapq


class Solution_0:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        edges = []

        for i in range(N):
            for j in range(i+1, N):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))

        edges.sort()

        parents = [i for i in range(N)]


        def getParent(node):
            if parents[node] == node:
                return node

            p = getParent(parents[node])
            parents[node] = p

            return p

        def setParent(node1, node2):
            parent1 = getParent(node1)
            parent2 = getParent(node2)

            if parent1 == parent2:
                return False

            parents[parent2] = parent1
            return True

        minCost = 0
        readyEdges = 0

        for dist, node1, node2 in edges:
            if readyEdges == N-1:
                break

            if setParent(node1, node2):
                minCost += dist
                readyEdges += 1

        return minCost

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        minCost = 0
        edgesCount = 0

        edgesHeap = [(0, 0)]
        visited = [False] * N

        while edgesCount < N:
            dist, node = heapq.heappop(edgesHeap)

            if visited[node]:
                continue

            visited[node] = True
            minCost += dist
            edgesCount += 1

            for i in range(N):
                if visited[i]:
                    continue

                dist = abs(points[i][0] - points[node][0]) + abs(points[i][1] - points[node][1])
                heapq.heappush(edgesHeap, (dist, i))


        return minCost


def test ():
    params = [
        {
            'input': [[0,0],[2,2],[3,10],[5,2],[7,0]],
            'output': 20,
        },
        {
            'input': [[3,12],[-2,5],[-4,1]],
            'output': 18,
        },
    ]
    solution = Solution()

    for param in params:
        points = param['input']
        result = solution.minCostConnectPoints(points)

        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
