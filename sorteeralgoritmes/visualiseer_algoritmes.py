import pygame
import random

import algoritmes as a
from constants import Kleur, Fonts

pygame.init()

# Deze klasse is een container voor alle informatie op de display
class Displayinformatie:
    # Deze klasse heeft twee constante variabele: 
    # een padding aan de zijkanten gelijk aan 50*2px
    # een padding aan de bovenkant gelijk aan 150px

    def __init__(): # vul input in OBV onderstaande vereisten
        # In deze methode moet een object van Displayinformatie volgende zaken bijhouden:
        # De breedte van de display
        # De hoogte van de display

        # Creëer via pygame een display met de juiste breedte en hoogte
        # Geef de display de caption "sorteeralgoritmes"
        
        # Object zal ook de lijst + een aantal extra parameters over de lijst bijhouden. 
        # Deze zetten we niet in __init__(). Want het moet mogelijk zijn om de lijst te resetten
        # Daarom plaatsen we deze in een aparte methode
        # Roep de methode set_lijst() op

        pass

    def set_lijst(self, lijst): 
        # In deze methode moet het object volgende zaken bijhouden:
        # De lijst die hij zal visualiseren. Deze lijst bestaat uit een aantal unieke waardes, gegenereerd via de functie genereer_begin_lijst()
        # De minimum waarde in deze lijst
        # De maximum waarde in deze lijst

        # Hiernaast zal het object ook de breedte van een blok, de (eenheids)hoogte van een blok moeten onthouden en de startpositie van het linkse blok
        # moeten onthouden 
        # blok_breedte: Breedte van een blok (hou rekening met padding). Omgezet naar een integer
        self.blok_breedte = ...
        # blok_hoogte: Hoogte van het blok met de laagste waarde. Omgezet naar een integer (geg)
        self.blok_hoogte = int((self.hoogte - self.PADDING_HOOGTE) / (self.max_waarde-self.min_waarde)) 
        # De beginpositie waarop het eerste blok getekend mag worden. Omgezet naar een integer
        self.begin_x = ...
        

# Functie om lijst te genereren
def genereer_begin_lijst(): # Vul input aan OBV onderstaande vereisten
    # return een lijst OBV het aantal blokken, de min_waarde van het kleinste blok en de max_waarde van het hoogste blok
    # De lijst mag geen blokken hebben waarvan de waardes gelijk zijn. 
    # Tip: Je zoekt een functie uit de random module
    lijst = ...

    return lijst

# Functie om statische onderdelen van de display eenmalig te tekenen
def teken_scherm_statisch(): # Vul input aan OBV onderstaande vereisten
    # Maak om te beginnen de display compleet wit

    # Er zijn twee statische onderdelen:
    # instructies (Kleur=zwart, hoogte=5, breedte=centered, font=normaal): Bevat uitleg over hoe de simulatie te resetten/starten
    # algoritmes (Kleur=zwart, hoogte=35, breedte=centered, font=normaal) : Bevat uitleg over hoe te wisselen tussen verschillende algoritmes
    # Tip: Gebruik render() en blit() om de tekst op de display te zetten
    # Tip: het is mogelijk om de breedte van de geschreven tekst op te vragen
    
    instructies = font.FONT_NORMAAL.render(...)
    display_info.display.blit(...)

    algoritmes = font.FONT_NORMAAL.render(...)
    display_info.display.blit(...)

# Functie om het huidig geactiveerde algoritme te tekenen
def teken_actief_algoritme(): # Vul input aan OBV onderstaande vereisten
    # Maak om te beginnen het deel waarop het algoritme zich bevindt wit
    # Teken hiervoor een rechthoek op de display met de juiste dimensies
    # Zie verder voor vereisten van het tekenen

    te_wissen_rechthoek = ...
    pygame.draw.rect(..., ..., te_wissen_rechthoek)

    # Er is een onderdeel:
    # sorteermethode (Kleur=groen, hoogte=70, breedte=centered, font=groot): Zegt welk algoritme actief is
    sorteermethode = font.FONT_GROOT.render(f"Actief: ")
    display_info.display.blit(...)

