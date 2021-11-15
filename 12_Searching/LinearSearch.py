#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# Searching algorithms - Linear Search

def linearSearch(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1 


print(linearSearch([20,40,30,50,90], 90))
try:
    print([20,40,30,50,90].index(90))
    print([20,40,30,50,90].index(10))
except:
    print("Not Found")