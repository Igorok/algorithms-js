import sys
sys.setrecursionlimit(1500)
from typing import List
import json
from collections import deque, defaultdict
import heapq

class Solution:
    def kSmallestPairs_0(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        arr1 = sorted(nums1)
        arr2 = sorted(nums2)
        n = len(arr1)
        m = len(arr2)

        res = []
        i1 = 0
        i2 = 0
        while len(res) < k:
            if i1 + 1 == n or arr1[i1] + arr2[i2] <= arr1[i1+1] + arr2[0]:
                res.append((arr1[i1], arr2[i2]))
                i2 += 1
                if i2 == m:
                    break
            else:
                i1 += 1
                i2 = 0

        return res

    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:


        return []

'''

[1,2,4,5,6]
[3,5,7,9]

'''


def test ():
    params = [
        {
            'input': [[1,7,11], [2,4,6], 3],
            'output': [[1,2],[1,4],[1,6]],
        },
        {
            'input': [[1,1,2], [1,2,3], 2],
            'output': [[1,1],[1,1]],
        },
        {
            'input': [[1,2,4,5,6], [3,5,7,9], 3],
            'output': [[1,3],[2,3],[1,5]],
        },
    ]
    solution = Solution()

    for param in params:
        nums1, nums2, k = param['input']
        result = solution.kSmallestPairs(nums1, nums2, k)
        correct = json.dumps(result) == json.dumps(param['output'])

        msg = 'SUCCESS' if json.dumps(result) == json.dumps(param['output']) else 'ERROR'
        msg += '\n'
        if not correct:
            msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()
