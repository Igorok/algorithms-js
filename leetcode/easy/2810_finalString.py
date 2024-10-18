from typing import List

class Solution:
    def finalString(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            if s[i] == 'i' and res != '':
                res = res[::-1]
            else:
                res += s[i]

        return res

def test ():
    params = [
        {
            'input': 'string',
            'output': 'rtsng',
        },
        {
            'input': 'poiinter',
            'output': 'ponter',
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.finalString(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
