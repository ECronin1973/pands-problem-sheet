#collatz.py
#this program asks a user to input any positive integer
#and will either divide the integer by two if it is an even number
#or else it will multiply the number by three and add one to it if it is an odd number
#until you get to a resulting number one
#Author: Edward Cronin

def collatz(n):
    while n > 1: #this will create a loop which runs as long as n is greater than one
        print(n, end=' ')
        if (n % 2): 
            # if the number is odd the following command will multiply the number by 3 and add 1 to it
            n = 3*n + 1
        else:
            # if the number is even the following command will divide the result by two
            n = n//2
    print(1, end='') #This will print the value of n in each iteration 'an amount that you get when you use a mathematical rule several times'
 
 
n = int(input(f'Please enter a positive integer: ')) #this will instruct the inoutter what is required
print('Sequence: ', end='')
collatz(n)

#sources : Google search for possible solutions on creating a program for collatz theory in python
# program uses the IF ELSE syntax to run the programme
# https://www.w3schools.com/python/python_for_loops.asp - utilised for understanding loops better

