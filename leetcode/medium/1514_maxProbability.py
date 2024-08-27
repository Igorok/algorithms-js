from typing import List
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        nodes = [[] for _ in range(n)]
        for i in range(len(edges)):
            s, e = edges[i]
            p = succProb[i]

            nodes[s].append([e, p])
            nodes[e].append([s, p])

        print('nodes', nodes)

        h = []
        nodesPath = [-1] * n
        def _heappop():
            v = heapq.heappop(h)
            return (v[0] * -1, v[1])

        def _heappush(p, n):
            heapq.heappush(h, (-1 * p, n))

        _heappush(1, start_node)

        while len(h) != 0:
            prob, node = _heappop()
            for n, p in nodes[node]:
                if nodesPath[n] == -1 or nodesPath[n] < p * prob:
                    _heappush(p * prob, n)
                    nodesPath[n] = p * prob

        return 0 if nodesPath[end_node] == -1 else nodesPath[end_node]


def test ():
    params = [
        {
            'input': [3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2],
            'output': 0.25000,
        },
        {
            'input': [3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.3], 0, 2],
            'output': 0.30000,
        },
        {
            'input': [3, [[0,1]], [0.5], 0, 2],
            'output': 0.00000,
        },
    ]
    solution = Solution()

    for param in params:

        n, edges, succProb, start, end = param['input']
        result = solution.maxProbability(n, edges, succProb, start, end)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
