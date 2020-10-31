# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

from collections import defaultdict

n, m = map(int, input().strip().split(' '))

word_dict = defaultdict(lambda: -1)
for i in range(1, n+1):
    word = input().strip()
    if word not in word_dict:
        word_dict[word] = [i]
    else:
        word_dict[word].append(i)

for i in range(m):
    word = input().strip()
    print(' '.join(map(str, word_dict[word] if word_dict[word]!=-1 else [-1])))
