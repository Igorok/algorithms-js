from typing import List
from json import dumps

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            id = index[i]
            val = nums[i]
            if id > len(res):
                res.append(val)
            else:
                l = res[:id]
                r = res[id:]
                l.append(val)
                res = l + r
        return res



def test ():
    params = [
        {
            'input': [[0,1,2,3,4], [0,1,2,2,1]],
            'output': [0,4,1,3,2],
        },
        {
            'input': [[1,2,3,4,0], [0,1,2,3,0]],
            'output': [0,1,2,3,4],
        },
    ]
    solution = Solution()

    for param in params:
        nums, index = param['input']
        result = solution.createTargetArray(nums, index)
        print(
            'SUCCESS' if dumps(result) == dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
