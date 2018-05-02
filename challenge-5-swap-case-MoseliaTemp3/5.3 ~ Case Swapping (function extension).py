#Made by Marika Colby (12.10)

# I'm assuming that comments don't count towards the extension line limit. This time I tried to make 
# a function that worked without the swapcase() method, and the commented script is basically how it
# works. First I use ord() to find the unicode code point of the first character, and see if it is
# in the range of capital letters, then I return the upper or lower of that character as required
# and move on if needed. This works with punctuation as well, because they are unaffected. All of it
# was then bundled up in ternary conditionals (note: there can only be one return statement per
# line, so it goes at the front before any ternary conditionals).
#
##  def swap_case(Input)
##      if ord(Input[0]) in range(65, 91):
##        if len(Input) == 1:
##              return Input[0].lower()
##          else:
##              return Input[0].lower() + swap_case(Input[1:])
##      else:
##          if len(Input) == 1:
##              return Input[0].upper()
##          else:
##              return Input[0].upper() + swap_case(Input[1:])


def swap_case(Input): return (((Input[0].lower()) if (len(Input) == 1) else (Input[0].lower() + swap_case(Input[1:]))) if (ord(Input[0]) in range(65, 91)) else ((Input[0].upper()) if (len(Input) == 1) else (Input[0].upper() + swap_case(Input[1:]))))
while True: print("\nSwapping the case of that string returns:\n    " + swap_case(input("\nWhat string would you like to swap the case of?\n  > ")) + "\n\n================================")
