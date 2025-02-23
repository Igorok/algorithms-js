from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def largestRectangleArea_0(self, heights: List[int]) -> int:
        n = len(heights)
        res = 0
        nums = {}

        for i in range(n):
            arr = nums.get(heights[i], [])
            if arr and arr[-1][1] >= i:
                continue

            l = r = i
            for j in range(i-1, -1, -1):
                if heights[j]<heights[i]:
                    break
                l=j

            for j in range(i+1, n):
                if heights[j]<heights[i]:
                    break
                r=j
            diff=r-l+1

            arr.append([l, r])
            nums[heights[i]] = arr

            res = max(res, diff*heights[i])

        return res


    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []

        for i in range(len(heights)):
            height = heights[i]
            start = i
            while stack and stack[-1][0] >= height:
                h, id = stack.pop()
                r = (i-id)*h
                res = max(res, r)
                start = id

            if start != i:
                stack.append([height, start])
            stack.append([height, i])


        for height, id in stack:
            diff = stack[-1][1] - id + 1
            r = diff * height
            res = max(res, r)


        return res

'''

2 1 3 4 1 1 1 1 1 1
1 2 1 1
2 2 3 4


'''


def test ():
    params = [
        {
            'input': [5,5,1,7,1,1,5,2,7,6],
            'output': 12,
        },
        {
            'input': [1,1,1,1,1],
            'output': 5,
        },
        {
            'input': [3,6,5,7,4,8,1,0],
            'output': 20,
        },
        {
            'input': [4,2,0,3,2,5],
            'output': 6,
        },
        {
            'input': [2,1,4,5,1,3,3],
            'output': 8,
        },
        {
            'input': [2,1,5,6,2,3],
            'output': 10,
        },
        {
            'input': [2,4],
            'output': 4,
        },
        {
            'input': [2,1,3,4,1,1],
            'output': 6,
        },
        {
            'input': [2,1,3,4,1,],
            'output': 6,
        },

    ]
    solution = Solution()

    for param in params:
        result = solution.largestRectangleArea(param['input'])
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
