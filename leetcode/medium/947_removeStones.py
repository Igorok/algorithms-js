from typing import List

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        if len(stones) == 1:
            return 0

        adj = [[] for _ in range(len(stones))]
        for i in range(len(stones)):
            y, x = stones[i]
            for j in range(i + 1, len(stones)):
                y1, x1 = stones[j]
                if y == y1 or x == x1:
                    adj[i].append(j)
                    adj[j].append(i)

        self.removed = 0
        visited = [0] * len(stones)

        def dfs(i):
            visited[i] = 1
            self.removed += 1
            for id in adj[i]:
                if visited[id] == 0:
                    dfs(id)

        for i in range(len(stones)):
            if (visited[i] != 0):
                continue
            dfs(i)
            self.removed -= 1


        return self.removed



def test ():
    params = [
        {
            'input': [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]],
            'output': 5,
        },
        {
            'input': [[0,0],[0,2],[1,1],[2,0],[2,2]],
            'output': 3,
        },
        {
            'input': [[0,0]],
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.removeStones(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
