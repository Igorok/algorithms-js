'''
Задача на программирование: кодирование Хаффмана
По данной непустой строке s длины не более 10^4 , состоящей из строчных букв латинского алфавита, постройте оптимальный беспрефиксный код.
В первой строке выведите количество различных букв k, встречающихся в строке, и размер получившейся закодированной строки.
В следующих k строках запишите коды букв в формате "letter: code".
В последней строке выведите закодированную строку.

Sample Input 1:
a
Sample Output 1:
1 1
a: 0
0

Sample Input 2:
abacabad
Sample Output 2:
4 14
a: 0
b: 10
c: 110
d: 111
01001100100111
'''

'''
abracadabra
'''


from heapq import heapify, heappop, heappush
from collections import Counter

class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def walk(self, _dict, _code):
        self.left.walk(_dict, _code + '0')
        self.right.walk(_dict, _code + '1')


class Leaf:
    def __init__(self, char):
        self.char = char

    def walk(self, _dict, _code):
        _dict[self.char] = _code or '0'


def get_huffman_code_heap(s):
    counted = []
    for [char, value] in Counter(s).items():
        counted.append((value, len(counted), Leaf(char)))
    heapify(counted)

    count = len(counted)
    while len(counted) > 1:
        l_value, l_count, left = heappop(counted)
        r_value, r_count, right = heappop(counted)
        value = l_value + r_value
        heappush(counted, (value, count, Node(left, right)))
        count += 1

    [[value, count, node]] = counted
    _dict = {}
    node.walk(_dict, '')
    return _dict


def encode(_string, _code):
    encoded = ''
    for s in _string:
        encoded += _code[s]
    return encoded


def main():
    s = input()
    code = get_huffman_code_heap(s)
    encoded = encode(s, code)

    print('{} {}'.format(len(code), len(encoded)))
    for key, value in code.items():
        print('{}: {}'.format(key, value))
    print(encoded)


if __name__ == "__main__":
    main()
