from typing import List
from json import dumps
from collections import deque

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        arr = nums.copy()
        arr.sort()

        groups = [deque([arr[0]])]
        groupsByNums = {}
        groupsByNums[arr[0]] = 0

        for i in range(1, len(arr)):
            num = arr[i]
            if num - groups[-1][-1] > limit:
                groups.append(deque([num]))
            else:
                groups[-1].append(num)
            groupsByNums[num] = len(groups) - 1

        res = []
        for num in nums:
            groupId = groupsByNums[num]
            res.append(groups[groupId].popleft())

        return res


def test ():
    params = [
        {
            'input': [[1,5,3,9,8], 2],
            'output': [1,3,5,8,9],
        },
        {
            'input': [[1,7,6,18,2,1], 3],
            'output': [1,6,7,18,1,2],
        },
        {
            'input': [[1,7,28,19,10], 3],
            'output': [1,7,28,19,10],
        },
        {
            'input': [[1,60,34,84,62,56,39,76,49,38], 4],
            'output': [1,56,34,84,60,62,38,76,49,39],
        },
        {
            'input': [[4,52,38,59,71,27,31,83,88,10], 14],
            'output': [4,27,31,38,52,59,71,83,88,10],
        },
    ]
    solution = Solution()

    for param in params:
        nums, limit = param['input']

        result = solution.lexicographicallySmallestArray(nums, limit)
        print(
            'SUCCESS' if dumps(result) == dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

if __name__ == '__main__':
    test()
