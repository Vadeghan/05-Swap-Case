# Coding CChallenge Week 6
# Creates a swap_case function
# swap_case2.py
# By Rob Thomas
# 26/11/2017
# Ver 2.0

def swap_case(a_string):
    new_string=[]
    for i in a_string:
#        print("i is:",i)
        if i<"A":
            new_string.append(i)
        elif i>"Z":
            new_string.append(i.upper())
        else:
            new_string.append(i.lower())
#        print(new_string)
    return new_string

# the star unpacks the list and return every element in the list.
print(*swap_case(input("Enter some stuff...")))
 
