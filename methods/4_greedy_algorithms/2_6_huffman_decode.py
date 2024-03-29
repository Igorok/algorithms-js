'''
Восстановите строку по её коду и беспрефиксному коду символов.

В первой строке входного файла заданы два целых числа k и l через пробел — количество различных букв, встречающихся в строке, и размер получившейся закодированной строки, соответственно. В следующих k строках записаны коды букв в формате "letter: code". Ни один код не является префиксом другого. Буквы могут быть перечислены в любом порядке. В качестве букв могут встречаться лишь строчные буквы латинского алфавита; каждая из этих букв встречается в строке хотя бы один раз. Наконец, в последней строке записана закодированная строка. Исходная строка и коды всех букв непусты. Заданный код таков, что закодированная строка имеет минимальный возможный размер.
В первой строке выходного файла выведите строку s. Она должна состоять из строчных букв латинского алфавита. Гарантируется, что длина правильного ответа не превосходит 10^4 символов.
'''

'''.git/
bcbdbcb

'''


import sys


def huffman_decode(_string, _codes):
    encoded = ''
    i = 0
    while i < len(_string):
        for [code, char] in _codes.items():
            if _string.startswith(code, i):
                encoded += char
                i += len(code)
                break

    return encoded


def main():
    data = []
    _codes = {}
    for line in sys.stdin:
        if ':' in line:
            [char, code] = line.strip().split(': ')
            _codes[code] = char
        else:
            data.append(line.strip())

    _string = data.pop()
    encoded = huffman_decode(_string, _codes)
    print(encoded)


if __name__ == "__main__":
    main()
