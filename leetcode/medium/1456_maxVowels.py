from typing import List

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = ('a', 'e', 'i', 'o', 'u')

        cnt = 0
        for i in range(k):
            c = s[i]
            if c in vowel:
                cnt += 1

        r = cnt
        for i in range(k, len(s)):
            c = s[i]
            if c in vowel:
                cnt += 1
            pc = s[i-k]
            if pc in vowel:
                cnt -= 1

            r = max(r, cnt)

        return r


def test ():
    params = [
        {
            'input': ["abciiidef", 3],
            'output': 3,
        },
        {
            'input': ["aeiou", 2],
            'output': 2,
        },
        {
            'input': ["leetcode", 3],
            'output': 2,
        },
    ]
    solution = Solution()

    for param in params:
        s, k = param['input']
        result = solution.maxVowels(s, k)

        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
