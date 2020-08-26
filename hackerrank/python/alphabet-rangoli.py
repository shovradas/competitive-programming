# Problem Link: https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_rangoli(size):
    w = size + 3*(size-1)

    for i in range(size-1, 0, -1):
        line_items = [chr(j+96) for j in range(size, i, -1)]
        line_items +=  [chr(j+96) for j in range(i+2, size+1)]
        print('-'.join(line_items).center(w, '-'))

    for i in range(size):
        line_items = [chr(j+96) for j in range(size, i, -1)]
        line_items +=  [chr(j+96) for j in range(i+2, size+1)]
        print('-'.join(line_items).center(w, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)