from typing import List

class Solution:
    def productExceptSelf_(self, nums: List[int]) -> List[int]:
        multiply = 1
        zero = 0
        for val in nums:
            if val == 0:
                zero += 1
                continue
            if zero > 1:
                multiply = 0
                break
            multiply *= val

        if (zero > 1):
            return [0] * len(nums)

        if zero == 1:
            return [
                multiply if v == 0 else 0
                for v in nums
            ]

        return [ int(multiply / v) for v in nums ]


    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        result = [0] * len(nums)

        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i]

        postfix[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i]

        result[0] = postfix[1]
        result[-1] = prefix[-2]
        for i in range(1, len(nums) - 1):
            result[i] = prefix[i - 1] * postfix[i + 1]

        print(
            'prefix', prefix,
            'postfix', postfix,
        )

        return result
'''

[1,2,3,4]
[24,12,8,6]

1  2  3 4
24 12 8 6

1  2  3 4
1  2  6 24
---


2  3  4  5
2  6  24 120
60 40 30 24
'''

def test ():
    params = [
        {
            'input': [1,2,3,4],
            'output': [24,12,8,6],
        },
        {
            'input': [-1,1,0,-3,3],
            'output': [0,0,9,0,0],
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.productExceptSelf(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
