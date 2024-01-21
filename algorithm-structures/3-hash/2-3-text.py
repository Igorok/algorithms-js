'''
Поиск образца в тексте

Найти все вхождения строки Pattern в строку Text.
Вход.
Строки Pattern и Text.
Выход.
Все индексы i строки Text, начиная с которых строка Pattern входит в Text: Text[i..i + |Pattern| - 1] = Pattern.

Реализуйте алгоритм Карпа–Рабина.
Формат входа. Образец Pattern и текст Text.
Формат выхода. Индексы вхождений строки
Pattern в строку Text в возрастающем порядке, используя индексацию с нуля.
Ограничения. 1 <= |Pattern| <= |Text| <= 5*10^5 .
Суммарная длина всех вхождений образца в текста не превосходит 10^8. Обе строки содержат буквы латинского алфавита.


Sample Input 1:
aba
abacaba

Sample Output 1:
0 4

Sample Input 2:
Test
testTesttesT

Sample Output 2:
4

Sample Input 3:
aaaaa
baaaaaaa

Sample Output 3:
1 2 3
'''

'''
https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/
hash = (hash - (text[i - pattern_length] * (b**pattern_length - 1)) % p) * b + text[i]
t = (d*(t-ord(txt[i])*h) + ord(txt[i+M])) % q

h[i] = ((h[i] - t[i+p] * x**p-1) * x + t[i] * x**0) % p

abacaba
aba
 aba
  aba
   aba
    aba


'''

import sys
import random

class RabinKarpHasher:
    def __init__(self, pattern, text):
        self.pattern = pattern
        self.text = text
        self.p = len(text)*10
        self.x = random.randint(1, len(pattern))
        self.x_degrees = [pow(self.x, i, self.p) for i in range(len(pattern))]


    def hash(self, _string):
        sumOfChar = 0
        for i in range(len(_string)):
            sumOfChar += (ord(_string[i]) * self.x_degrees[i]) % self.p
        return sumOfChar % self.p

    def compareStr(self, i):
        j = 0
        l = len(self.pattern)
        while j < l // 2:
            s = l - j - 1
            if self.pattern[j] != self.text[i + j] or self.pattern[s] != self.text[i + s]:
                return False
            j +=1
        return True

    def search(self):
        result = []
        len_pattern = len(self.pattern)
        len_text = len(self.text)

        if len_text <= len_pattern:
            return [0] if self.text == self.pattern else []

        hash_pattern = self.hash(self.pattern)
        hash_past = self.hash(self.text[len_text - len_pattern:])

        if hash_pattern == hash_past:
            result.append(len_text - len_pattern)
            # if self.compareStr(len_text - len_pattern):
            #     result.append(len_text - len_pattern)

        for i in reversed(range(len_text - len_pattern)):
            # hash_past = ((hash_past - ord(self.text[i + len_pattern]) * self.x_degrees[-1]) * self.x + ord(self.text[i])) % self.p
            hash_past = (
                ((hash_past - ord(self.text[i + len_pattern]) * self.x_degrees[-1]) % self.p) * self.x
                + ord(self.text[i])
            ) % self.p

            if hash_past == hash_pattern:
                result.append(i)
                # if self.compareStr(i):
                #     result.append(i)

        return list(reversed(result))



def main():
    data = []
    for line in sys.stdin:
        data.append(line.strip())

    rabinKarpHasher = RabinKarpHasher(data[0], data[1])
    result = rabinKarpHasher.search()
    print(' '.join([str(i) for i in result]))

def test():
    assert RabinKarpHasher('aba', 'abacaba').search() == [0, 4]
    assert RabinKarpHasher('Test', 'testTesttesT').search() == [4]
    assert RabinKarpHasher('aaaaa', 'baaaaaaa').search() == [1, 2, 3]

if __name__ == '__main__':
    main()
