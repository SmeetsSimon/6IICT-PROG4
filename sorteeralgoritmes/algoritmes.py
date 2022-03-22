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
    for step in range(1, len(lijst)):
        key = lijst[step]
        j = step - 1
             
        while j >= 0 and key < lijst[j]:
            lijst[j + 1] = lijst[j]
            j = j - 1
    
        lijst[j + 1] = key
    # for i in range(len(lijst)):         
    #      waarde = lijst[i]               
    #      for j in range(0, i):         
    #          if waarde<lijst[j]:         
    #              waarde, lijst[j] = lijst[j], waarde  
    #      lijst[i] = waarde 


# Het bozo_sort algoritme. 
def bozo_sort(lijst):
    
    status = [False]
    while True:
        if False in status:
            True
            random.shuffle(lijst)
        else:
            False
        status = []
        for i in range(len(lijst) - 1):  
            waarde1 = lijst[i]
            waarde2 = lijst[i + 1]
            yield -2, -2
            if waarde1 < waarde2:
                status.append(True)
            else:
                status.append(False)
                break






        
        

