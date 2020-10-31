# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

n = int(input())
s = set(map(int, input().split()))

N = int(input())
for _ in range(N):
    cmd = input().strip().split(' ')
    if cmd[0] == 'pop':
        s.pop()
    elif cmd[0] == 'discard ':
        s.discard(int(cmd[1]))
    else:
        try:
            s.remove(int(cmd[1]))
        except KeyError:
            continue

print(sum(s))
