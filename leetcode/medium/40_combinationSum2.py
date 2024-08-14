from typing import List
import json

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        targeted = set()

        def recursion(i, numsList, sumOfNums):
            if sumOfNums == target:
                targeted.add(tuple(numsList))
                return

            if sumOfNums > target or i >= len(candidates):
                return

            cur = candidates[i]
            numsList.append(cur)
            recursion(i + 1, numsList, sumOfNums + cur)

            numsList.pop()
            while i < len(candidates) and candidates[i] == cur:
                i += 1
            recursion(i, numsList, sumOfNums)

        recursion(0, [], 0)

        return list(targeted)


def test ():
    params = [
        {
            'input': [[10,1,2,7,6,1,5], 8],
            'output': [
                [1,1,6],
                [1,2,5],
                [1,7],
                [2,6]
            ],
        },
        {
            'input': [[2,5,2,1,2], 5],
            'output': [
                [1,2,2],
                [5]
            ],
        },
        {
            'input': [[1,1,1,1,1,1,1,1,1], 2],
            'output': [
                [1,1],
            ],
        },
    ]
    solution = Solution()

    for param in params:
        candidates, target = param['input']
        result = solution.combinationSum2(candidates, target)
        print(
            'SUCCESS' if json.dumps(result) == json.dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
