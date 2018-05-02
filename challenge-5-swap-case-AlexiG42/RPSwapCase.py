def swap_case(string):
    if string == "": return ""
    elif string[0].isupper(): return string[0].lower() + swap_case(string[1:])
    else: return string[0].upper() + swap_case(string[1:])

print(swap_case('Hello, World! 23986'))

# Originally, I'd uploaded a different version of the program that was five lines long,
# but removed it about 10 minutes later when I remembered that recursion was a thing I could use.
#
# Basically, how this works is by returning the case-inverted version of the first character,
# concatenated with the entire rest of the string run through the function again.
#
# Also, the function works for any string, even if it has numbers or special characters! So that's nice.
#
# (and yes, I could have used exec() to get the entire function on a single line,
# or used the inbuilt .swapcase() method,
# but those would have been both (a) cheating and (b) way less cool)



