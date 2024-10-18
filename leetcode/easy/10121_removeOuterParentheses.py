from typing import List

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ''

        l = 0
        start = 0
        for i in range(len(s)):
            char = s[i]
            if char == '(':
                if l == 0:
                    start = i
                l += 1
            else:
                l -= 1
                if l == 0:
                    res += s[start+1:i]
                    start = 0

        return res

def test ():
    params = [
        {
            'input': '(()())(())',
            'output': '()()()',
        },
        {
            'input': '(()())(())(()(()))',
            'output': '()()()()(())',
        },
        {
            'input': '()()',
            'output': '',
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.removeOuterParentheses(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
