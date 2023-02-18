#bank.py
#This program just prints out the sum of two inputs
#Author: Edward Cronin

x = int(input("Enter amount1(in cent): ")) #this allows for capturing input 1
y = int(input("Enter amount2(in cent): ")) #this allows for capturing input 2
ans = (x/100) + (y/100) # this adds the two inputs and divides each by 100 in order to convert cent into 'euro and cent'

txt ="The sum of these is €{:.2f}" # this allows for format to be with 2 decimal places
print(txt.format(ans)) # this prints the output formatted


#source: w3schools - string format - format() displays as 2 decimal places



