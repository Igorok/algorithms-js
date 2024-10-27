from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        roads = set()
        matrix = [[] for i in range(n)]
        for s, e in connections:
            matrix[s].append(e)
            matrix[e].append(s)
            roads.add((s, e))

        res = 0
        visited = [-1] * n
        def mark(num):
            nonlocal res
            visited[num] = 1
            for nei in matrix[num]:
                if visited[nei] == -1:
                    if (num, nei) in roads:
                        res += 1
                    mark(nei)
        mark(0)

        return res


def test ():
    params = [
        {
            'input': [6, [[0,1],[1,3],[2,3],[4,0],[4,5]]],
            'output': 3,
        },
        {
            'input': [5, [[1,0],[1,2],[3,2],[3,4]]],
            'output': 2,
        },
    ]
    solution = Solution()

    for param in params:
        n, connections = param['input']
        result = solution.minReorder(n, connections)

        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
