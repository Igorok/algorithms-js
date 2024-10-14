from typing import List


class Solution:
    def interpret(self, command: str) -> str:
        if command == '':
            return command

        res = ''
        start = 0
        while start < len(command):
            if command[start] == 'G':
                res += 'G'
                start += 1
            elif start + 1 <= len(command) and command[start:start+2] == '()':
                res += 'o'
                start += 2
            elif start + 3 <= len(command) and command[start:start+4] == '(al)':
                res += 'al'
                start += 4

        return res


def test ():
    params = [
        {
            'input': "G()(al)",
            'output': 'Goal',
        },
        {
            'input': "(al)G(al)()()G",
            'output': 'alGalooG',
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.interpret(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
