from typing import List


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        data = s.split('-')
        data = ''.join(data)
        data = data.upper()

        count = len(data) // k
        rem = len(data) % k

        parts = []
        if rem != 0:
            parts.append(data[0:rem])

        for i in range(count):
            parts.append(data[rem:rem+k])
            rem += k

        return '-'.join(parts)


def test ():
    params = [
        {
            'input': ["5F3Z-2e-9-w", 4],
            'output': "5F3Z-2E9W",
        },
        {
            'input': ["2-5g-3-J", 2],
            'output': "2-5G-3J",
        },
    ]
    solution = Solution()

    for param in params:
        s, k = param['input']
        result = solution.licenseKeyFormatting(s, k)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
