from typing import List
from operator import itemgetter, attrgetter

class Solution:
    def maxWidthRamp_1(self, nums: List[int]) -> int:
        width = 0

        for i in range(0, len(nums) - 1):
            end = i
            for j in range(i + 1, len(nums)):
                if nums[j] >= nums[i]:
                    end = j
            width = max(width, end - i)

        return width

    def maxWidthRamp_2(self, nums: List[int]) -> int:
        width = 0

        for i in range(0, len(nums) - 1):
            if len(nums) - 1 - i <= width:
                break
            end = i
            for j in range(len(nums) - 1, i, -1):
                if nums[j] >= nums[i]:
                    end = j
                    break
            width = max(width, end - i)

        return width


    def maxWidthRamp_2(self, nums: List[int]) -> int:
        width = 0
        solutions = []
        for i in range(0, len(nums) - 1):
            if len(nums) - 1 - i <= width:
                break
            start = i
            processed = False
            for val, end in solutions:
                if val <= nums[i]:
                    processed = True
                    break
                if end != -1:
                    start = end

            if processed:
                continue

            print(
                'i', i,
                'nums[i]', nums[i],
                'start', start,
                'nums[start]', nums[start],
            )

            for j in range(start, len(nums)):
                if nums[j] >= nums[i]:
                    start = j

            if start - i > 0:
                width = max(width, start - i)
                solutions.append((nums[i], start))
            else:
                solutions.append((nums[i], -1))

        return width

    '''
    two pointers
    l = 0
    r = i
    [20, 15, 10, 5, 11, 12, 13, 14, 15, 16, 14, 6]
    [20, 16, 16, 16, 16, 16, 16, 16, 16, 16, 14, 6]
     l
         l
                                             l
                                                 l
    '''
    def maxWidthRamp_3(self, nums: List[int]) -> int:
        rightMax = [None]*len(nums)
        rightMax[-1] = nums[-1]
        for i in range(len(nums)- 2, -1, -1):
            rightMax[i] = max(nums[i], rightMax[i + 1])

        print('rightMax', rightMax)

        width = 0
        left = 0
        for right in range(len(nums)):
            while nums[left] > rightMax[right]:
                left += 1
            width = max(width, right-left)

        return width

    # stack
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = [0]
        for i in range(1, len(nums)):
            if nums[i] < nums[stack[-1]]:
                stack.append(i)

        width = 0
        right = len(nums) - 1
        while len(stack):
            left = stack.pop()
            while nums[right] < nums[left]:
                right -= 1
            width = max(width, right - left)

        return width




def test ():
    params = [
        {
            'input': [6,0,8,2,1,5],
            'output': 4,
        },
        {
            'input': [9,8,1,0,1,9,4,0,4,1],
            'output': 7,
        },
        {
            'input': [20, 15, 10, 5, 11, 12, 13, 14, 15, 16, 14, 6],
            'output': 8,
        },

    ]
    solution = Solution()

    for param in params:
        result = solution.maxWidthRamp(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
