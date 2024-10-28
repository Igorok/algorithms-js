from typing import List

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        arr = sorted(set(nums))

        res = -1
        checked = {}
        checkedNum = 0
        def binSearch(s, num):
            nonlocal arr

            start = s
            end = len(arr) - 1
            if arr[end] < num:
                return None

            while start <= end:
                middle = (end + start) // 2
                if arr[middle] == num:
                    return middle
                elif num < arr[middle]:
                    end = middle - 1
                else:
                    start = middle + 1
            return None

        for i in range(len(arr)):
            if i in checked:
                continue
            num = arr[i]
            checked[i] = 1
            subarr = [num]

            sqrNum = num**2
            while True:
                id = binSearch(i+1, sqrNum)
                if not id:
                    break
                subarr.append(sqrNum)
                sqrNum = sqrNum**2
                checked[id] = 1

            if len(subarr) > 1:
                res = max(res, len(subarr))

        return res


def test ():
    params = [
        {
            'input': [4,3,6,16,8,2],
            'output': 3,
        },
        {
            'input': [2,3,5,6,7],
            'output': -1,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.longestSquareStreak(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
