from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)

        def countOfPairs(dist):
            l = 0
            res = 0
            for r in range(len(nums)):
                while nums[r] - nums[l] > dist:
                    l += 1
                res += r - l

            return res

        l, r = 0, nums[-1]
        while l < r:
            m = (l + r) // 2
            pairs = countOfPairs(m)
            if pairs >= k:
                r = m
            else:
                l = m + 1
        return r


def test ():
    params = [
        {
            'input': [[1,3,1], 1],
            'output': 0,
        },
        {
            'input': [[1,1,1], 2],
            'output': 0,
        },
        {
            'input': [[1,6,1], 3],
            'output': 5,
        },
    ]
    solution = Solution()

    for param in params:
        nums, k = param['input']
        result = solution.smallestDistancePair(nums, k)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

'''
[1,2,3,4,   5,6,7,8,9]
'''


if __name__ == '__main__':
    test()
