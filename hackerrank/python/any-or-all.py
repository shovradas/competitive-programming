# https://www.hackerrank.com/challenges/any-or-all/problem

n = int(input())
nums = input().strip().split(" ")

if(all([int(x)>0 for x in nums])):
    if any([x==x[::-1] for x in nums]):
        print(True)
    else:
        print(False)
else:
        print(False)
