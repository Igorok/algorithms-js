from typing import List

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return ''.join([str(v) for v in sorted(target)]) == ''.join([str(v) for v in sorted(arr)])


def test ():
    params = [
        {
            'input': [[1,2,3,4], [2,4,1,3]],
            'output': True,
        },
        {
            'input': [[7], [7]],
            'output': True,
        },
        {
            'input': [[3,7,9], [3,7,11]],
            'output': False,
        },
        {
            'input': [[1,2,2,3], [1,1,2,3]],
            'output': False,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.canBeEqual(param['input'][0], param['input'][1])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
