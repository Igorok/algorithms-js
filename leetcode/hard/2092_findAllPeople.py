import json
from collections import defaultdict, deque
from typing import List
import heapq


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        adj = [[] for i in range(n)]
        for pers1, pers2, time in meetings:
            adj[pers1].append((pers2, time))
            adj[pers2].append((pers1, time))


        visited = {}
        meetQueue = [(0,0), (0, firstPerson)]
        heapq.heapify(meetQueue)

        while meetQueue:
            time, node = heapq.heappop(meetQueue)

            if visited.get(node, float('inf')) <= time:
                continue

            visited[node] = time

            for _nei, _time in adj[node]:
                if _time < visited[node]:
                    continue
                if _nei in visited and visited[_nei] <= visited[node]:
                    continue

                heapq.heappush(meetQueue, (_time, _nei))


        return list(visited.keys())


'''

[4, [[3,1,3],[1,2,2],[0,3,3]], 3]

[
[1,2,2], [0,3,3], [3,1,3]
]


'''


def test():
    params = [
        {
            "input": [6, [[1,2,5],[2,3,8],[1,5,10]], 1],
            "output": [0,1,2,3,5],
        },
        {
            "input": [4, [[3,1,3],[1,2,2],[0,3,3]], 3],
            "output": [0,1,3],
        },
        {
            "input": [5, [[3,4,2],[1,2,1],[2,3,1]], 1],
            "output": [0,1,2,3,4],
        },
    ]
    solution = Solution()

    for param in params:
        n, meetings, firstPerson = param["input"]
        result = solution.findAllPeople(n, meetings, firstPerson)
        correct = json.dumps(result) == json.dumps(param["output"])

        msg = "SUCCESS" if correct else "ERROR"
        msg += "\n"
        if not correct:
            msg += "input " + json.dumps(param["input"]) + "\n"
            msg += "output " + json.dumps(param["output"]) + "\n"
            msg += "result " + json.dumps(result) + "\n"

        print(msg)


if __name__ == "__main__":
    test()
