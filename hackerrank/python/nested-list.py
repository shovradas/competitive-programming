# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':

    student_grades = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_grades.append([name, score])
    
    student_grades.sort(key=lambda x: x[1])

    second_lowest_scorers = []
    for i in range(0, len(student_grades)):
        if student_grades[i][1] == student_grades[0][1]:
            second_lowest_score = student_grades[i+1][1]
            continue        
        if student_grades[i][1] != second_lowest_score:
            break
        second_lowest_scorers.append(student_grades[i][0])

    for i in sorted(second_lowest_scorers):
        print(i)
