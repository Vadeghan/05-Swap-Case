# Coding CChallenge Week 6
# Creates a swap_case function
# swap_case.py
# By Rob Thomas
# 26/11/2017

def swap_case(a_string):
    new_string=[]
    for i in a_string:
#        print("i is:",i)
        if i==" ":
            new_string.append(i)
        elif i>"Z":
            new_string.append(i.upper())
        else:
            new_string.append(i.lower())
#        print(new_string)
    return new_string

# the star unpacks the list and return every element in the list.
print(*swap_case(input("Enter some stuff...")))
 
