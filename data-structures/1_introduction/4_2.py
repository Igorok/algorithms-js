'''.git/
Sample Input:
10
Sample Output:
55
'''

def addNums(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s

def main():
    n = int(input())
    print(str(addNums(n)))

if __name__ == '__main__':
    main()