# Problem Link: https://www.hackerrank.com/challenges/words-score/problem

__author__ = "Shovra Das"

def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words:
        num_vowels = sum([1 for letter in word if is_vowel(letter)])
        score += 2 if num_vowels & 1 == 0 else 1
    return score


n = int(input())
words = input().split()
print(score_words(words))