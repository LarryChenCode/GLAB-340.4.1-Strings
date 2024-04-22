print("Welcome to the GLAB!")
userInput = input("Enter a word: ")
print("The length of the word entered is ", len(userInput))
print("The uppercase of the word is ", userInput.upper())
print("The lowercase of the word is ", userInput.lower())
input("Press Enter to continue...\n")
letterInput = input("Enter a letter: ")
print("The letter ", letterInput, " appears how many times? ", userInput.count(letterInput))
input("Press Enter to continue...\n")
substringInput = input("Enter a substring: ")
print("The substring ", substringInput, " appears how many times? ", userInput.count(substringInput))
print(userInput[::-1])
input("Press Enter to continue...")
startIndex = int(input("Enter a starting number: "))
endIndex =int(input("Enter a ending number: "))
print("The world is sliced as ", userInput[startIndex:endIndex])
input("Press Enter to continue...\n")
charInput1 = input("Enter a character that you want to replace: ")
charInput2 = input("Enter a character that you want to be replaced: ")
print(userInput.replace(charInput2,charInput1))
input("Press Enter to continue...\n")
print("Now you can combine 2 words together!")
firstInput = input("Enter the first word: ")
secondInput = input("Enter the second word: ")
print("{} {}".format(firstInput, secondInput))
input("Press Enter to continue...\n")
palInput = input("Enter a word to check if it's a palindrome: ")
print("The word you typed is a palindrome?", palInput.lower() == palInput[::-1].lower())
input("Press Enter to continue...\n")
pyIdfInput = input("Enter a word to check if it's a valid python identifier: ")

def checkValid(name):
    for char in name:
        if name[0].isdigit():
            return False
        elif char.isalnum() or char == "_":
            return True
        else:
            return False
            
print("The word you typed is a valid python identifier?", checkValid(pyIdfInput))
