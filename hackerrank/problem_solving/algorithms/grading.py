#!/bin/python3

""" problem: https://www.hackerrank.com/challenges/grading """

__author__ = "Shovra Das"

def gradingStudents(grades):
    for i, grade in enumerate(grades):
        if grade>37 and grade%5 >= 3:
            grades[i] = (grades[i]//5+1)*5
    return grades

if __name__ == '__main__':
    grades_count = int(input().strip())
    grades = [int(input()) for _ in range(grades_count)]
    
    result = gradingStudents(grades)
    print('\n'.join(map(str, result)))
