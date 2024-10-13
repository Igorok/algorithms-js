from typing import List
from json import dumps


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        data = sorted(nums.copy())

        pos = {}
        for i in range(len(data)):
            num = data[i]
            if not num in pos:
                pos[num] = i

        return [pos[v] for v in nums]


def test ():
    params = [
        {
            'input': [8,1,2,2,3],
            'output': [4,0,1,1,3],
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.smallerNumbersThanCurrent(param['input'])
        print(
            'SUCCESS' if dumps(result) == dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
