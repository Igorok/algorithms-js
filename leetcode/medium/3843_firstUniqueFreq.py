from typing import List
from json import dumps
from collections import deque
import heapq

class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        N = len(nums)
        freqByNum = {}
        numByFreq = {}
        idByNum = {}

        for i in range(N):
            num = nums[i]
            if num not in idByNum:
                idByNum[num] = i

            cnt = freqByNum.get(num, 0)
            if cnt != 0:
                numByFreq[cnt].remove(num)

            cnt += 1
            freqByNum[num] = cnt
            numByFreq[cnt] = numByFreq.get(cnt, set())
            numByFreq[cnt].add(num)

        res = -1

        for arr in numByFreq.values():
            if len(arr) != 1:
                continue
            for num in arr:
                if res == -1 or idByNum[num] < idByNum[res]:
                    res = num

        return res

def test ():
    params = [
        {
            'input': [20,10,30,30],
            'output': 30,
        },
        {
            'input': [20,20,10,30,30,30],
            'output': 20,
        },
        {
            'input': [10,10,20,20],
            'output': -1,
        },
    ]
    solution = Solution()

    for param in params:
        nums = param['input']
        result = solution.firstUniqueFreq(nums)

        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            # 'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
