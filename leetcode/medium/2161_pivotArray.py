from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def pivotArray_0(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        middle = []
        right = []

        for num in nums:
            if num < pivot:
                left.append(num)
            elif num == pivot:
                middle.append(num)
            else:
                right.append(num)

        return left + middle + right

    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        res = [0]*n

        l = lId = 0
        r = rId = n - 1

        while l < n and r > -1:
            if nums[l] < pivot:
                res[lId] = nums[l]
                lId += 1
            if nums[r] > pivot:
                res[rId] = nums[r]
                rId -= 1
            l += 1
            r -= 1

        while lId <= rId:
            res[lId] = pivot
            lId += 1

        return res


def test ():
    params = [
        {
            'input': [[9,12,5,10,14,3,10], 10],
            'output': [9,5,3,10,10,12,14],
        },
        {
            'input': [[-3,4,3,2], 2],
            'output': [-3,2,4,3],
        },
    ]
    solution = Solution()

    for param in params:
        nums, pivot = param['input']
        result = solution.pivotArray(nums, pivot)
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
