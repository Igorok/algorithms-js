'''
Реализуйте структуру данных "стек". Напишите программу, содержащую описание стека и моделирующую работу стека, реализовав все указанные здесь методы. Программа считывает последовательность команд и в зависимости от команды выполняет ту или иную операцию. После выполнения каждой команды программа должна вывести одну строчку. Возможные команды для программы:

push n
Добавить в стек число n (значение n задается после команды). Программа должна вывести ok.
pop
Удалить из стека последний элемент. Программа должна вывести его значение.
back
Программа должна вывести значение последнего элемента, не удаляя его из стека.
size
Программа должна вывести количество элементов в стеке.
clear
Программа должна очистить стек и вывести ok.
exit
Программа должна вывести bye и завершить работу.

Входные данные
Команды управления стеком вводятся в описанном ранее формате по 1 на строке.
Гарантируется, что набор входных команд удовлетворяет следующим требованиям: максимальное количество элементов в стеке в любой момент не превосходит 100, все команды pop и back корректны, то есть при их исполнении в стеке содержится хотя бы один элемент.

Выходные данные
Требуется вывести протокол работы со стеком, по 1 сообщению в строке

Sample Input:
push 1
back
exit

Sample Output:
ok
1
bye



push 1
push 2
push 3
push 4
size
back
back
back
size
pop
pop
pop
size
clear
size
push 2
push 3
push 4
size
exit

push 1
push 2
push 3
push 4
size
back
back
back
size
pop
pop
pop
size
clear
size
push 2
push 3
push 4
size
exit


ok
ok
ok
ok
4
4
4
4
4
4
3
2
1
ok
0
ok
ok
ok
3
bye


'''

import sys

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(n)

    def pop(self):
        return self.stack.pop()

    def back(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def clear(self):
        self.stack = []


def main():
    stack = Stack()
    for line in sys.stdin:
        arr = line.strip().split(' ')
        if arr[0] == 'push':
            stack.push(int(arr[1]))
            print('ok')
        elif arr[0] == 'pop':
            print(stack.pop())
        elif arr[0] == 'back':
            print(stack.back())
        elif arr[0] == 'size':
            print(stack.size())
        elif arr[0] == 'clear':
            stack.clear()
            print('ok')
        elif arr[0] == 'exit':
            print('bye')
            return


if __name__ == '__main__':
    main()
