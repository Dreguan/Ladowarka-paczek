paczka = 0
suma_element = 0
suma_paczek = 0

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
    else:
        print ("Element jest za ciężki! Otwieram nową paczkę.")
        suma_paczek += 1
        print ("Aktualna ilość paczek: {}".format(suma_paczek))
        paczka = element
        print ("Paczka waży teraz {}kg".format(paczka))
        suma_element = element
    element = input()
    if element:
        element = int(element)
suma_paczek += 1 #zamykamy ostatnią paczkę
print ("Koniec elementów!")
print ("Łączna ilość paczek: {}".format(suma_paczek))
