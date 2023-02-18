#lab3.3.4-accounts.py
#This program just prints out the last four characters of a bank account
#Author: Edward Cronin

#accountno = str(input("Please enter an 10 digit account number: ")) #this allows for capturing input 1

while True:
    user_input = str(input("Please enter an 10 digit account number: "))   
 
    if len(user_input) != 10:                                       #this sets length of input to 10 characters
        print('Account number must be 10 charachers in length')     #'this gives a message if length of input does not meet criteria set down'
        continue
    else:
        display = user_input[6:]                                    #display variable is used to give output of last four digits entered
        print("XXXXXX{}".format(display))                           #command combines both text which replaces entered text and display output
        break

#Please enter an 10 digit account number: 4562587913
#XXXXXX7913


#note this programme limits input to 10 characters

#Modify the program to deal with account numbers of any length (yes that is a vague requirement, comment your assumptions)
#Answer, I am asuming that the first six characters returned as XXXXXX are still required
#I am also asuming that if there can be any length, then line 10 to 13 are not required.
# I am asuming that it will be clarified what the length of an account it and the code lines 10 - 13 are re-examined to reflect the input and subsequent output.
#if there are no max length then the accounts.py file will exclude lines 10 - 13
