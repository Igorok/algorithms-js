from typing import List
from json import dumps
from queue import Queue

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        data = sorted(folder)

        key = data[0]
        folders = {}
        folders[key] = []
        for i in range(len(data)):
            if data[i].startswith(key + '/'):
                folders[key].append(data[i])
            else:
                key = data[i]
                folders[key] = []

        result = []
        for k in folders:
            result.append(k)

        return result

def test ():
    params = [
        {
            'input': ["/a","/a/b","/c/d","/c/d/e","/c/f"],
            'output': ["/a","/c/d","/c/f"],
        },
        {
            'input': ["/a/b/c", "/a/b/d", "/a",],
            'output': ["/a"],
        },
        {
            'input': ["/a/b/c","/a/b/ca","/a/b/d"],
            'output': ["/a/b/c","/a/b/ca","/a/b/d"],
        }
    ]
    solution = Solution()

    for param in params:
        result = solution.removeSubfolders(param['input'])
        print(
            'SUCCESS' if dumps(result) == dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
