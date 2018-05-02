#!/usr/bin/env python3

# im not sure if just hardcoding a lookup table would be more efficient
# knowing python, probably would be

# i know challenge said that there wouldnt be special chars, but one of the
# examples has a space, and it's easier to test for them all like this
swap_case = lambda i: "".join([l if not l.isalpha() else chr(ord(l)+32) if ord(l) < 91 else chr(ord(l)-32) for l in i])
