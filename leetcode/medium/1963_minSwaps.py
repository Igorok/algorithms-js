from typing import List

class Solution:
    def minSwaps_(self, s: str) -> int:
        self.swaps = 0

        data = s
        def stackify(data):
            stack = []
            fc = -1
            lo = -1
            for i in range(len(data)):
                char = data[i]
                if char == ']' and len(stack) > 0 and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(char)
            return stack

        def replacer(data):
            fc = -1
            lo = -1
            for i in range(len(data)):
                if fc == -1 and data[i] == ']':
                    fc = i
                    break
            for i in range(len(data) - 1, -1, -1):
                if lo == -1 and data[i] == '[':
                    lo = i
                    break
            data[fc], data[lo] = data[lo], data[fc]
            self.swaps += 1
            return data

        while len(data) > 0:
            data = stackify(data)
            if len(data) > 0:
                data = replacer(data)

        return self.swaps

    def minSwaps(self, s: str) -> int:
        closed = 0
        opened = 0
        start = 0
        end = len(s) - 1
        swaps = 0
        while start < end:
            ok = False
            if s[start] == '[':
                opened += 1
                start += 1
                ok = True
            elif s[start] == ']' and opened > 0:
                opened -= 1
                start += 1
                ok = True

            if s[end] == ']':
                closed += 1
                end -= 1
                ok = True
            elif s[end] == '[' and closed > 0:
                closed -= 1
                end -= 1
                ok = True

            if not ok:
                swaps += 1
                opened += 1
                closed += 1
                start += 1
                end -= 1

        return swaps


'''

]]][[[

]]][[[
1    1
[]][[]
111111
'''

def test ():
    params = [
        {
            'input': '][][',
            'output': 1,
        },
        {
            'input': ']]][[[',
            'output': 2,
        },
        {
            'input': '[]',
            'output': 0,
        },
        {
            'input': ']'*100 + '['*100,
            'output': 50,
        },
    ]

    for param in params:
        solution = Solution()
        result = solution.minSwaps(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
