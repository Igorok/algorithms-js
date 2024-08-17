from typing import List

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minVal = 10e5
        maxVal = -10e5
        diff = -10e5

        for arr in arrays:
            diff = max(arr[-1] - minVal, diff)
            diff = max(maxVal - arr[0], diff)
            minVal = min(minVal, arr[0])
            maxVal = max(maxVal, arr[-1])

        return diff


def test ():
    params = [
        {
            'input': [[1,2,3],[4,5],[1,2,3]],
            'output': 4,
        },
        {
            'input': [[1],[1]],
            'output': 0,
        },
        {
            'input': [[1,4],[0,5]],
            'output': 4,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.maxDistance(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
