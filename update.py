#!/usr/bin/env python3

import os

#Verification des packages a mettre a jours
#------------------------------------------

os.system("apt list --upgradable | cut -f1 -d/ > data.txt")

#Mise a jour des packages
#------------------------

x = open('data.txt', 'r', encoding = 'utf-8')

mylinelist = [] # crée une liste vide (qui doit recueillir les mots)
for line in x:
    mylinelist.append(line.strip())

mylinelist.pop(0) # suppression du premier element de la liste car c'est le resultat de la commande precedante 

i = 0
while i <= len(mylinelist):
    if len(mylinelist) == 0:
        os.system('clear')
        print('\nListe vide\n----------')
    else:
        os.system(f"sudo aptitude install {mylinelist[i]}")

        os.system(f"sudo aptitude safe-upgrade")
        os.system(f"sudo aptitude full-upgrade")

        x.close()
        os.system('clear')

        print(f"---------------succesfull install {i}-----------------\n")
    i += 1
    
os.system("rm -r data.txt")

   
    
    

