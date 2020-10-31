# https://www.hackerrank.com/challenges/py-if-else/problem


if __name__ == '__main__':
    n = int(input().strip())

    if n&1 == 1:
        print("Weird")
    else:
        if n>1 and n<6:
            print("Not Weird")
        
        elif n>5 and n<21:
            print("Weird")

        else:
           print("Not Weird") 
