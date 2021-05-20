paczka = 0
suma_element = 0
suma_paczek = 0
puste_kg = 0
suma_pustych_kg = 0
suma_wysl_kg = 0
max_paczka = 20

element = input()
if element:
    element = int(element)

while element:
    if element <= 10 and paczka + element <= 20:
        print ("Kolejny element waży {}kg".format(element))
        suma_element += element
        print ("Suma elementów wynosi {}kg".format(suma_element))
        paczka += element
        print ("Ilość w paczce to {}kg".format(paczka))
    elif element > 10:
        print ("ELEMENT WAZY ZA DUŻO! ZOSTAJE POMINIĘTY.\n")
    else:
        print ("ELEMENT JEST ZA CIĘŻKI! OTWIERAM NOWĄ PACZKĘ.\n")
        puste_kg = max_paczka - paczka
        suma_pustych_kg += puste_kg
        print ("Puste kg teraz: {}".format(suma_pustych_kg))
        suma_wysl_kg += paczka
        suma_paczek += 1
        print ("Aktualna ilość paczek: {}".format(suma_paczek))
        paczka = element
        print ("Paczka waży teraz {}kg".format(paczka))
        suma_element = element
    element = input()
    if element:
        element = int(element)
suma_paczek += 1 #zamykamy ostatnią paczkę
puste_kg = max_paczka - paczka
suma_wysl_kg += paczka
suma_pustych_kg += puste_kg
print ("Koniec elementów!")
print ("Łączna ilość paczek: {}".format(suma_paczek))
print ("Łączna ilość wysłanych kg: {}".format(suma_wysl_kg))
print ("Łączna ilość pustych kg: {}".format(suma_pustych_kg))
