from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0

        for num in nums:
            if num % 3 == 0:
                continue

            left = num
            right = num
            i = 0
            while left % 3 != 0 and right % 3 != 0:
                left -= 1
                right += 1
                i =+ 1
            operations += i

        return operations


def test ():
    params = [
        {
            'input': [1,2,3,4],
            'output': 3,
        },
        {
            'input': [3,6,9],
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.minimumOperations(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
