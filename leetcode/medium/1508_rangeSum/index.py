from typing import List

class Solution:
    def mod (self, num):
        m = 10e9 + 7
        return num % m

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        resultList = []

        for i in range(len(nums)):
            acc = self.mod(nums[i])
            resultList.append(acc)
            for j in range(i + 1, len(nums)):
                acc = self.mod(acc + nums[j])
                resultList.append(acc)

        s = 0
        for v in sorted(sorted(resultList)[left - 1: right]):
            s = self.mod(s + v)

        return int(s)

# [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]
#
# '2, 3, 3, 4, 5'.replace(/\,/g, '+')

def test ():
    params = [
        {
            'input': [[1, 2, 3, 4], 4, 1, 5],
            'output': 13,
        },
        {
            'input': [[1,2,3,4], 4, 3, 4],
            'output': 6,
        },
        {
            'input': [[1,2,3,4], 4, 1, 10],
            'output': 50,
        },



    ]
    solution = Solution()

    for param in params:
        nums, n, left, right = param['input']
        result = solution.rangeSum(nums, n, left, right)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
