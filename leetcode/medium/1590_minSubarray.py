from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        idsByRemainder = {0: -1}
        rem = sum(nums) % p
        if rem == 0:
            return 0

        length = len(nums)
        sumRem = 0
        for i in range(len(nums)):
            sumRem = (sumRem + nums[i]) % p
            idsByRemainder[sumRem] = i
            r =(sumRem - rem + p) % p
            if r not in idsByRemainder:
                continue

            l = i - idsByRemainder[r]
            length = min(length, l)

        print('idsByRemainder', idsByRemainder)

        return -1 if length == len(nums) else length

'''

3,1,4,2

x,1,4,2
x,x,x,x

3,x,x,x
3,1,x,2
'''

def test ():
    params = [
        {
            'input': [[3,1,4,2], 6],
            'output': 1,
        },
        {
            'input': [[4,1,3,2], 6],
            'output': 1,
        },
        {
            'input': [[3,1,2,4], 6],
            'output': 1,
        },
        {
            'input': [[6,3,5,2], 9],
            'output': 2,
        },
        {
            'input': [[1,2,3], 3],
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        nums, p = param['input']
        result = solution.minSubarray(nums, p)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
