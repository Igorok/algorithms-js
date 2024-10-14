from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    pairs += 1

        return pairs


def test ():
    params = [
        {
            'input': [1,2,3,1,1,3],
            'output': 4,
        },
        {
            'input': [1,1,1,1],
            'output': 6,
        },
        {
            'input': [1,2,3],
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.numIdenticalPairs(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
