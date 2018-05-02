import sys

dumbMode = False

args = sys.argv
if len(sys.argv) > 1:
	if str(sys.argv[1]).lower: #Incase people want to say "TrUe" or "TruE" or "TRUE" or "tRUE", etc
		dumbMode = True
#Easy way
if dumbMode == False:
	print((input("String to switch: ").swapcase()))

#Stupid way
else:
	print("Dumb mode on")
	def swapLetterCase(inputString):
		lowerCaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #Two Variables for upper letters and lower letters
		upperCaseLetters = "abcdefghijklmnopqrstuvwxyz"
		lowerCaseTranslations = {} #A dictionary to store the inverse of each
		upperCaseTranslation = {}
		for i in range(len(list(upperCaseLetters))): #For each in the range of the length of the list of upperCaseLetters (using this so i is an int not a string)
			lowerCaseTranslations[upperCaseLetters[i]] = lowerCaseLetters[i]  #Add to the lowerCaseTranslations by taking the index and taking the lowerCaseLetter of that
		for i in range(len(list(lowerCaseTranslations))): #Same applies as above
			upperCaseTranslation[lowerCaseLetters[i]] = upperCaseLetters[i] #Same applies as above
		
		characters = list(inputString) #Get a list of every character used
		newString = ""
		for i in characters: #Iterate over each character
			if i in lowerCaseLetters: #If the character is lowercase
				newString += upperCaseTranslation[i] #Take the uppercase version of it
			elif i in upperCaseLetters: #If the character is uppercase
				newString += lowerCaseTranslations[i] #Take the lowercase version of it
			else:
				newString += i #Else, add it as is. This for things such as spaces, exclamation points, etc.
		return newString

	print(swapLetterCase(input("String to switch: ")))
