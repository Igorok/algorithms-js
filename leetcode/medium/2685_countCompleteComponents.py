from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]

        for s, e in edges:
            adj[s].append(e)
            adj[e].append(s)

        componentsForNode = [0] * n
        componentNodesCount = {}

        def dfs(node, component):
            for nei in adj[node]:
                if componentsForNode[nei] == 0:
                    componentNodesCount[component] += 1
                    componentsForNode[nei] = component
                    dfs(nei, component)

        componentId = 0
        for i in range(n):
            if componentsForNode[i] == 0:
                componentId += 1
                componentNodesCount[componentId] = 1
                componentsForNode[i] = componentId
                dfs(i, componentId)

        validComponents = componentNodesCount.copy()
        for i in range(n):
            component = componentsForNode[i]
            nodes = componentNodesCount[component]
            if len(adj[i]) != (nodes-1):
                validComponents[component] = -1

        res = 0
        for c in validComponents:
            if validComponents[c] != -1:
                res += 1

        return res

'''
m*n



'''

def test ():
    params = [
        {
            'input': [6, [[0,1],[0,2],[1,2],[3,4]]],
            'output': 3,
        },
        {
            'input': [6, [[0,1],[0,2],[1,2],[3,4],[3,5]]],
            'output': 1,
        },
    ]
    solution = Solution()

    for param in params:
        n, edges = param['input']
        result = solution.countCompleteComponents(n, edges)
        correct = json.dumps(result) == json.dumps(param['output'])

        msg = 'SUCCESS' if correct else 'ERROR'
        msg += '\n'
        if not correct:
            msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()
