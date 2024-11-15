from typing import List
from json import dumps
import heapq

class Solution:
    def largestCombination_1(self, candidates: List[int]) -> int:
        res = 1

        def rec(id, num, length):
            nonlocal res, candidates
            if id == len(candidates):
                return

            rec(id + 1, num, length)
            if num == None:
                rec(id + 1, candidates[id], 1)
            else:
                r = candidates[id] & num
                if r != 0:
                    res = max(res, length + 1)
                    rec(id + 1, r, length + 1)

        rec(0, None, 0)
        return res


    def largestCombination_2(self, candidates: List[int]) -> int:
        res = 1

        memo = [0]*32
        for cand in candidates:
            bitStr = bin(cand)[2:][::-1]
            for i in range(len(bitStr)):
                if bitStr[i] == '1':
                    memo[i] += 1
                    res = max(res, memo[i])

        return res


    def largestCombination(self, candidates: List[int]) -> int:
        memo = [0]*32
        for cand in candidates:
            for i in range(32):
                if cand & (1 << i) != 0:
                    memo[i] += 1

        return max(memo)

def test ():
    params = [
        {
            'input': [16,17,71,62,12,24,14],
            'output': 4,
        },
        {
            'input': [8,8],
            'output': 2,
        },
        {
            'input': [84,40,66,44,91,90,1,14,73,51,47,35,18,46,18,65,55,18,16,45,43,58,90,92,91,43,44,76,85,72,24,89,60,94,81,90,86,79,84,41,41,28,44],
            'output': 28,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.largestCombination(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
