from typing import List

class Solution:
    def maxUniqueSplit_1(self, s: str) -> int:
        def split(string):
            substr = set()
            start = 0
            end = 1

            while end <= len(string):
                if not string[start:end] in substr:
                    substr.add(string[start:end])
                    start = end
                end += 1

            print('substr', substr)
            return len(substr)

        return max(
            split(s),
            split(s[::-1]),
        )


    def maxUniqueSplit(self, s: str) -> int:
        self.string = s
        self.res = 0

        def split(start, acc):
            if start == len(self.string):
                self.res = max(self.res, len(acc))
                return

            for i in range(start + 1, len(self.string) + 1):
                sub = self.string[start:i]
                if sub in acc:
                    continue
                acc.add(sub)
                split(i, acc)
                acc.remove(sub)

        split(0, set())

        return self.res


def test ():
    params = [
        {
            'input': 'ababccc',
            'output': 5,
        },
        {
            'input': 'aba',
            'output': 2,
        },
        {
            'input': 'aa',
            'output': 1,
        },
        {
            'input': 'wwwzfvedwfvhsww',
            'output': 11,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.maxUniqueSplit(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
