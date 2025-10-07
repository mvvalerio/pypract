# "plaindrome.py" Is a program which checks the
# word given to it and if it is a palindrome, prints
# the word but inverted, which is the same thing LOL

word = input("Write a word: ")

palindrome = "".join(list(word))[::-1]

if palindrome != word:
    print("That word isn't a palindrome !")

else:
    print(f"Palindrome: {palindrome}")
    