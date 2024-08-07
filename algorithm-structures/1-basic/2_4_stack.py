'''
Sample Input 1:
5
push 2
push 1
max
pop
max

Sample Output 1:
2
2

Sample Input 2:
5
push 1
push 2
max
pop
max
Sample Output 2:
2
1

Sample Input 3:
10
push 2
push 3
push 9
push 7
push 2
max
max
max
pop
max
Sample Output 3:
9
9
9
9


4
push 5
pop
push 3
max


'''

import sys

def printAnswer(n, commands):
    stack = []
    maxStack = []

    for com in commands:
        if (com[0] == 'pop' and len(stack) > 0):
            stack.pop()
            maxStack.pop()
        elif (com[0] == 'push'):
            n = int(com[1])
            stack.append(n)
            if len(maxStack) == 0 or maxStack[-1] < n:
                maxStack.append(n)
            else:
                maxStack.append(maxStack[-1])
        elif (com[0] == 'max'):
            if len(stack) == 0:
                print(0)
            else:
                print(maxStack[-1])

def main():
    n = None
    commands = []

    for line in sys.stdin:
        if n is None:
            n = int(line.strip())
        else:
            commands.append(line.strip().split(' '))

    printAnswer(n, commands)


if __name__ == '__main__':
    main()
