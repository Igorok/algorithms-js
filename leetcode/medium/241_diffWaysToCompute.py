from typing import List
from json import dumps

class Solution:
    def _diffWaysToCompute(self, expression: str) -> List[int]:
        listOfNumbers = []
        operators = {
            '*': '*',
            '+': '+',
            '-': '-',
        }
        i = 0
        while i < len(expression):
            char = expression[i]
            if char in operators:
                listOfNumbers.append(char)
                i += 1
            elif i + 1 < len(expression):
                if  expression[i + 1] in operators:
                    listOfNumbers.append(int(char))
                    i += 1
                else:
                    listOfNumbers.append(int(expression[i : i+2]))
                    i += 2
            else:
                listOfNumbers.append(int(char))
                i += 1

        print(listOfNumbers)

        return []


    def diffWaysToCompute(self, expression: str) -> List[int]:
        operators = {
            '*': lambda a, b : a * b,
            '+': lambda a, b : a + b,
            '-': lambda a, b : a - b,
        }
        def getNumbers(start, end):
            if end - start <= 0:
                return []

            if end - start == 1 and expression[start].isnumeric():
                return [int(expression[start])]

            if end - start == 2 and expression[start].isnumeric():
                return [int(expression[start: start + 2])]

            result = []
            for i in range(start, end):
                if expression[i] not in operators:
                    continue

                leftNumbers = getNumbers(start, i)
                rightNumbers = getNumbers(i + 1, end)

                for l in leftNumbers:
                    for r in rightNumbers:
                        result.append(operators[expression[i]](l, r))

            return result

        res = getNumbers(0, len(expression))
        if len(res) == 0:
            res = int(expression)

        return res

'''

2*3-4*5

---

2*3-4*5

(2)*(3-4*5)
    (2)*((3)-(4*5)) = 2 * (3 - 20) = -34
    (2)*((3-4)*(5)) = 2 * (-1 * 5) = -10

(2*3)-(4*5) = 6 - 20 = -14

(2*3-4)*(5)
    ((2*3)-(4))*(5) = (6 - 4) * 5 = 10
    (2*(3-4))*(5) = (2 * -1) * 5 = -10



2*3-4*5
2*3-4*5
2*3-4*5


'''


def test ():
    params = [
        {
            'input': "2-1-1",
            'output': [0,2],
        },
        {
            'input': "2*3-4*5",
            'output': [-34,-14,-10,-10,10],
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.diffWaysToCompute(param['input'])
        result = dumps(sorted(result))
        output = dumps(sorted(param['output']))
        print(
            'SUCCESS' if result == output else 'ERROR',
            'input', param['input'],
            'output', output,
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
