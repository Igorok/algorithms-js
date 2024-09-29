from typing import List
from json import dumps

class MyCircularDeque:

    def __init__(self, k: int):
        self.max = k
        self.arr = [None] * self.max
        self.length = 0
        self.left = self.right = None

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.left == None:
            self.left = self.right = self.max // 2
        else:
            if self.left > 0:
                self.left -= 1
            else:
                self.left = self.max - 1

        self.arr[self.left] = value
        self.length += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.left == None:
            self.left = self.right = self.max // 2
        else:
            self.right = (self.right + 1) % self.max

        self.arr[self.right] = value
        self.length += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.left == self.max - 1:
            self.left = 0
        else:
            self.left += 1

        self.length -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.right == 0:
            self.right = self.max - 1
        else:
            self.right -= 1
        self.length -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.left]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.right]

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.max



'''
Input
["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, True, True, True, false, 2, True, True, True, 4]


[None, True, True, True, False, 2, True, True, True, 4]
[None, True, True, True, False, False]



'''
def test ():
    params = [
        {
            'input': [
                ('MyCircularDeque', 3),
                ('insertLast', 1),
                ('insertLast', 2),
                ('insertFront', 3),
                ('insertFront', 4),
                ('getRear'),
                ('isFull'),
                ('deleteLast'),
                ('insertFront', 4),
                ('getFront'),
            ],
            'output': [None, True, True, True, False, 2, True, True, True, 4],
        },
    ]


    for param in params:
        result = []
        myCircularDeque = None
        for p in param['input']:
            print('p', p)

            if p[0] == 'MyCircularDeque':
                myCircularDeque = MyCircularDeque(p[1])
                result.append(None)
            elif p[0] == 'insertFront':
                result.append(myCircularDeque.insertFront(p[1]))
            elif p[0] == 'insertLast':
                result.append(myCircularDeque.insertLast(p[1]))
            elif p[0] == 'deleteFront':
                result.append(myCircularDeque.deleteFront())
            elif p[0] == 'deleteLast':
                result.append(myCircularDeque.deleteLast())
            elif p[0] == 'getFront':
                result.append(myCircularDeque.getFront())
            elif p[0] == 'getRear':
                result.append(myCircularDeque.getRear())
            elif p[0] == 'isEmpty':
                result.append(myCircularDeque.isEmpty())
            elif p[0] == 'isFull':
                result.append(myCircularDeque.isFull())

        print(
            'SUCCESS' if dumps(result) == dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
