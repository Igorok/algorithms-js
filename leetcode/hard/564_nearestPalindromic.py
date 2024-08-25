from typing import List


class Solution:
    def getPalindrom(self, numStr, addition):
        half = ''
        palindrom = ''
        if len(numStr) % 2 == 0:
            half = numStr[0 : (len(numStr) // 2)]
            half = int(half) + addition
            half = str(half)
            palindrom = half[::-1]
        else:
            half = numStr[0 : (len(numStr) // 2) + 1]
            half = int(half) + addition
            half = str(half)
            palindrom = half[0:len(half) - 1]
            palindrom = palindrom[::-1]

        return int(half + palindrom)

    def getZero(self, numStr):
        return (10 ** len(numStr)) + 1

    def getNine(self, numStr):
        return (10 ** (len(numStr) - 1)) - 1


    def nearestPalindromic(self, n: str) -> str:
        if n == '':
            return ''

        intN = int(n)
        palindromes = [
            self.getPalindrom(n, 0),
            self.getPalindrom(n, 1),
            self.getPalindrom(n, -1),
            self.getZero(n),
            self.getNine(n),
        ]

        print(palindromes)

        result = -1
        minResult = -1
        for i in range(0, len(palindromes)):
            if palindromes[i] == intN:
                continue
            if result == -1:
                result = i
            elif abs(palindromes[i] - intN) < abs(palindromes[result] - intN):
                result = i

            if palindromes[i] < intN:
                if minResult == -1:
                    minResult = i
                elif abs(palindromes[i] - intN) < abs(palindromes[minResult] - intN):
                    minResult = i

        print(
            palindromes,
            palindromes[result],
            palindromes[minResult],
        )

        if palindromes[result] == intN or (abs(palindromes[result] - intN) == abs(palindromes[minResult] - intN)):
            return str(palindromes[minResult])

        return str(palindromes[result])

def test ():
    params = [
        {
            'input': '123',
            'output': '121',
        },
        {
            'input': '1',
            'output': '0',
        },
        {
            'input': '10',
            'output': '9',
        },
        {
            'input': '139',
            'output': '141',
        },
        {
            'input': '139',
            'output': '141',
        },
        {
            'input': '1233',
            'output': '1221',
        },
        {
            'input': '99',
            'output': '101',
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.nearestPalindromic(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
