from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cash = {
            5: 0,
            10: 0,
            20: 0
        }

        for v in bills:
            if v == 5:
                cash[5] += 1

            if v == 10:
                if cash[5] == 0:
                    return False
                cash[5] -= 1
                cash[10] += 1

            if v == 20:
                if cash[10] > 0 and cash[5] > 0:
                    cash[10] -= 1
                    cash[5] -= 1
                    cash[20] += 1
                elif cash[5] >= 3:
                    cash[5] -= 3
                    cash[20] += 1
                else:
                    return False

        return True


def test ():
    params = [
        {
            'input': [5,5,5,10,20],
            'output': True,
        },
        {
            'input': [5,5,10,10,20],
            'output': False,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.lemonadeChange(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
