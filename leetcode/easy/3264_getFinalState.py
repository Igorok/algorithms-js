from typing import List
import json
import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        numsHeap = [(nums[i], i) for i in range(len(nums))]
        heapq.heapify(numsHeap)

        res = nums.copy()

        for i in range(k):
            n, i = heapq.heappop(numsHeap)
            res[i] = n*multiplier
            heapq.heappush(numsHeap, (res[i], i))

        return res




def test ():
    params = [
        {
            'input': [ [2,1,3,5,6], 5, 2],
            'output': [8,4,6,5,6],
        },
        {
            'input': [[1,2], 3, 4],
            'output': [16,8],
        },

    ]
    solution = Solution()

    for param in params:
        nums, k, multiplier = param['input']
        result = solution.getFinalState(nums, k, multiplier)
        print(
            'SUCCESS' if json.dumps(result) == json.dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
