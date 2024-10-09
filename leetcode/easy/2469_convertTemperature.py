from typing import List
from json import dumps

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [
            celsius + 273.15,
            celsius * 1.80 + 32.00
        ]


def test ():
    params = [
        {
            'input': 36.50,
            'output': [309.65000,97.70000],
        },
        {
            'input': 122.11,
            'output': [395.26000,251.79800],
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.convertTemperature(param['input'])
        print(
            'SUCCESS' if dumps(result) == dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
