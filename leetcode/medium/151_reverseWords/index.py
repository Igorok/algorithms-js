class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        arr = [w.strip() for w in s.split()]
        return ' '.join(reversed(arr))

def test ():
    params = [
        {
            'input': 'the sky is blue',
            'output': 'blue is sky the',
        },
        {
            'input': '  hello world  ',
            'output': 'world hello',
        },
        {
            'input': 'a good   example',
            'output': 'example good a',
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.reverseWords(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
