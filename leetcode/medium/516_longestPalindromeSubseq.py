from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def longestPalindromeSubseq_0(self, s: str) -> int:
        n = len(s)
        res = 1

        def rec(i, substr):
            nonlocal s, n, res

            rev = substr[::-1]
            if rev == substr:
                res = max(res, len(substr))

            if i >= n:
                return

            rec(i+1, substr + s[i])
            rec(i+1, substr)

        rec(0, '')

        return res

    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        res = 1

        def lcs(string1, string2):
            n = len(string1)
            memo = [[0]*n for i in range(n)]

            for r in range(n):
                for c in range(n):
                    top = memo[r-1][c] if r > 0 else 0
                    left = memo[r][c-1] if c > 0 else 0
                    diag = memo[r-1][c-1] if r > 0 and c > 0 else 0

                    memo[r][c] = max(top, left)
                    if string1[r] == string2[c]:
                        memo[r][c] = max(memo[r][c], diag + 1)

            return memo[-1][-1]

        return lcs(s, s[::-1])

'''

abckiocba
abcoikcba

  a b c k i o c b a
a 1 1 1 1 1 1 1 1 1
b 1 2 2 2 2 2 2 2 2
c 1 2 3 3 3 3 3 3 3
o 1 2 3 3 3 4 4 4 4
i 1 2 3 3 4 4 4 4 4
k 1 2 3 4 4 4 4 4 4
c 1 2 3 4 4 4 5 5 5
b 1 2 3 4 4 4 5 6 6
a 1 2 3 4 4 4 5 6 7


  a b c
c 0 0 1
b 0 1 1
a 1 1 1



'''



def test ():
    params = [
        {
            'input': 'abckiocba',
            'output': 7,
        },
        {
            'input': 'bbbab',
            'output': 4,
        },
        {
            'input': 'cbbd',
            'output': 2,
        },
        {
            'input': 'euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxojfofbvwnncajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymdyxoeodqmvkxittxjnlltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpuktirmduxdywwlbikaqkqajzbsjvdgjcnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuvucmesnnrwppheizkapovoloneaxpfinaontwtdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew',
            'output': 4,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.longestPalindromeSubseq(param['input'])
        correct = json.dumps(result) == json.dumps(param['output'])

        msg = 'SUCCESS' if correct else 'ERROR'
        msg += '\n'
        if not correct:
            msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()
