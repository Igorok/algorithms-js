from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats = sorted(seats)
        students = sorted(students)

        moves = 0
        for i in range(len(seats)):
            moves += abs(students[i] - seats[i])

        return moves


def test ():
    params = [
        {
            'input': [[3,1,5], [2,7,4]],
            'output': 4,
        },
        {
            'input': [[4,1,5,9], [1,3,2,6]],
            'output': 7,
        },

    ]
    solution = Solution()

    for param in params:
        seats, students = param['input']

        result = solution.minMovesToSeat(seats, students)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
