from typing import List
import heapq
import math

class Solution:
    def findScore(self, nums: List[int]) -> int:
        length = len(nums)
        score = 0
        marks = [0]*length
        numsHeap = [(nums[i], i) for i in range(length)]
        heapq.heapify(numsHeap)

        while numsHeap:
            num, id = heapq.heappop(numsHeap)
            if marks[id] != 0:
                continue
            score += num
            marks[id] = 1
            if id != 0:
                marks[id - 1] = 1
            if id != length - 1:
                marks[id + 1] = 1

        return score

def test ():
    params = [
        {
            'input': [2,1,3,4,5,2],
            'output': 7,
        },
        {
            'input': [2,3,5,1,3,2],
            'output': 5,
        },

    ]
    solution = Solution()

    for param in params:
        result = solution.findScore(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
