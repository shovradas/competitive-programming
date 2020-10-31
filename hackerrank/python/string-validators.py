# https://www.hackerrank.com/challenges/string-validators/problem


if __name__ == '__main__':
    s = input()

    for c in s:
        if c.isalnum():
            print(True)
            break;
    else:
        print(False)

    for c in s:
        if c.isalpha():
            print(True)
            break;
    else:
        print(False)

    for c in s:
        if c.isdigit():
            print(True)
            break;
    else:
        print(False)

    for c in s:
        if c.islower():
            print(True)
            break;
    else:
        print(False)

    for c in s:
        if c.isupper():
            print(True)
            break;
    else:
        print(False)
