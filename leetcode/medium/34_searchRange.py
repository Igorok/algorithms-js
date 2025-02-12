from typing import List
from json import dumps
import heapq
from collections import deque


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        small = float('inf')
        big = -1

        def searchLeft(start, end):
            nonlocal small, big, target

            while start <= end:
                m = (start + end) // 2
                if nums[m] == target:
                    small = min(small, m)
                    end = m - 1
                elif nums[m] < target:
                    start = m + 1
                else:
                    break

        def searchRight(start, end):
            nonlocal small, big, target

            while start <= end:
                m = (start + end) // 2
                if nums[m] == target:
                    big = max(small, m)
                    start = m + 1
                elif nums[m] > target:
                    end = m - 1
                else:
                    break

        def search(start, end):
            nonlocal small, big, target

            while start <= end:
                m = (start + end) // 2
                if nums[m] == target:
                    small = big = m
                    searchLeft(0, m-1)
                    searchRight(m+1, len(nums) - 1)
                    return
                elif nums[m] > target:
                    end = m - 1
                else:
                    start = m + 1

        search(0, len(nums)-1)

        return [-1, -1] if big == -1 else [small, big]

def test ():
    params = [
        {
            'input': [[5,7,7,8,8,10], 8],
            'output': [3,4],
        },
        {
            'input': [[5,7,7,8,8,10], 6],
            'output': [-1,-1],
        },
        {
            'input': [[], 0],
            'output': [-1,-1],
        },
    ]
    solution = Solution()

    for param in params:
        nums, target = param['input']
        result = solution.searchRange(nums, target)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

if __name__ == '__main__':
    test()
