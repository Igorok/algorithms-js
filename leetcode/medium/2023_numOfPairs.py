from typing import List
import json
from collections import deque, defaultdict
import heapq
from functools import lru_cache


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        n = len(nums)
        length = len(target)
        countOfStr = {}

        for num in nums:
            countOfStr[num] = countOfStr.get(num, 0) + 1

        res = 0
        for key in countOfStr:
            l = len(key)
            if l >= length:
                continue

            if key == target[:l]:
                remainder = target[l:]
                if remainder == key:
                    if countOfStr[key] > 1:
                        res += countOfStr[key] * (countOfStr[key]-1)
                elif remainder in countOfStr:
                    res += countOfStr[key] * countOfStr[remainder]

        return res

'''

111_111

111_22

'''

def test ():
    params = [
        {
            'input': [["777","7","77","77"], "7777"],
            'output': 4,
        },
        {
            'input': [["123","4","12","34"], "1234"],
            'output': 2,
        },
        {
            'input': [["1","1","1"], "11"],
            'output': 6,
        },
        {
            'input': [["1","111"], "11"],
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        nums, target = param['input']
        result = solution.numOfPairs(nums, target)
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
