'''
Задача на программирование: наибольший общий делитель

Sample Input 1:
18 35
Sample Output 1:
1

Sample Input 2:
14159572 63967072
Sample Output 2:
4
'''

def gcd(a, b):
    while a and b:
        if a > b:
            a %= b
        else:
            b %= a

    return max(a, b)


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()