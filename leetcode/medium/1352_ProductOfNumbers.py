import sys
sys.setrecursionlimit(1500)
from typing import List
import json
from collections import deque, defaultdict
import heapq

class ProductOfNumbers_0:

    def __init__(self):
        self._nums = []

    def add(self, num: int) -> None:
        self._nums.append(num)


    def getProduct(self, k: int) -> int:
        n = len(self._nums)
        m = 1
        for i in range(n - 1, n - k - 1, -1):
            if self._nums[i] == 0:
                return 0
            m *= self._nums[i]

        return m



class ProductOfNumbers:

    def __init__(self):
        self._multiplies = []
        self._zero = -1

    def add(self, num: int) -> None:
        if num == 0:
            self._zero = len(self._multiplies)

        if len(self._multiplies) == 0 or self._multiplies[-1] == 0 and num != 0:
            self._multiplies.append(num)
        else:
            self._multiplies.append(self._multiplies[-1] * num)

    def getProduct(self, k: int) -> int:
        kId = len(self._multiplies) - k
        if self._zero >= kId:
            return 0
        if kId == 0 or self._multiplies[kId-1] == 0:
            return self._multiplies[-1]
        else:
            return self._multiplies[-1] // self._multiplies[kId-1]



# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

'''

1 2 3 4

1 2 3 4 5 6 7 8 9

1 2 6 24 120
  2 6 24 120
    3 12  60
       4  20
'''


def test ():
    params = [
        {
            'input': [[1,7,11], [2,4,6], 3],
            'output': [[1,2],[1,4],[1,6]],
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
