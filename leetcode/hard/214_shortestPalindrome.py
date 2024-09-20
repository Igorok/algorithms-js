from typing import List

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def isPalindrome(start, end):
            subStr = s[start:end + 1]
            rem = subStr[::-1]
            return rem == subStr

        end = 0
        for i in reversed(range(len(s))):
            isp = isPalindrome(0, i)
            if isp:
                end = i
                break

        if end == len(s) - 1:
            return s

        remainder = s[(end+1):]
        remainder = remainder[::-1]

        return remainder + s



def test ():
    params = [
        {
            'input': 'aacecaaa',
            'output': 'aaacecaaa',
        },
        {
            'input': 'abcd',
            'output': 'dcbabcd',
        },
        {
            'input': 'aba',
            'output': 'aba',
        },
        {
            'input': 'a',
            'output': 'a',
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.shortestPalindrome(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

if __name__ == '__main__':
    test()
