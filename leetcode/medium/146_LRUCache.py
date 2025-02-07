from typing import List
import json
from collections import deque

class Node:
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.queueStart = None
        self.queueEnd = None
        self.length = 0

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1

        node = self.cache[key]
        if node == self.queueEnd:
            return node.val
        elif node == self.queueStart:
            self.queueStart = self.queueStart.right
            self.queueStart.left = None
            self.queueEnd.right = node
            node.left = self.queueEnd
            node.right = None
            self.queueEnd = self.queueEnd.right
            return node.val

        node.left.right = node.right
        node.right.left = node.left
        self.queueEnd.right = node
        node.left = self.queueEnd
        node.right = None
        self.queueEnd = self.queueEnd.right

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.get(key)
            self.cache[key].val = value
            return

        if self.length + 1 > self.capacity:
            self.cache.pop(self.queueStart.key)
            self.queueStart = self.queueStart.right
            if self.queueStart:
                self.queueStart.left = None
            else:
                self.queueEnd = None
            self.length -= 1

        if not self.queueStart:
            self.queueStart = Node(key, value)
            self.queueEnd = self.queueStart
            self.cache[key] = self.queueStart
            self.length = 1
            return

        node = Node(key, value)
        self.cache[key] = node
        self.queueEnd.right = node
        node.left = self.queueEnd
        self.queueEnd = self.queueEnd.right
        self.length += 1




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


def test ():
    param = [
        ["put", "put", "get", "put", "get", "put", "get", "get", "get"],
        [[1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
    ]
    result = [None, None, 1, None, -1, None, -1, 3, 4]
    solution = LRUCache(2)

    for i in range(len(result)):
        command = param[0][i]
        if command == 'put':
            solution.put(param[1][i][0], param[1][i][1])
        else:
            r = solution.get(param[1][i][0])
            if r != result[i]:
                print('ERROR', r, result[i], '\n')
            else:
                print('SUCCESS', r, result[i], '\n')





if __name__ == '__main__':
    test()
