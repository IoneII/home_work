import sys


def main(a=10):
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n, m = (input().split())
    table = []
    row = []
    for i in range(int(n)):
        for j in range(int(m)):
            row.append(int(input()))
        table.append(row)
        row = []

    print(table)



if __name__ == '__main__':
    main()
