from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        uniq = []
        count = {}

        for num in nums:
            if not num in count:
                count[num] = 1
                uniq.append(num)
            else:
                count[num] += 1

        uniq.sort()

        cache = {}
        def rec(id):
            if id >= len(uniq):
                return 0

            if id in cache:
                return cache[id]

            #1
            s1 = uniq[id] * count[uniq[id]]
            if id+1 < len(uniq):
                if uniq[id+1] == uniq[id] + 1:
                    s1 += rec(id+2)
                else:
                    s1 += rec(id+1)
            #2
            s2 = rec(id+1)

            cache[id] = max(s1, s2)

            return cache[id]

        return rec(0)

'''

2 3 4

2 0 4
0 3 0

---


'''



def test ():
    params = [
        {
            'input': [3,4,2],
            'output': 6,
        },
        {
            'input': [2,2,3,3,3,4],
            'output': 9,
        },
    ]
    solution = Solution()

    for param in params:
        nums = param['input']
        result = solution.deleteAndEarn(nums)
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
