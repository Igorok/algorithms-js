from typing import List
import json
from collections import deque, defaultdict
import heapq

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        N = len(s)
        prevCnt = 0
        currCnt = 1
        left = 0


        res = 0
        for right in range(1, N):
            if s[right] == s[left]:
                currCnt += 1
                continue

            res += min(prevCnt, currCnt)
            prevCnt = currCnt
            currCnt = 1
            left = right

        res += min(prevCnt, currCnt)

        return res





def test ():
    params = [
        {
            'input': '00110011',
            'output': 6,
        },
        {
            'input': '10101',
            'output': 4,
        },
    ]
    solution = Solution()

    for param in params:
        s = param['input']
        result = solution.countBinarySubstrings(s)
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
