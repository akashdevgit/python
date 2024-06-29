#This program aims to calculate execution time of a python script in seconds 
#Idea: Store initiation time in a variable called 'timestart' and completion time in a variable called 'timeend' and get the difference between them to compute execution time 
# - Akash 

import time 

timestart = time.time() 

word = "Akash" 
word += "CSE"
print(word)



timeend = time.time() 

print(f"\The execution time of the program is {timeend-timestart}")
