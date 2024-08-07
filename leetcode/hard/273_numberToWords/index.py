class Solution:
    ones = [
        "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
        "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
    ]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'

        result = []
        i = 0
        while num != 0:
            remainder = num % 1000
            num = num // 1000

            res = []
            hundred = remainder // 100
            if hundred != 0:
                res.append(self.ones[hundred] + ' Hundred')

            remainder %= 100
            if remainder < 20 and remainder != 0:
                res.append(self.ones[remainder])
            elif remainder >= 20:
                ten = remainder // 10
                res.append(self.tens[ten])

                remainder %= 10
                if remainder != 0:
                    res.append(self.ones[remainder])

            if i != 0 and len(res) != 0:
                res.append(self.thousands[i])

            if len(res) != 0:
                result.append(' '.join(res))

            i += 1

        return ' '.join(reversed(result))


def test ():
    params = [
        {
            'input': 123,
            'output': 'One Hundred Twenty Three',
        },
        {
            'input': 12345,
            'output': 'Twelve Thousand Three Hundred Forty Five',
        },
        {
            'input': 1234567,
            'output': 'One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven',
        },
        {
            'input': 2147483647,
            'output': 'Two Billion One Hundred Forty Seven Million Four Hundred Eighty Three Thousand Six Hundred Forty Seven',
        },
        {
            'input': 1000100,
            'output': 'One Million One Hundred',
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.numberToWords(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
