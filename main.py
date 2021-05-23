paczka = 0
suma_element = 0
suma_paczek = 0
puste_kg = 0
suma_pustych_kg = 0
suma_wysl_kg = 0
max_paczka = 20
licznik = 1
najwiecej_pustych = 0
ktora_paczka = 0

element = input()
if element:
    element = float(element)
print ("Numer paczki: {}".format(licznik))
while element:
    if element > 10:
        print ("ELEMENT WAŻY ZA DUŻO! {}KG ZOSTAJE POMINIĘTY.".format(element))
        #print ("ELEMENT WAŻY ZA DUŻO!")
        #break
    elif element > 1 and paczka + element <= max_paczka:
        print ("Kolejny element waży {}kg".format(element))
        suma_element += element
        print ("Suma elementów wynosi {}kg".format(suma_element))
        paczka += element
        print ("Ilość w paczce to {}kg".format(paczka))
    elif element == 0:
        print ("ELEMENT NIC NIE WAŻY! KONIEC PAKOWANIA.\n")
        break
    else:
        print ("ELEMENT JEST ZA CIĘŻKI DO TEJ PACZKI! OTWIERAM NOWĄ PACZKĘ.\n")
        puste_kg = max_paczka - paczka
        suma_pustych_kg += puste_kg
        print ("Puste kg w paczce nr {}: {}.".format(licznik,puste_kg))
        print ("Puste kg teraz razem: {}".format(suma_pustych_kg))
        if puste_kg > najwiecej_pustych:
            najwiecej_pustych = puste_kg
            print ("Najwięcej pustych kg w paczce to {}kg.\n".format(najwiecej_pustych))
            ktora_paczka += 1
        else:
            print ("Najwięcej pustych kg w paczce to {}kg.\n".format(najwiecej_pustych))
        suma_wysl_kg += paczka
        suma_paczek += 1
        print ("Aktualna ilość paczek: {}".format(suma_paczek))
        licznik += 1
        print ("Numer paczki: {}".format(licznik))
        paczka = element
        print ("Paczka waży teraz {}kg".format(paczka))
        suma_element = element
    element = input()
    if element:
        element = float(element)
if paczka:
    suma_paczek += 1 #zamykamy ostatnią paczkę
    puste_kg = max_paczka - paczka
    suma_wysl_kg += paczka
    suma_pustych_kg += puste_kg
    print("Puste kg w paczce nr {}: {}.".format(licznik, puste_kg))
    print("Puste kg teraz: {}".format(suma_pustych_kg))
    if puste_kg > najwiecej_pustych:
        najwiecej_pustych = puste_kg
        print("Najwięcej pustych kg w paczce to {}kg.\n".format(najwiecej_pustych))
        ktora_paczka += 1
    else:
        print("Najwięcej pustych kg w paczce to {}kg.\n".format(najwiecej_pustych))
    print ("Koniec elementów.\n")
print ("Łączna ilość paczek: {}".format(suma_paczek))
print ("Łączna ilość wysłanych kg: {}".format(suma_wysl_kg))
print ("Łączna ilość pustych kg: {}".format(suma_pustych_kg))
print ("Najwięcej pustych kg było w paczce nr {} -> {}kg.".format(ktora_paczka, najwiecej_pustych))