# Functie om de huidige staat van de lijst te tekenen
# De "actieve blokken" krijgen de kleuren rood en groen
def teken_lijst():  # Vul input aan OBV onderstaande vereisten

    # Wis deel waarop de blokken zich bevonden terug wit
    te_wissen_rechthoek = ...
    pygame.draw.rect(..., ..., te_wissen_rechthoek)

    # Overloop alle waarden in de lijst. (Tip: Je zal zowel de waarde van een blok als zijn index in de lijst nodig hebben)
    # x: Op welke x-positie bevindt dit blok zich.
    # y: op welke y-positie bevindt dit blok zich. (Gegeven)
    # kleur: kleur van het blok. Gebruik Gradient en de index van het blok om ervoor te zorgen dat de drie kleuren grijs zich afwisselen.
    #        maar... als de index van het blok overeenkomt met een actief blok, moet deze de overeenkomende kleur krijgen
    #        (Tip: Geef een dictionary als input, zo kan je meteen index en kleur linken)
       
    for i, waarde in ...:
        x = ...  
        y = display_info.hoogte - (waarde - display_info.min_waarde) * display_info.blok_hoogte
        blok_kleur = ...

        if i in actieve_blokken:
            ...

        pygame.draw.rect(...)

# Main-functie
def main():
    # Enkele start-parameters
    run = True
    sorteren = False
    klok = pygame.time.Clock() 

    # Hoeveel blokken we willen sorteren en tussen welke waardes ze zich bevinden (Let op: hoe groter de lijst, hoe langer het duurt)
    n = ...
    min_waarde = ...
    max_waarde = ...

    lijst = genereer_begin_lijst(...)
   
    # Creëer objecten van de klasses Kleur, Fonts en Displayinformatie
    kleur = ...
    font = ...
    display_info = ... # Het scherm heeft een breedte van 800px en een hoogte van 600px

    # Hou bij welk algoritme momenteel actief is. Zet generator klaar (Geg)
    actief_algoritme = a.bubbel_sort
    actief_algoritme_generator = None

    # Teken eerste versie van de display.
    teken_scherm_statisch(...)
    teken_actief_algoritme(..., "Bubbel sort")
    teken_lijst(...) # In eerste instantie zijn er nog geen "actieve blokken", geef daarom een leeg dictionary mee

    while run:
        # Laat programma lopen op 60 FPS
        # Update de display (gebruik hiervoor een functie van pygame)

        # We zullen een generator gebruiken om door het algoritme te lopen
        # Een generator zal onthouden wat zijn huidige staat is, wanneer deze wordt onderbroken
        # Op deze manier blijven wij toegang krijgen tot de knoppen, zelfs terwijl het algoritme sorteert!
        # Als je nog niet bekend bent met generators. Zoek wat tutorials op en maak wat simpele oefeningen (bvb in test.py)
        if sorteren:
            try:
               i, j = next(actief_algoritme_generator)
               teken_lijst(...) # Vul de dictionary in met i = groen, j = rood 
            except StopIteration: # Als de lijst helemaal doorlopen geeft de generator deze error
                sorteren = False
                teken_lijst(...) # Teken de lijst een laatste maal. Dit zodat alle blokken een grijze-gradient hebben.

        # Creëer de keyhandles voor de simulatie:
        # QUIT: Simulatie moet stoppen met "runnen"

        # r: De simulatie moet resetten. Dit betekent dat het sorteren stopt en er een nieuw lijst gegenereerd wordt
        #    (Vergeet niet om deze nieuwe lijst in display_info te "setten" en te tekenen op de display)
        # spatie: Start met sorteren
        # b: Zet het actief_algoritme naar bubbel_sort en verander actief algoritme op display naar "Bubbel sort"
        #    Deze toets mag enkel iets doen zolang het programma niet aan het sorteren is.
        # i: Zet het actief_algoritme naar insertion_sort en verander actief algoritme op display naar "Insertion sort"
        #    Deze toets mag enkel iets doen zolang het programma niet aan het sorteren is.
        # z: Zet het actief_algoritme naar bozo_sort en verander actief algoritme op display naar "Bozo sort"
        #    Deze toets mag enkel iets doen zolang het programma niet aan het sorteren is.

    # Stop pygame als de "QUIT" toets is ingeduwd.
    pygame.quit()


# Zorgt ervoor dat de main functie uitgevoerd wordt, maar enkel indien het bestand sorteer_algoritme.py uitgevoerd wordt.
if __name__ == "__main__":
    main()
