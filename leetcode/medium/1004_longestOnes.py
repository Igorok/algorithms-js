from typing import List

class Solution:
    def longestOnes_1(self, nums: List[int], k: int) -> int:
        res = 0

        start = 0
        end = 0
        limit = k

        while end < len(nums):
            if nums[end] == 0:
                if limit != 0:
                    limit -= 1
                else:
                    res = max(res, end - start)
                    start = start + 1
                    limit = k
                    end = start
                    continue
            end += 1

        res = max(res, end - start)

        return res

    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        start = 0
        end = 0
        limit = k

        stack = []

        while end < len(nums):
            if nums[end] == 0:
                stack.append(end)
                if limit != 0:
                    limit -= 1
                else:
                    res = max(res, end - start)
                    start = stack[-(k+1)] + 1
            end += 1
            if end == len(nums):
                res = max(res, end - start)

        return res


def test ():
    params = [
        {
            'input': [[1,1,1,0,0,0,1,1,1,1,0], 2],
            'output': 6,
        },
        {
            'input': [[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3],
            'output': 10,
        },
        {
            'input': [[0,0,0,1], 4],
            'output': 4,
        },
    ]
    solution = Solution()

    for param in params:
        nums, k = param['input']
        result = solution.longestOnes(nums, k)

        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
