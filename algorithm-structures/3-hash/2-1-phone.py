'''
Телефонная книга

Sample Input 1:
12
add 911 police
add 76213 Mom
add 17239 Bob
find 76213
find 910
find 911
del 910
del 911
find 911
find 76213
add 76213 daddy
find 76213

Sample Output 1:
Mom
not found
police
not found
Mom
daddy

Sample Input 2:
8
find 3839442
add 123456 me
add 0 granny
find 0
find 123456
del 0
del 0
find 0

Sample Output 2:
not found
granny
me
not found
'''


import sys


class PhoneBook:
    phones = [None]*10**7

    def apply(self, command, phone, name):
        if command == 'find':
            print('not found' if self.phones[phone] is None else self.phones[phone])
        elif command == 'add':
            self.phones[phone] = name
        elif command == 'del':
            self.phones[phone] = None


def main():
    phoneBook = PhoneBook()
    i = 0
    for line in sys.stdin:
        if i != 0:
            data = line.strip().split(' ')
            n = data[2] if len(data) == 3 else None
            phoneBook.apply(data[0], int(data[1]), n)
        i += 1


if __name__ == '__main__':
    main()