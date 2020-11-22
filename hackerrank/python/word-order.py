# https://www.hackerrank.com/challenges/word-order/problem

__author__ = "Shovra Das"

n = int(input().strip())

word_counts = {}
for i in range(n):
    word = input().strip()

    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(len(word_counts))
for k, v in word_counts.items():
    print(v, end=' ')
