def int_as_array(num): return list(map(int, [y for y in str(num)]))


def array_as_int(arr): return int(''.join(map(str, arr)))


def read_int_array(): return list(map(int, input().split(' ')))


def solve(number):
    print('number', number)


T = int(input())

for i in range(T):
    N = int(input())
    print('M', N)
    number = int(input())
    solve(number)
