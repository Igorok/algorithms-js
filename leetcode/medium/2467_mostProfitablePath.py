from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def mostProfitablePath_0(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        values = amount.copy()

        adj = [[] for i in range(len(amount))]
        parent = [None]*len(amount)
        parent[0] = 0
        for s, e in edges:
            adj[s].append(e)
            adj[e].append(s)

        leafs = []
        levels = [None]*len(amount)
        levels[0] = 1
        nodesQ = deque()
        nodesQ.append((0, 1))
        while nodesQ:
            node, level = nodesQ.popleft()
            levels[node] = level
            a = 0
            for nei in adj[node]:
                if parent[nei] != None:
                    continue
                parent[nei] = node
                nodesQ.append((nei, level + 1))
                a += 1
            if a == 0:
                leafs.append(node)

        odd = bool(levels[bob] % 2)
        bobSteps = levels[bob] // 2
        if odd:
            bobSteps += 1
        def bobPath(node, steps, odd):
            if steps-1 == 0:
                values[node] = int(values[node] / 2) if odd else 0
                return
            values[node] = 0
            bobPath(parent[node], steps-1, odd)
        bobPath(bob, bobSteps, odd)

        def getRes(node, val):
            val += values[node]
            if node == 0:
                return val
            return getRes(parent[node], val)

        res = float('-inf')
        for leaf in leafs:
            res = max(res, getRes(leaf, 0))

        return res

    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)

        adj = [[] for i in range(n)]
        for s, e in edges:
            adj[s].append(e)
            adj[e].append(s)

        bobSteps = [None]*n
        bobVisited = [None]*n
        def bobWalk(node, step):
            nonlocal bobSteps, bobVisited

            bobVisited[node] = True
            if node == 0:
                bobSteps[node] = step
                return True

            for nei in adj[node]:
                if bobVisited[nei]:
                    continue
                if bobWalk(nei, step+1):
                    bobSteps[nei] = step+1
                    bobSteps[node] = step
                    return True

            return False
        bobWalk(bob, 1)

        res = float('-inf')
        aliceVisited = [None]*n
        def aliceWalk(node, step, val):
            nonlocal bobSteps, aliceVisited, res
            aliceVisited[node] = True

            if bobSteps[node] == None or bobSteps[node] > step:
                val += amount[node]
            elif bobSteps[node] == step:
                val += int(amount[node] // 2)

            a = 0
            for nei in adj[node]:
                if aliceVisited[nei]:
                    continue
                a += 1
                aliceVisited[nei] = True
                aliceWalk(nei, step + 1, val)

            if a == 0:
                res = max(res, val)

        aliceWalk(0,1,0)

        return res

'''

Alice meet Bob
Bob way is positive
Bob take more profit that other ways?
Bob way is negative
Bob take more negative?


'''

def test ():
    params = [
        {
            'input': [[[0,1],[1,2],[1,3],[3,4]], 3, [-2,4,2,-4,6]],
            'output': 6,
        },
        {
            'input': [[[0,2],[0,4],[1,3],[1,2]], 1, [3958,-9854,-8334,-9388,3410]],
            'output': -7280,
        },

        {
            'input': [[[0,1]], 1, [-7280,2350]],
            'output': -7280,
        },
    ]
    solution = Solution()

    for param in params:
        edges, bob, amount = param['input']
        result = solution.mostProfitablePath(edges, bob, amount)
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
