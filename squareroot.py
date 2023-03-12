#squareroot.py
#this program, takes a positive floating point number as input
# and outputs an approximation of its square root
# Author: Edward Cronin

num = float(input(f"Please enter a positive number: "))
positiveNum = (abs(num)) # this causes the number if inputted as negative to turn positive

#main program - this takes input in positiveNum and calculates its square root using newton method
# 0.5*(approx+n/approx) is the Newton method to find the square root of the number

def sqrt(PositiveNum, base):  # function titled 'sqrt' is created 
    approx_root = 0.5 * positiveNum 
    for i in range(base):
        moreapprox = 0.5 * (approx_root + positiveNum/approx_root)
        approx_root = moreapprox
    return moreapprox

print(f"the square root of {positiveNum} is approx. ",sqrt(positiveNum, 10))

