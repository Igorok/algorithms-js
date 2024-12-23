from typing import List
import json
import heapq

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        res = [-1]*len(queries)

        queryById = {};
        for i, query in enumerate(queries):
            alice, bob = sorted(query)
            if alice == bob or heights[alice] < heights[bob]:
                res[i] = bob
            else:
                arr = queryById.get(bob, [])
                arr.append((max(heights[alice], heights[bob]), i))
                queryById[bob] = arr

        bobHeap = []

        for i, height in enumerate(heights):
            for q in queryById.get(i, []):
                heapq.heappush(bobHeap, q)

            while bobHeap and bobHeap[0][0] < height:
                h, id = heapq.heappop(bobHeap)
                res[id] = i

        return res

def test ():
    params = [
        {
            'input': [[6,4,8,5,2,7], [[0,1],[0,3],[2,4],[3,4],[2,2]]],
            'output': [2,5,-1,5,2],
        },
        {
            'input': [[5,3,8,2,6,1,4,6], [[0,7],[3,5],[5,2],[3,0],[1,6]]],
            'output': [7,6,-1,4,6],
        },
    ]
    solution = Solution()

    for param in params:
        heights, queries = param['input']
        result = solution.leftmostBuildingQueries(heights, queries)
        print(
            'SUCCESS' if json.dumps(result) == json.dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
