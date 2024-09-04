from typing import List
import json
import heapq

class Solution:
    def dijkstra (self):
        self.matrix = [[-2]*self.n for _ in range(self.n)]

        adj = [[] for _ in range(self.n)]
        for i in range(len(self.edges)):
            start, end, weight = self.edges[i]
            w = weight if weight > 0 else 1
            adj[start].append([end, w])
            adj[end].append([start, w])

            self.matrix[start][end] = weight
            self.matrix[end][start] = weight

        nodesPath = [float('inf')] * self.n
        nodesParent = [-1] * self.n
        visited = [-1] * self.n

        nodesHeap = [(0, self.source)]
        visited[self.source] = 1
        nodesPath[self.source] = 0

        while len(nodesHeap) != 0:
            weight, node = heapq.heappop(nodesHeap)
            if node == self.destination:
                continue

            for nei in adj[node]:
                id, w = nei
                if id == self.source:
                    continue
                newPath = int(weight + w)
                if visited[id] == -1 or nodesPath[id] > newPath:
                    visited[id] = 1
                    nodesPath[id] = newPath
                    nodesParent[id] = node
                    heapq.heappush(nodesHeap, (newPath, id))

        self.nodesParent = nodesParent
        self.nodesPath = nodesPath


    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        self.n = n
        self.edges = edges
        self.source = source
        self.destination = destination
        self.target = target

        self.dijkstra()

        print('self.nodesPath', self.nodesPath)
        print('self.nodesParent', self.nodesParent)

        if self.nodesPath[self.destination] > self.target:
            return []

        path = []
        parent = self.destination
        minuses = []
        while parent != -1:
            a = parent
            b = self.nodesParent[parent]
            if b != -1:
                if self.matrix[a][b] == -1:
                    minuses.append((a, b))
                    self.matrix[a][b] = 1
                    self.matrix[b][a] = 1
                    self.target -= 1
                else:
                    self.target -= self.matrix[a][b]

            path.append(parent)
            parent = self.nodesParent[parent]

        if self.target > 0 and len(minuses) == 0:
            return []

        a, b = minuses[0]
        self.matrix[a][b] += self.target
        self.matrix[b][a] += self.target

        print('path', list(reversed(path)))
        print('self.matrix', self.matrix)
        print('minuses', minuses)
        print('self.target', self.target)

        result = []
        for edge in edges:
            a, b, w = edge
            w = self.matrix[a][b] if self.matrix[a][b] > 0 else 1
            result.append([a, b, w])

        return result


def test ():
    params = [
        {
            'input': [5, [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], 0, 1, 5],
            'output': [[4,1,1],[2,0,1],[0,3,3],[4,3,1]],
        },
        {
            'input': [3, [[0,1,-1],[0,2,5]], 0, 2, 6],
            'output': [],
        },
        {
            'input': [4, [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]], 0, 2, 6],
            'output': [[1,0,4],[1,2,3],[2,3,5],[0,3,1]],
        },
        {
            'input': [5, [[1,3,10],[4,2,-1],[0,3,7],[4,0,7],[3,2,-1],[1,4,5],[2,0,8],[1,0,3],[1,2,5]], 3, 4, 11],
            'output': [[1,0,4],[1,2,3],[2,3,5],[0,3,1]],
        },
        {
            'input': [4, [[0,1,-1],[1,2,-1],[3,1,-1],[3,0,2],[0,2,5]], 2, 3, 8],
            'output': [],
        },



    ]
    solution = Solution()

    for param in params:
        n, edges, source, destination, target = param['input']
        result = solution.modifiedGraphEdges(n, edges, source, destination, target)
        print(
            'SUCCESS' if json.dumps(result) == json.dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
