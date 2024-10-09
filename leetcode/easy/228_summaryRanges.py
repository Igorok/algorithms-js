from typing import List
from json import dumps


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        start = nums[0]
        end = nums[0]

        def append(start, end):
            if start == end:
                res.append(str(start))
            else:
                res.append(f'{start}->{end}')

        for num in nums:
            if num == end + 1:
                end = num
            elif num > end:
                append(start, end)
                start = end = num

        append(start, end)

        return res



def test ():
    params = [
        {
            'input': [0,1,2,4,5,7],
            'output': ["0->2","4->5","7"],
        },
        {
            'input': [0,2,3,4,6,8,9],
            'output': ["0","2->4","6","8->9"],
        },

    ]
    solution = Solution()

    for param in params:
        result = solution.summaryRanges(param['input'])
        print(
            'SUCCESS' if dumps(result) == dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
