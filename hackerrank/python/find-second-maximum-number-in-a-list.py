# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

__author__ = "Shovra Das"

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    winning_score = -101
    runnerup_score = -101
    for score in arr:
        if score > winning_score:
            runnerup_score = winning_score
            winning_score = score
        else:
            if score != winning_score and score > runnerup_score:
                runnerup_score = score
    
    print(runnerup_score)
