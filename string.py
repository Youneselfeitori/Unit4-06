# Created by: Younes Elfeitori
# Created on: Nov 2017
# Created for: ICS3U
# This program checks to see if two strings are true or false

def check_if_true(string_one, string_two):
    
    string_one = string_1.upper()
    string_two = string_2.upper()
    
    if string_one == string_two:
        return True
    else:
        return False

# input
string_1 = raw_input("Enter string: ")
string_2 = raw_input("Enter second string: ")

# process
answer = check_if_true(string_1, string_2)

# output
print answer
