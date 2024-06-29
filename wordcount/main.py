#This program has a function which returns the number of words in a file 
# - Akash 
import sys

def count_words(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            number_of_words = len(words)
            return number_of_words
    except FileNotFoundError:
        print("The File was not found")
        sys.exit()
print(count_words('wordw.txt'))