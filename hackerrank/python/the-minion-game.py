# Problem Link: https://www.hackerrank.com/challenges/the-minion-game/problem

VOWELS = ['A', 'E', 'I', 'O', 'U']

def minion_game(string):
    str_len = len(string)
    stuart_score, kevin_score = 0, 0
    for index, char in enumerate(string):
        if char in VOWELS:
            kevin_score += str_len-index
        else:
            stuart_score += str_len-index

    if stuart_score > kevin_score:
        print(f'Stuart {stuart_score}')
    elif stuart_score < kevin_score:
        print(f'Kevin {kevin_score}')
    else:
        print('Draw')
        

if __name__ == '__main__':
    s = input()
    minion_game(s)