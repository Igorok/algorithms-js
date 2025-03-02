from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = []

        n = len(nums1)
        m = len(nums2)
        i1 = i2 = 0

        while i1 < n and i2 < m:
            if nums1[i1][0] == nums2[i2][0]:
                res.append([nums1[i1][0], nums1[i1][1] + nums2[i2][1]])
                i1 += 1
                i2 += 1
            elif nums1[i1][0] > nums2[i2][0]:
                res.append(nums2[i2])
                i2 += 1
            else:
                res.append(nums1[i1])
                i1 += 1

        for i in range(i1, n):
            res.append(nums1[i])

        for i in range(i2, m):
            res.append(nums2[i])

        return res

'''

1 5 10 11
2 3 4 5 12 100

1

'''


def test ():
    params = [
        {
            'input': [
                [[2,4],[3,6],[5,5]],
                [[1,3],[4,3]]
            ],
            'output': [[1,3],[2,4],[3,6],[4,3],[5,5]],
        },

        {
            'input': [
                [[1,2],[2,3],[4,5]],
                [[1,4],[3,2],[4,1]]
            ],
            'output': [[1,6],[2,3],[3,2],[4,6]],
        },

    ]
    solution = Solution()

    for param in params:
        nums1, nums2 = param['input']
        result = solution.mergeArrays(nums1, nums2)
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
