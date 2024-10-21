from typing import List
from json import dumps

class Solution:
    def decodeString(self, s: str) -> str:
        self.result = ''
        self.start = 0

        def getNum():
            start = self.start
            while s[self.start].isdigit():
                self.start += 1
            return int(s[start:self.start])

        # 3[a2[c]]
        def parseBraces():
            num = getNum()
            self.start += 1
            res = ''
            while s[self.start] != ']':
                if s[self.start].isdigit():
                    res += parseBraces()
                else:
                    res += s[self.start]
                self.start += 1

            return res*num

        while self.start < len(s):
            if s[self.start].isdigit():
                self.result += parseBraces()
            else:
                self.result += s[self.start]
            self.start += 1

        return self.result


def test ():
    params = [
        {
            'input': '3[a]2[bc]',
            'output': 'aaabcbc',
        },
        {
            'input': '3[a2[c]]',
            'output': 'accaccacc',
        },
        {
            'input': '2[abc]3[cd]ef',
            'output': 'abcabccdcdcdef',
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.decodeString(param['input'])
        print(
            'SUCCESS' if dumps(result) == dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
