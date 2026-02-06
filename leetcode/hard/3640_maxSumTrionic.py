from typing import List
import json
import heapq

class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        N = len(nums)

        increase = {}
        decrease = {}

        status = 0
        start = -1
        totalSum = 0
        maxBottom = 0
        maxTop = 0

        for i in range(N):
            if i == 0:
                if nums[i] == nums[i+1]:
                    continue

                status = 1 if nums[i] < nums[i+1] else 2

                start = i
                totalSum = nums[i]
                if status == 1:
                    maxBottom = nums[i] + nums[i+1]
                    maxTop = nums[i]
                continue

            if i == N-1:
                if status == 0:
                    continue
                if status == 1:
                    totalSum += nums[i]
                    maxBottom = max(maxBottom, totalSum)
                    maxTop += nums[i]
                    increase[start] = {
                        's': start,
                        'e': i,
                        't': totalSum,
                        'mb': maxBottom,
                        'mt': maxTop,
                    }
                elif status == 2:
                    totalSum += nums[i]
                    decrease[start] = {
                        's': start,
                        'e': i,
                        't': totalSum,
                    }
                continue

            if nums[i] == nums[i+1]:
                if status == 1:
                    totalSum += nums[i]
                    maxBottom = max(maxBottom, totalSum)
                    maxTop += nums[i]
                    increase[start] = {
                        's': start,
                        'e': i,
                        't': totalSum,
                        'mb': maxBottom,
                        'mt': maxTop,
                    }
                elif status == 2:
                    totalSum += nums[i]
                    decrease[start] = {
                        's': start,
                        'e': i,
                        't': totalSum,
                    }
                status = 0
                totalSum = maxBottom = maxTop = 0
                continue

            if nums[i] > nums[i+1]:
                if status == 0:
                    status = 2
                    start = i
                    totalSum = nums[i]
                elif status == 1:
                    totalSum += nums[i]
                    maxBottom = max(maxBottom, totalSum)
                    maxTop += nums[i]
                    increase[start] = {
                        's': start,
                        'e': i,
                        't': totalSum,
                        'mb': maxBottom,
                        'mt': maxTop,
                    }
                    status = 2
                    start = i
                    totalSum = nums[i]
                elif status == 2:
                    totalSum += nums[i]

            if nums[i] < nums[i+1]:
                if status == 0:
                    status = 1
                    start = i
                    totalSum = maxTop = nums[i]
                    maxBottom = nums[i] + nums[i+1]
                elif status == 1:
                    totalSum += nums[i]
                    maxBottom = max(maxBottom, totalSum)
                    maxTop = nums[i] if nums[i] >= maxTop + nums[i] else maxTop + nums[i]
                elif status == 2:
                    totalSum += nums[i]
                    decrease[start] = {
                        's': start,
                        'e': i,
                        't': totalSum,
                    }
                    status = 1
                    start = i
                    totalSum = maxTop = nums[i]
                    maxBottom = nums[i] + nums[i+1]



        # print(
        #     'increase', increase,
        #     'decrease', decrease,
        # )

        res = float('-inf')

        for start in increase:
            inc1 = increase[start]

            if inc1['e'] not in decrease:
                continue

            dec = decrease[inc1['e']]

            if dec['e'] not in increase:
                continue

            inc2 = increase[dec['e']]

            part1 = inc1['mt']
            part2 = dec['t']
            part3 = inc2['mb']

            r = part1 + part2 + part3 - nums[dec['s']] - nums[dec['e']]

            res = max(res, r)


        return res

'''
0   1   2   3  4  5   6
0, -2, -1, -3, 0, 2, -1
increase
{
1: {'s': 1, 'e': 2, 't': -3, 'm': -1},
3: {'s': 3, 'e': 5, 't': -1, 'm': 2}}
decrease {
0: {'s': 0, 'e': 1, 't': -2},
2: {'s': 2, 'e': 3, 't': -4},
5: {'s': 5, 'e': 6, 't': 1}}
ERROR input [0, -2, -1, -3, 0, 2, -1] output -4 result 0

increase
{
0: {'s': 0, 'e': 1, 't': 5, 'm': 5},
2: {'s': 2, 'e': 3, 't': 9, 'm': 9}}
decrease
{
1: {'s': 1, 'e': 2, 't': 6}}
ERROR input [1, 4, 2, 7] output 14 result 0

increase
{
0: {'s': 0, 'e': 5, 't': -15, 'm': 0},
7: {'s': 7, 'e': 10, 't': 1, 'm': 3}}
decrease
{
5: {'s': 5, 'e': 7, 't': -3}}
ERROR input [-5, -4, -3, -2, -1, 0, -1, -2, 0, 1, 2] output -1 result 0

-2,-1; -1
-1;-3; -4
-3;0;2;-1

'''

def test ():
    params = [
        {
            'input': [0,-2,-1,-3,0,2,-1],
            'output': -4,
        },
        {
            'input': [1,4,2,7],
            'output': 14,
        },
        {
            'input': [-5,-4,-3,-2,-1,0,-1,-2,0,1,2],
            'output': -1,
        },
        {
            'input': [467,941,-696,-288],
            'output': 424,
        },
    ]
    solution = Solution()

    for param in params:
        nums = param['input']
        result = solution.maxSumTrionic(nums)
        print(
            'SUCCESS' if json.dumps(result) == json.dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
