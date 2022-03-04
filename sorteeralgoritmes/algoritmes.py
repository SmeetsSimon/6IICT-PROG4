import random

# Vooraleer het algoritme hier te implementeren. Probeer het eerst met een kleine lijst in test.py

# Het bubbel_sort algoritme, deze is gegeven ter verduidelijking van de werking van generatoren
def bubbel_sort(lijst):
    for i in range(len(lijst)-1): #We kijken naar huidig en volgend blok
        for j in range(len(lijst)-1-i):
            waarde1 = lijst[j]
            waarde2 = lijst[j+1]

            if (waarde1 > waarde2):
               #lijst[j], lijst[j+1] = lijst[j+1], lijst[j] #Snellere methode om onderstaande te bereiken
               tmp = lijst[j]
               lijst[j]=lijst[j+1]
               lijst[j+1]=tmp

               yield j, j+1 # Volgorde: Groen blok (links), Rood blok (rechts)

# Het insertion_sort algoritme
def insertion_sort(lijst):
    pass

# Het bozo_sort algoritme. Gebruik als yield -2. Alle blokken worden tegelijk gewisseld. Een actief blok aanduiden is dus niet mogelijk
def bozo_sort(lijst):
    pass

# Extra: probeer het merge_sort algoritme te bouwen. Tip: het internet is je vriend





        
        

