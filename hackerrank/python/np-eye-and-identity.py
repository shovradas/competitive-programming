import numpy

dimensions = map(int, input().split())
# numpy.set_printoptions(legacy='1.13') # Added to match output with extra space
print(numpy.eye(*dimensions))