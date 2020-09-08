# Problem Link: https://www.hackerrank.com/challenges/zipped/problem

n, x = map(int, input().split())

student_marks = [map(float, input().split()) for _ in range(x)]

for marks in zip(*student_marks):
    print(sum(marks)/x)
