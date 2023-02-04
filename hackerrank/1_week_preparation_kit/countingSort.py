#!/bin/python3

# https://www.hackerrank.com/challenges/one-week-preparation-kit-countingsort1/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-two

import os

def countingSort(arr):
    counts = [0]*100
    for e in arr:
        counts[e] += 1
    return counts

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = countingSort(arr)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()


# Full algorithm --------------------------
#
# def countingSort(arr):
#     counts = [0]*100
#     for e in arr:
#         counts[e] += 1    
#     sorted_arr = []
#     for item, count in enumerate(counts):
#         sorted_arr.extend([item]*(count))
#     return sorted_arr

# if __name__ == '__main__':
#     data = "63 25 73 1 98 73 56 84 86 57 16 83 8 25 81 56 9 53 98 67 99 12 83 89 80 91 39 86 76 85 74 39 25 90 59 10 94 32 44 3 89 30 27 79 46 96 27 32 18 21 92 69 81 40 40 34 68 78 24 87 42 69 23 41 78 22 6 90 99 89 50 30 20 1 43 3 70 95 33 46 44 9 69 48 33 60 65 16 82 67 61 32 21 79 75 75 13 87 70 33"
#     # data = "1 1 3 2 1 7"
#     arr = list(map(int, data.split()))
#     sorted_arr = countingSort(arr)
#     print(' '.join(map(str, sorted_arr)))




# More generic
# def countingSort(array):
#     _min, _max = min(array), max(array)
#     counts = {i:0 for i in range(_min, _max+1)}
 
#     for item in array:
#         counts[item] += 1

#     sorted_array = []
#     for item, count in counts.items():
#         sorted_array.extend([item]*(count))

#     return sorted_array

# if __name__ == '__main__':
#     data = "63 25 73 -2 1 98 100 73 56 84 86 57 16 83 8 25 81 56 9 53 98 67 99 12 83 89 80 91 39 86 76 85 74 39 25 90 59 10 94 32 44 3 89 30 27 79 46 96 27 32 18 21 92 69 81 40 40 34 68 78 24 87 42 69 23 41 78 22 6 90 99 89 50 30 20 1 43 3 70 95 33 46 44 9 69 48 33 60 65 16 82 67 61 32 21 79 75 75 13 87 70 33"
#     # data = "1 1 3 2 10 1 7 -5"
#     array = list(map(int, data.split()))
#     print(countingSort(array))