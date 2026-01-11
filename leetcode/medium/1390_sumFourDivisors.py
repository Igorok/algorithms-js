from typing import List
import heapq
import math


class Solution_0:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            sqrt2 = math.ceil(math.sqrt(num))
            divisors = set()

            for n1 in range(1, sqrt2+1):
                n2 = num // n1
                if num % n1 == 0:
                    divisors.add(n1)
                    divisors.add(n2)
                if len(divisors) > 4:
                    break

            if len(divisors) == 4:
                res += sum(divisors)


        return res



class Solution:
    def precompute(self):
        maxVal = 1 + 10**5

        self.countOfDivisors = [0] * maxVal
        self.sumOfDivisors = [0] * maxVal

        for n1 in range(1, math.ceil(math.sqrt(maxVal)) + 1):
            for n2 in range(n1, maxVal, n1):
                self.countOfDivisors[n2] += 1
                self.sumOfDivisors[n2] += n1


        # res = {}
        # for n in range(maxVal):
        #     if self.countOfDivisors[n] == 4:
        #         res[n] = self.sumOfDivisors[n]

        # print(res)


    def sumFourDivisors(self, nums: List[int]) -> int:
        self.precompute()
        res = 0

        for num in nums:
            if self.countOfDivisors[num] == 4:
                res += self.sumOfDivisors[num]

        return res



def test ():
    params = [
        {
            'input': [21,4,7],
            'output': 32,
        },
        {
            'input': [21,21],
            'output': 64,
        },
        {
            'input': [1,2,3,4,5],
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.sumFourDivisors(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
