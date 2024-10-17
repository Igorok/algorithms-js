from typing import List
from json import dumps

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        postfix = [None]*len(nums2)
        postfix[-1] = nums2[-1]
        positions = {}
        positions[nums2[-1]] = len(nums2) - 1

        for i in range(len(nums2) - 2, -1, -1):
            postfix[i] = max(nums2[i], postfix[i+1])
            positions[nums2[i]] = i

        print(
            'postfix', postfix,
            'positions', positions,
        )

        res = [-1] * len(nums1)
        for i in range(len(nums1)):
            val = nums1[i]
            id = positions[val]
            if postfix[id] > val:
                for j in range(id + 1, len(nums2)):
                    if nums2[j] > val:
                        res[i] = nums2[j]
                        break

        return res



def test ():
    params = [
        {
            'input': [[4,1,2], [1,3,4,2]],
            'output': [-1,3,-1],
        },
        {
            'input': [[2,4], [1,2,3,4]],
            'output': [3,-1],
        },
    ]
    solution = Solution()

    for param in params:
        nums1, nums2 = param['input']
        result = solution.nextGreaterElement(nums1, nums2)
        print(
            'SUCCESS' if dumps(result) == dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
