from typing import List

class Solution:
    def increasingTriplet_(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        for i in range(1, len(nums) - 1):
            less = False
            great = False
            for l in range(0, i):
                if nums[l] < nums[i]:
                    less = True
                    break
            for g in range(i + 1, len(nums)):
                if nums[g] > nums[i]:
                    great = True
                    break

            if less and great:
                return True

        return False

    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        n1 = nums[0]
        n2 = None
        n3 = None

        for i in range(1, len(nums)):
            if nums[i] < n1:
                n1 = nums[i]

            if nums[i] > n1:
                if n2 is None:
                    n2 = nums[i]
                    continue
                if nums[i] > n2:
                    n3 = nums[i]
                    return True

                n2 = nums[i]
                continue

        return False


def test ():
    params = [
        {
            'input': [1,2,3,4,5],
            'output': True,
        },
        {
            'input': [5,4,3,2,1],
            'output': False,
        },
        {
            'input': [2,1,5,0,4,6],
            'output': True,
        },
        {
            'input': [100, 110, 91, 92, 11, 12, 13, 1, 2],
            'output': True,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.increasingTriplet(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
