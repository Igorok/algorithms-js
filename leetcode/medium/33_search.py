from typing import List
import json
from collections import deque

class Solution:
    def search_0(self, nums: List[int], target: int) -> int:
        n = len(nums)
        def getSorted():
            if nums[0] <= nums[-1]:
                return [[], nums]

            start = 0
            end = n-1

            while start <= end:
                m = (start + end) // 2
                if m+1 != n and nums[m] > nums[m+1]:
                    return [nums[:m+1], nums[m+1:]]

                if m-1 != -1 and nums[m] < nums[m-1]:
                    return [nums[:m], nums[m:]]

                if nums[m] > nums[0]:
                    start += 1
                    continue
                if nums[m] < nums[0]:
                    end -= 1

            return [[], nums]

        def binSearch(arr):
            if len(arr) == 0:
                return -1

            start = 0
            end = len(arr) - 1
            while start <= end:
                m = (start + end) // 2
                if arr[m] == target:
                    return m
                if arr[m] > target:
                    end -= 1
                else:
                    start += 1

            return -1


        left, right = getSorted()
        leftR = binSearch(left)
        if leftR != -1:
            return leftR
        rightR = binSearch(right)
        if rightR != -1:
            return len(left) + rightR

        return -1

    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def getPivot():
            if nums[0] <= nums[-1]:
                return -1

            start = 0
            end = n-1

            while start <= end:
                m = (start + end) // 2
                if m+1 != n and nums[m] > nums[m+1]:
                    return m+1

                if m-1 != -1 and nums[m] < nums[m-1]:
                    return m

                if nums[m] > nums[0]:
                    start += 1
                    continue
                if nums[m] < nums[0]:
                    end -= 1

            return -1

        def binSearch(s, e):
            if s == e:
                return s if nums[s] == target else -1

            start = s
            end = e
            while start <= end:
                m = (start + end) // 2
                if nums[m] == target:
                    return m
                if nums[m] > target:
                    end -= 1
                else:
                    start += 1

            return -1


        pivot = getPivot()
        if pivot == -1:
            return binSearch(0, n-1)

        leftR = binSearch(0, pivot-1)
        if leftR != -1:
            return leftR
        rightR = binSearch(pivot, n-1)
        if rightR != -1:
            return rightR

        return -1


def test ():
    params = [
        {
            'input': [[6,7,8,9,10,1,2,3,4,5], 3],
            'output': 7,
        },
        {
            'input': [[4,5,6,7,0,1,2], 0],
            'output': 4,
        },
        {
            'input': [[4,5,6,7,0,1,2], 3],
            'output': -1,
        },
        {
            'input': [[1], 0],
            'output': -1,
        },
        {
            'input': [[3, 1], 0],
            'output': -1,
        },
        {
            'input': [[1], 1],
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        nums, target = param['input']
        result = solution.search(nums, target)
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
