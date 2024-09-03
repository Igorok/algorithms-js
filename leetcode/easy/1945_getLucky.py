from typing import List

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        nums = ''
        for char in s:
            nums += str(ord(char) - 96)

        def getSumOfStr(s):
            sumOfStr = 0
            for char in s:
                sumOfStr += int(char)
            return str(sumOfStr)

        for _ in range(k):
            nums = getSumOfStr(nums)

        print('nums', nums)

        return int(nums)



def test ():
    params = [
        {
            'input': ["iiii", 1],
            'output': 36,
        },
        {
            'input': ["leetcode", 2],
            'output': 6,
        },
        {

            'input': ["zbax", 2],
            'output': 8,
        }
    ]
    solution = Solution()

    for param in params:
        s, k = param['input']
        result = solution.getLucky(s, k)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
