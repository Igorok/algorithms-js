from typing import List
from json import dumps

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res = []
        groupBySize = {}

        def insertInGroup(id, size):
            print('id, size', id, size)

            group = groupBySize.get(size, [])
            group.append(id)
            if len(group) == size:
                res.append(group)
                groupBySize[size] = []
            else:
                groupBySize[size] = group

            print('groupBySize', groupBySize)

        for i in range(len(groupSizes)):
            insertInGroup(i, groupSizes[i])


        return res


def test ():
    params = [
        {
            'input': [3,3,3,3,3,1,3],
            'output': [[5],[0,1,2],[3,4,6]],
        },
        {
            'input': [2,1,3,3,3,2],
            'output': [[1],[0,5],[2,3,4]],
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.groupThePeople(param['input'])
        print(
            'SUCCESS' if dumps(result) == dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
