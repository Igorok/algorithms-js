from typing import List

class Solution:
    def checkInclusion_(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        target = ''.join(sorted(s1))

        s1Count = {}
        for char in s1:
            count = s1Count.get(char, 0)
            s1Count[char] = count + 1

        start = 0
        end = len(s1)

        while end <= len(s2):
            if ''.join(sorted(s2[start:end])) == target:
                return True
            start += 1
            end += 1

        return False

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        target = ''.join(sorted(s1))
        def hash(char):
            return (ord(char) - ord('a') + 1)
        s1Sum = 0
        for char in s1:
            s1Sum += hash(char)

        s2Sum = 0
        for i in range(len(s1)):
            char = s2[i]
            s2Sum += hash(char)

        if s1Sum == s2Sum and ''.join(sorted(s2[:len(s1)])) == target:
            return True

        start = 1
        end = len(s1)
        while end < len(s2):
            s2Sum -= hash(s2[start - 1])
            s2Sum += hash(s2[end])

            if s1Sum == s2Sum:
                if ''.join(sorted(s2[start:(end + 1)])) == target:
                    return True
            start += 1
            end += 1


        return False


def test ():
    params = [
        {
            'input': ["ab", "eidbaooo"],
            'output': True,
        },
        {
            'input': ["ab", "eidboaoo"],
            'output': False,
        },
        {
            'input': ["adc", "dcda"],
            'output': True,
        },
        {
            'input': ["abc", "ccccbbbbaaaa"],
            'output': False,
        },


    ]
    solution = Solution()

    for param in params:
        s1, s2 = param['input']
        result = solution.checkInclusion(s1, s2)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
