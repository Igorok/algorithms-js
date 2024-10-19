from typing import List
from json import dumps

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        count = 0
        data = [v*k for v in nums2]

        for num in nums1:
            for d in data:
                if d != 0 and num % d == 0:
                    count += 1

        return count


def test ():
    params = [
        {
            'input': [[1,3,4], [1,3,4], 1],
            'output': 5,
        },
        {
            'input': [[1,2,4,12], [2,4], 3],
            'output': 2,
        },
    ]
    solution = Solution()

    for param in params:
        nums1, nums2, k = param['input']
        result = solution.numberOfPairs(nums1, nums2, k)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
