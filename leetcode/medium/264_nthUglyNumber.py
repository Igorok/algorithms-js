from typing import List

class Solution:
    def nthUglyNumber__(self, n: int) -> int:
        if n == 1:
            return 1

        ugly = 1
        allNumbers = set()
        allNumbers.add(ugly)

        for i in range(n):
            ugly = min(allNumbers)
            allNumbers.remove(ugly)

            allNumbers.add(ugly * 2)
            allNumbers.add(ugly * 3)
            allNumbers.add(ugly * 5)

        return ugly

    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1

        allNumbers = [0] * n
        allNumbers[0] = 1
        i2, i3, i5 = 0, 0, 0
        n2, n3, n5 = 2, 3, 5

        for i in range(1, n):
            allNumbers[i] = min(n2, n3, n5)

            if allNumbers[i] == n2:
               i2 += 1
               n2 = allNumbers[i2] * 2
            if allNumbers[i] == n3:
                i3 += 1
                n3 = allNumbers[i3] * 3
            if allNumbers[i] == n5:
                i5 += 1
                n5 = allNumbers[i5] * 5

        return allNumbers[n - 1]

def test ():
    params = [
        {
            'input': 10,
            'output': 12,
        },
        {
            'input': 1,
            'output': 1,
        },
        {
            'input': 11,
            'output': 15,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.nthUglyNumber(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

if __name__ == '__main__':
    test()


'''
allNumbers [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14]
ERROR input 11 output 15 result 14

'''
