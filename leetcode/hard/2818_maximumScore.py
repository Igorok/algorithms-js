from typing import List
import json
from collections import deque, defaultdict
import heapq
import math



class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        mod = int(7 + 10e8)

        def getPrimeFactor(num):
            count = 0
            right = int(math.sqrt(num)) + 1
            for i in range(2, right):
                if num % i == 0:
                    count += 1
                while num % i == 0:
                    num = num // i

            if num >= 2:
                count += 1

            return count

        getPrimeFactors = [getPrimeFactor(num) for num in nums]

        length = len(nums)
        leftBorder = [-1] * length
        rightBorder = [length] * length

        stack = []
        for i in range(length):
            while stack and getPrimeFactors[stack[-1]] < getPrimeFactors[i]:
                id = stack.pop()
                rightBorder[id] = i
            if stack:
                leftBorder[i] = stack[-1]
            stack.append(i)

        primeHeap = []
        for i in range(length):
            heapq.heappush(primeHeap, (-nums[i], i))

        res = 1
        while k > 0 and primeHeap:
            num, id = heapq.heappop(primeHeap)
            num = -num

            starts = id - leftBorder[id]
            ends = rightBorder[id] - id
            possible = starts * ends

            real = min(k, possible)
            k -= real
            r = pow(num, real, mod)
            res *= r
            res %= mod

        return res


'''

19,12,14,6,10,18

1 2 2 2 2 2
0 0 1 2 3 4
1 6 6 6 6 6

[3289,2832,14858,22011]
3 3 4 4
0 1 0 3
2 2 4 4

22011*14858*14858*14858*14858*3289


m = 7+10e8
n = [22011,14858,14858,14858,14858,14858].reduce((acc, num) => {
    acc = acc*num
    acc = acc % m
    return acc;
}, 1);
console.log('n', n);



'''



def test ():
    params = [
        {
            'input': [[3289,2832,14858,22011], 6],
            'output': 256720975,
        },
        {
            'input': [[19,12,14,6,10,18], 3],
            'output': 4788,
        },


        {
            'input': [[8,3,9,3,8], 2],
            'output': 81,
        },


    ]
    solution = Solution()

    for param in params:
        nums, k = param['input']
        result = solution.maximumScore(nums, k)
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
