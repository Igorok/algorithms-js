from typing import List
import heapq
import math
from collections import defaultdict, deque

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        N = len(parents)
        adj = [[] for i in range(N)]
        for c in range(N):
            p = parents[c]
            if p == -1:
                continue
            adj[p].append(c)

        cntOfNode = [0]*N
        def getCnt(node):
            nonlocal cntOfNode
            cntOfNode[node] = 1
            for nei in adj[node]:
                cntOfNode[node] += getCnt(nei)
            return cntOfNode[node]

        getCnt(0)

        scores = defaultdict(int)
        maxScore = 0

        def getScores(node):
            nonlocal cntOfNode, scores, maxScore

            cnt = 1
            for nei in adj[node]:
                cnt *= cntOfNode[nei]

            if parents[node] != -1:
                cnt *= cntOfNode[0] - cntOfNode[node]

            scores[cnt] += 1
            maxScore = max(maxScore, cnt)

            for nei in adj[node]:
                getScores(nei)

        getScores(0)


        return scores[maxScore]


def test ():
    params = [
        {
            'input': [-1,2,0,2,0],
            'output': 3,
        },
        {
            'input': [-1,2,0],
            'output': 2,
        },
        {
            'input': [-1,3,3,5,7,6,0,0],
            'output': 2,
        },
    ]
    solution = Solution()

    for param in params:
        parents = param['input']
        result = solution.countHighestScoreNodes(parents)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
