# Greeting 
print("Welcome to the GLAB! Are you ready?")
input("Press Enter to continue...\n")

# Ask the user for a word and show the length, uppercase, and lowercase
print("You will be asked several questions to play with string.")
userInput = input("Enter a word: ")
print("The length of the word entered is ", len(userInput))
print("The uppercase of the word is ", userInput.upper())
print("The lowercase of the word is ", userInput.lower())
input("Press Enter to continue...\n")

# Ask the user for a letter and show how many time it appears in the word he/she entered in the last question
print("Check how many times a letter you enter appears?")
letterInput = input("Enter a letter: ")
print("The letter ", letterInput.lower(), " appears how many times? ", userInput.lower().count(letterInput.lower()))
input("Press Enter to continue...\n")

# Ask the user for a substring and show how many time it appears in the word he/she entered in the first question
print("Check how many times a substring you enter appears?")
substringInput = input("Enter a substring: ")
print("The substring ", substringInput.lower(), " appears how many times? ", userInput.lower().count(substringInput.lower()))
input("Press Enter to continue...\n")

# Show the reversed word that the user entered
print("Show the reversed version of the word: \n", userInput[::-1])
input("Press Enter to continue...\n")

# Ask the user what parts of the word he/she wants to show
print("Now you can decide what parts of the word he/she wants to show")
startIndex = int(input("Enter a starting number: "))
endIndex =int(input("Enter a ending number: "))
print("The world is sliced as ", userInput[startIndex-1:endIndex+1])
input("Press Enter to continue...\n")

# Ask the user what character he/she wants to replace
charInput1 = input("Enter a character that you want to replace: ")
charInput2 = input("Enter a character that you want to be replaced: ")
print(userInput.replace(charInput2,charInput1))
input("Press Enter to continue...\n")

# Ask the user to enter two new words and combine it together with a space in between
print("Now you can combine 2 words together!")
firstInput = input("Enter the first word: ")
secondInput = input("Enter the second word: ")
print("The output is {} {}".format(firstInput, secondInput))
input("Press Enter to continue...\n")

# Ask the user to enter a new word and check if it's is a palindrome
palInput = input("Enter a word to check if it's a palindrome: ")
print("The word you typed is a palindrome?", palInput.lower() == palInput[::-1].lower())
input("Press Enter to continue...\n")

# Ask the user to enter a new word and check if it can be a avalid python identifier
pyIdfInput = input("Enter a word to check if it's a valid python identifier: ")
print("The word you typed is a valid python identifier?", pyIdfInput.isidentifier())

