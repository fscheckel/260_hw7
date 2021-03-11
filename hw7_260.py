import numpy as np
import math

#((G*M)/r**2)-((G*m)/((R-r)**2)=(O**2*r) for L1
#((G*M)/r**2)+((G*m)/((R-r)**2)=(O**2*r) for L2

# r=?
# G=6.674e-11
# M=1.989e30
# m=5.972e24
# R=1.496e11
# O=1.991e-7

def L1(r, G=None, M=None, m=None, R=None, O=None):
    return ((G*M)/r**2)-((G*m)/((R-r)**2)-(O**2*r)

def L1_prime(r, G=None, M=None, m=None, R=None, O=None):
    return (((-2*G*M)/(r**3))-((2*G*m)/(R-r)**3))-(O**2)

def L2(r, G=None, M=None, m=None, R=None, O=None):
    return ((G*M)/r**2)+((G*m)/((R-r)**2)-(O**2*r)

def L2_prime(r, G=None, M=None, m=None, R=None, O=None):
    return(((-2*G*M)/(r**3))+((2*G*m)/(R-r)**3))-(O**2)

def newton(func=None, deriv=None, first_guess=None, max_iterations=100):
    guess = first_guess
    for i in range(max_iterations):
        guess = guess - (func(guess) / deriv(guess))
    return guess

def secant(func=None, deriv=None, first_guess=None, max_iterations=100):
#x2 - f(x2) * (x2 - x1) / f(x2) - f(x1)
    x1 = r
    x2 = R
    top = x2 - func(x2) * (x2 - x1)
    bottom = func(x2) - func(x1)
    return top/bottom

if __name__ == "__main__":
    G=6.674*10**(-11)
    M=1.989*10**30
    m=5.972*10**24
    R=1.496*10**11
    O=1.991*10**(-7)

print("newton's method for L1", newton(func=L1, deriv=L1_prime, first_guess=10, max_iterations))
print("newton's method for L2", newton(func=L2, deriv=L2_prime, first_guess=10, max_iterations))
print("secant method for L1", secant(func=L1, deriv=L1_prime, first_guess=10, max_iterations))
print("secant method for L2", secant(func=L2, deriv=L2_prime, first_guess=10, max_iterations))