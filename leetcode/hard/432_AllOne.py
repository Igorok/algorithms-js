from typing import List
from json import dumps

class Node:
    def __init__(self):
        self.str = ''
        self.count = 0
        self.next = None
        self.prev = None

class AllOne:
    def __init__(self):
        self.strs = {}
        self.start = Node()
        self.end = Node()
        self.end.count = 10e5
        self.start.next = self.end
        self.end.prev = self.start

    def _addNew(self, key: str):
        node = Node()
        node.str = key
        node.count = 1
        self.strs[key] = node

        n = self.start.next
        self.start.next = node
        node.next = n
        node.prev = self.start
        n.prev = node

    def _addExists(self, key: str):
        node = self.strs[key]
        node.count += 1
        while node.count > node.next.count:
            p = node.prev
            n = node.next
            nn = node.next.next
            n.prev = p
            n.next = node
            p.next = n
            node.prev = n
            node.next = nn
            nn.prev = node

    def inc(self, key: str) -> None:
        if not key in self.strs:
            self._addNew(key)
        else:
            self._addExists(key)

    def dec(self, key: str) -> None:
        node = self.strs[key]
        if node.count == 1:
            p = node.prev
            n = node.next
            p.next = n
            n.prev = p
            del self.strs[key]
        else:
            node.count -= 1
            while node.count < node.prev.count:
                n = node.next
                p = node.prev
                pp = p.prev
                pp.next = node
                node.prev = pp
                p.next = n
                p.prev = node
                node.next = p
                n.prev = p

    def getMaxKey(self) -> str:
        prev = self.end.prev
        if prev == self.start:
            return ''
        return prev.str

    def getMinKey(self) -> str:
        n = self.start.next
        if n == self.end:
            return ''
        return n.str



# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()


'''
a = 0
b = 0
c = 3

p ('inc', 'a')
p ('inc', 'b')
p ('inc', 'b')
p ('inc', 'c')
p ('inc', 'c')
p ('inc', 'c')
p ('dec', 'b')
p ('dec', 'b')
p ('getMinKey', '')
p ('dec', 'a')
p ('getMaxKey', '')
p ('getMinKey', '')


[None, None, None, None, None, None, None, None, 'a', None, 'c', 'c']
[None, None, None, None, None, None, None, None, 'a', None, '', '']




'''

def test ():
    params = [
        {
            'input': [
                ('inc', 'hello'),
                ('inc', 'hello'),
                ('getMaxKey',),
                ('getMinKey',),
                ('inc', 'leet'),
                ('getMaxKey',),
                ('getMinKey',),
            ],
            'output': [None, None, 'hello', 'hello', None, 'hello', 'leet'],
        },
        {
            'input': [
                ('inc','hello'),
                ('inc','goodbye'),
                ('inc','hello'),
                ('inc','hello'),
                ('getMaxKey',''),
                ('inc','leet'),
                ('inc','code'),
                ('inc','leet'),
                ('dec','hello'),
                ('inc','leet'),
                ('inc','code'),
                ('inc','code'),
                ('getMaxKey',''),
            ],
            'output': [None,None,None,None,'hello',None,None,None,None,None,None,None,'leet'],
        },
        {
            'input': [
                ('inc','a'),
                ('inc','b'),
                ('inc','b'),
                ('inc','c'),
                ('inc','c'),
                ('inc','c'),
                ('dec','b'),
                ('dec','b'),
                ('getMinKey',''),
                ('dec','a'),
                ('getMaxKey',''),
                ('getMinKey',''),
            ],
            'output': [None,None,None,None,None,None,None,None,"a",None,"c","c"],
        },
    ]

    for param in params:
        result = []
        allOne = AllOne()
        for p in param['input']:
            print('p', p)

            if p[0] == 'inc':
                result.append(allOne.inc(p[1]))
            elif p[0] == 'dec':
                result.append(allOne.dec(p[1]))
            elif p[0] == 'getMaxKey':
                result.append(allOne.getMaxKey())
            elif p[0] == 'getMinKey':
                result.append(allOne.getMinKey())

        print(
            'SUCCESS' if dumps(result) == dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

        node = allOne.start
        while node != None:
            print(node.str, node.count)
            node = node.next


if __name__ == '__main__':
    test()
