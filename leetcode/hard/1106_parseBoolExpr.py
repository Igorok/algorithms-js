from typing import List
from json import dumps


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        expr = ('&','|', '!')
        self.start = 0

        def parse():
            ex = expression[self.start]
            booleans = []
            self.start += 1

            while expression[self.start] != ')':
                char = expression[self.start]
                if char == 'f':
                    booleans.append(False)
                elif char == 't':
                    booleans.append(True)
                elif char in expr:
                    res = parse()
                    booleans.append(res)
                self.start += 1

            if ex == '&':
                return all(booleans)
            if ex == '|':
                return any(booleans)

            return not booleans[0]

        return parse()


def test ():
    params = [
        {
            'input': "&(|(f))",
            'output': False,
        },
        {
            'input': "|(f,f,f,t)",
            'output': True,
        },
        {
            'input': "!(&(f,t))",
            'output': True,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.parseBoolExpr(param['input'])
        print(
            'SUCCESS' if dumps(result) == dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
