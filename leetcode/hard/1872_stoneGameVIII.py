
from typing import List
import json
from collections import Counter
from functools import cache

'''
[-1,2,-3,4,-5]
-1 2 -3 4 -5
-1 1 -2 2 -3

a = 2
b = -3
diff = 2 - -3

I should calculate a max difference between total Alice and total Bob scores.
How can I do it? I should accumulate largest score for every player, but I should return [Alice, Bob] for every recursion call and compare it.
Insted I can return just a difference between scores. It is equal to calculation total Alice - total Bob step by step.
a:5, b: 4: d:1
a:4, b: 3: d:1
5+4 - 4+3 = 2
4 - (3 - (5-4))
But I should make a loop for every Id. How can I avoid it?

The math trick here - there are no deletion of the prefix, scores do always get whole prefix sum for i, minus diff of the suffix sum.
Its like, I can take 1 or 2 or 3 stones, if I will take all stones my socres will be a prefixSum[N-1]. If I want to earn stones[i+1] I should get all prefix[i+1]
1,2,3
1 - (1+2 - (3+3 - 0)) = 4
1+2 - (3+3 - 0) = -3
1+2+3 - 0 = 6
Result for B after A is: rec(i+1) = prefix[i+1] - recursion(i+2). But because of the repeating prefix, if A will get prefix[i+1], result will be same prefix[i+1] - recursion(i+2).

'''
class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        N = len(stones)
        prefixSum = [0]*N
        prefixSum[0] = stones[0]
        for i in range(1, N):
            prefixSum[i] = prefixSum[i-1] + stones[i]


        # print('prefixSum', prefixSum)

        @cache
        def rec(id):
            if id == N-1:
                return prefixSum[N-1]
            if id >= N:
                return 0

            curr = prefixSum[id]
            opposite = rec(id+1)
            diff = curr - opposite

            return max(diff, opposite)


        return rec(1)


def test ():
    params = [
        {
            'input': [-1,2,-3,4,-5],
            'output': 5,
        },
        {
            'input': [7,-6,5,10,5,-2,-6],
            'output': 13,
        },
        {
            'input': [-10,-12],
            'output': -22,
        },
    ]
    solution = Solution()

    for param in params:
        stones = param['input']
        result = solution.stoneGameVIII(stones)
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
