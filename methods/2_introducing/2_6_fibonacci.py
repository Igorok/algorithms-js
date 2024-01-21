# 0,1,1,2,3,5,8,13,21,34...
def fib_digit(n):
    x1 = 0
    x2 = 1
    if n < 2:
        return n

    for i in range(n - 1):
        x1, x2 = x2, x1 + x2

    return x2


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()