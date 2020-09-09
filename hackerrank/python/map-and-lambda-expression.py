# Problem Link: https://www.hackerrank.com/challenges/map-and-lambda-expression/problem

cube = lambda x: x*x*x

def fibonacci(n):    
    if n==0:
        return []
    if n==1:
        return [0]

    numbers = [0, 1]
    for _ in range(n-2):
        numbers.append(numbers[-1] + numbers[-2])
    return numbers

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))