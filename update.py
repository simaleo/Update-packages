#!/usr/bin/env python3

import os
import time

#Checking for packages to update
#------------------------------------------

os.system("apt list --upgradable | cut -f1 -d/ > data.txt")

#Package update
#--------------

x = open('data.txt', 'r', encoding = 'utf-8')

mylinelist = [] # create an empty list (which must collect the words)
for line in x:
    mylinelist.append(line.strip())

mylinelist.pop(0) # deletion of the first element of the list because it is the result of the previous command 


i = 0
while i <= len(mylinelist):
    if len(mylinelist) == 0:
        os.system('clear')
        print('\nListe vide\n----------')
    else:
        os.system(f"sudo aptitude install {mylinelist[i]}")

        os.system(f"sudo aptitude safe-upgrade")
        os.system(f"sudo aptitude full-upgrade")

        os.system('clear')
        
        print(f"---------------succesfull install {mylinelist[i]}-----------------\n")
    
    x.close()
    os.system("rm -r data.txt")    
    time.sleep(6)   
    i += 1
    

    
    

