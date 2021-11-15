#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.



def reverse(strng):
    if strng=='':
        return 
    else:
        return reverse(strng[1:]) + strng[0]

print(reverse("python"))