# Problem Link: https://www.hackerrank.com/challenges/zipped/problem

__author__ = "Shovra Das"

n, x = map(int, input().split())

student_marks = [map(float, input().split()) for _ in range(x)]

for marks in zip(*student_marks):
    print(sum(marks)/x)
