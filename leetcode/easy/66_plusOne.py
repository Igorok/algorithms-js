from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        remainder = 1
        N = len(digits)

        for i in range(N-1, -1, -1):
            num = digits[i]
            remainder += num
            res.append(remainder % 10)
            remainder = remainder // 10

        while remainder > 0:
            res.append(remainder % 10)
            remainder = remainder // 10

        res.reverse()
        return res

def test ():
    params = [
        {
            'input': [1,2,3],
            'output': [1,2,4],
        },
        {
            'input': [4,3,2,1],
            'output': [4,3,2,2],
        },
        {
            'input': [9],
            'output': [1,0],
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.plusOne(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
