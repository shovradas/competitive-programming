# https://www.hackerrank.com/challenges/py-check-subset/problem


t = int(input().strip())

for _ in range(t):
    len_a = int(input().strip())
    a = set(map(int, input().strip().split(' ')))

    len_b = int(input().strip())
    b = set(map(int, input().strip().split(' ')))

    if len_a > len_b:
        print(False)
    else:
        if all([i in b for i in a]):
            print(True)
        else:
            print(False)
