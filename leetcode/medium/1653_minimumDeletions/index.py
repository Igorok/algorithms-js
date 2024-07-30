class Solution:
    def minimumDeletions(self, s: str) -> int:
        aTotal = 0
        bTotal = 0
        for char in s:
            if char == 'a':
                aTotal += 1
            else:
                bTotal += 1

        if aTotal == 0 or bTotal == 0:
            return 0

        actions = len(s)
        a = 0
        b = 0

        for char in s:
            if char == 'a':
                a += 1

            aRight = aTotal - a
            actions = min(actions, aRight + b)

            if char == 'b':
                b += 1

        return actions

'''
aababbab

a a b a b b a b


b b b a a

bbbbbbaaabbaababbabbb
b b b b b b a a a b b a a b a b b a b b b
a7
b14

b6
correctB = 3
wrongB = 14 - 3 = 11
wrongBRight = 11 - 6 = 5

a left = 0
a ritgh = 7 - 1 = 6


b b b b a a a b b a b b


'''



def test ():
    params = [
        {
            'input': 'bbbaa',
            'output': 2,
        },
        {
            'input': 'aababbab',
            'output': 2,
        },
        {
            'input': 'bbaaaaabb',
            'output': 2,
        },
        {
            'input': 'baababbaabbaaabaabbabbbabaaaaaabaabababaaababbb',
            'output': 18,
        },
        {
            'input': 'bbbbbbaaabbaababbabbb',
            'output': 7,
        },
        {
            'input': 'ababaaaabbbbbaaababbbbbbaaabbaababbabbbbaabbbbaabbabbabaabbbababaa',
            'output': 25,
        },
        {
            'input': 'bbbb',
            'output': 0,
        },
        {
            'input': 'aabbbbaabababbbbaaaaaabbababaaabaabaabbbabbbbabbabbababaabaababbbbaaaaabbabbabaaaabbbabaaaabbaaabbbaabbaaaaabaa',
            'output': 52,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.minimumDeletions(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()



'''
baababbaabbaaabaabbabbbabaaaaaabaabababaaababbb

b a a b a b b a a b b a a a b a a b b a b b b a b a a a a a a b a a b a b a b a a a b a b b b
1       2     3 4
a2
b3

a a1 b0
b a1 b1
a a2 b1 - broken - 1
b a1 b2
a a2 b2 - broken - 2
b a1 b3
a a 2 b3 - broken
a a3 b3
a a4 b3
a a5 b3
a a6 b3
b a6 b4 - 3 = 6
????

a a1 b0
b a1 b1
a a2 b1 - broken left=a2, rigth = a8-2=6; left b1, right b4-1=3;
b a2 b2
a a3 b2 - broken left=a3, rigth = a8-3=5; left b3, right b4-3=1;
b a3 b3         left=a3, rigth = a8-3=5; left b3, right b4-3=1;
a a4 b3 - broken
a a5 b3
a a6 b3
a a7 b3
a a8 b3
b a8 b4

abababaaaaab
a b a b a b a a a a a b

'''
