# Problem Link: https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem

__author__ = "Shovra Das"

def wrapper(f):
    def fun(l):
        # complete the function
        for i in range(len(l)):
            m_num = l[i]
            l[i] = f'+91 {m_num[-10:-5]} {m_num[-5:]}'
        f(l)

    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 