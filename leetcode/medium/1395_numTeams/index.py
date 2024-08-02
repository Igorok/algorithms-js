from typing import List

class Solution:
    def numTeams_(self, rating: List[int]) -> int:
        great = []
        less = []
        result = 0

        for rate in rating:
            newGreat = [[rate]]
            newLess = [[rate]]

            for sequence in great:
                if len(sequence) == 1:
                    if sequence[0] < rate:
                        newGreat.append([sequence[0], rate])
                if len(sequence) == 2:
                    if sequence[1] < rate:
                        newGreat.append([sequence[0], sequence[1], rate])
                        result += 1

            for sequence in less:
                if len(sequence) == 1:
                    if sequence[0] > rate:
                        newLess.append([sequence[0], rate])
                if len(sequence) == 2:
                    if sequence[1] > rate:
                        newLess.append([sequence[0], sequence[1], rate])
                        result += 1

            great = great + newGreat
            less = less + newLess

        return result

    def numTeams(self, rating: List[int]) -> int:
        result = 0

        raitingLength = len(rating)
        for i in range(1, raitingLength):
            less_left = 0
            bigger_left = 0
            less_right = 0
            bigger_right = 0

            for l in range(0, i):
                if rating[l] < rating[i]:
                    less_left += 1
                else:
                    bigger_left += 1

            for r in range(i + 1, raitingLength):
                if rating[r] > rating[i]:
                    bigger_right += 1
                else:
                    less_right += 1

            result += (less_left * bigger_right)
            result += (bigger_left * less_right)


        return result

def test ():
    params = [
        {
            'input': [2,5,3,4,1],
            'output': 3,
        },
        {
            'input': [2,1,3],
            'output': 0,
        },
        {
            'input': [1,2,3,4],
            'output': 4,
        }
    ]
    solution = Solution()

    for param in params:
        result = solution.numTeams(param['input'])
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
Example 1:
Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1).

Example 2:
Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.

Example 3:
Input: rating = [1,2,3,4]
Output: 4

'''

'''
2,5,3,4,1

    2 5 3 4 1
2 g:1, l:1, max:2, min: 2

5 g:1, l:1, max:2, min: 2

3

1

---

1,2,3,4

1 2 3 4

1 2 3
1 3 4
1 2 4
2 3 4
















'''
