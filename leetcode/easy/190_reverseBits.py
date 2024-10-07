from typing import List


class Solution:
    def reverseBits(self, n: int) -> int:
        sourse = n
        bits = []
        while sourse != 0:
            bits.append(str(sourse % 2))
            sourse //= 2

        print(bin(n))

        if len(bits) < 32:
            bits = bits + ['0']*(32-len(bits))

        print('0b' + ''.join(bits))
        print(int('0b' + ''.join(bits), 2))

        return int('0b' + ''.join(bits), 2)



def test ():
    params = [
        {
            'input': 43261596,
            'output': 964176192,
        },
        {
            'input': 4294967293,
            'output': 3221225471,
        },

    ]
    solution = Solution()

    for param in params:
        result = solution.reverseBits(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
