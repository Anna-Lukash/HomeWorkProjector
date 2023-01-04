'''1. Write a program that generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
To each file append a random number between 1 and 100.
Create a summary file (summary.txt) that contains name of the file and number in that file:
A.txt: 67
B.txt: 12
Z.txt: 98'''
  
from random import randint
import string
#looping through alphabet and creating a new file to each charecter and writing random number in it
for char in string.ascii_uppercase:
    with open(char + '.kek', 'w') as f:
        c = str(randint(1, 100))
        f.write(str(c))
        # creating new file and adding name of the previous file and it's content
        with open('sumarry.txt', "a") as new_f:
            new_f.write(f.name + ":" + c + '\n')