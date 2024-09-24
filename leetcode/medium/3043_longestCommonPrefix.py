from typing import List
from collections import defaultdict

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        pref1 = set()
        for num in arr1:
            while num != 0:
                pref1.add(num)
                num = num // 10

        res = 0
        for num in arr2:
            while num != 0:
                if num in pref1:
                    res = max(res, len(str(num)))
                    break
                num = num // 10

        return res


'''

'''


def test ():
    params = [
        {
            'input': [[1,10,100], [1000]],
            'output': 3,
        },
        {
            'input': [[1,2,3], [4,4,4]],
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        arr1, arr2 = param['input']

        result = solution.longestCommonPrefix(arr1, arr2)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

if __name__ == '__main__':
    test()