# https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem

import math

__author__ = "Shovra Das"

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        self.number = complex(real, imaginary)
        
    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)
        
    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)
        
    def __mul__(self, no):  # fromula: (a+bi)(c+di) = ac+adi+bci+bdi^2 = ac-bd+(ad+bc)i
        real = self.real * no.real - self.imaginary * no.imaginary
        imaginary = self.real * no.imaginary + self.imaginary * no.real
        return Complex(real, imaginary)

    def __truediv__(self, no):  # fromula: (a+bi)/(c+di) = (a+bi)*(c-di)/(c+di)*(c-di)
        no_conjugate = Complex(no.real, -no.imaginary)        
        numerator = self * no_conjugate
        denominator = no * no_conjugate  # imaginary part is zero
        return math.nan if denominator.real == 0 else Complex(
            numerator.real/denominator.real, 
            numerator.imaginary/denominator.real
        )

    def mod(self):
        real = math.sqrt(self.real** 2 + self.imaginary**2)
        return Complex(real, 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')