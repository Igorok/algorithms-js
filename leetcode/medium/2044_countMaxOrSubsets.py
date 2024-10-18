from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOr = 0
        for n in nums:
            maxOr = maxOr | n

        res = 0
        def rec(id, acc):
            nonlocal res, nums, maxOr
            if id == len(nums):
                if acc == maxOr:
                    res += 1
                return

            rec(id + 1, acc)
            rec(id + 1, acc | nums[id])

        rec(0, 0)

        return res

def test ():
    params = [
        {
            'input': [3,1],
            'output': 2,
        },
        {
            'input': [2,2,2],
            'output': 7,
        },
        {
            'input': [3,2,1,5],
            'output': 6,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.countMaxOrSubsets(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
