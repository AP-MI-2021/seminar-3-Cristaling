# În cadrul laboratorului 4, fiecare student va primi cerințele pentru primul examen parțial. Acesta valorează 30% din media notelor pe laborator.
#
# Va trebui să acceptați assignmentul și să încărcați rezolvarea în repository-ul creat astfel.
#
# Pentru rezolvarea cerințelor se recomandă să parcurgeți cursurile, seminarele și laboratoarele de până acum.
#
# În timpul testului puteți folosi orice resurse, dar nu aveți voie să comunicați între voi sau cu terțe persoane și
# nici să accesați repository-urile de github ale colegilor voștri.
#
# Să vă asigurați că puteți face share screen și că aveți webcam și microfon funcționale. Fără acestea este posibil să vă fie refuzat accesul la test.
#
# Timpul de lucru va fi de 1 oră și 30 minute.
#
# Programul se evaluează exact în forma în care este submis pe github la expirarea timpului de lucru.
#
# Orice erori la pornirea programului înseamnă notarea testului cu 1.
#
# La finalul timpului de lucru, încărcați rezolvările pe repository-ul creat prin acceptarea assignment-ului Lab 4,
# într-un fișier denumit main.py. Puteți folosi fișiere suplimentare dacă doriți, dar programul trebuie să poată fi pornit rulând doar main.py.
#
# Scrieți un program cu meniu (meniul va conține o opțiune care oprește programul) care suportă operațiile:
#
# [1p] Citirea unei liste de float-uri. Citirile repetate suprascriu listele precedente.
# [2p] Afișarea tuturor numerelor întregi din listă (de exemplu, 3 și 2.0 se consideră întregi).
# [2p] Afișarea celui mai mare număr divizibil cu un număr citit de la tastatură.
# [2p] Afișarea tuturor float-urilor ale căror parte fracționară este palindrom.
# [3p] Afișarea listei obținute din lista inițială în care float-urile cu partea întreagă a radicalului număr prim sunt puse ca
# string-uri cu caracterele în ordine inversă. Exemplu: [10.0, 100.0, 12.45, 50.0, 101.2] --> ['0.01', 100.0, '54.21', '0.05', 101.2]
# 1.00244200
# Punctajul pe fiecare cerință se acordă astfel:
#
# 50% corectitudinea implementării.
# 25% specificații scrise corect (unde se aplică) și denumiri sugestive.
# 25% teste relevante și scrise corect (unde se poate).
import math
from math import trunc, sqrt


def gaseste_intregi(lista):
    result = []

    for numar in lista:
        if numar == int(numar):
            result.append(int(numar))

    return result


def cmmn_div_k(lista, k):
    m = None

    for numar in lista:
        if numar % k == 0:
            if m is None or m < numar:
                m = numar

    return m


def get_oglindit(nr):
    oglindit = 0

    while nr > 0:
        oglindit = oglindit * 10 + nr % 10
        nr = nr // 10

    return oglindit


def is_palindrome(nr):
    oglindit = get_oglindit(nr)
    return oglindit == nr


def extract_fractionar(numar):
    return str(numar).split('.')[1]


def gaste_floats_cu_frac_palindroame(lista):
    result = []

    for numar in lista:
        frac_str = extract_fractionar(numar)
        if is_palindrome(int(frac_str)):
            result.append(numar)

    return result


def is_prime(numar):
    if numar < 2:
        return False
    if numar == 2:
        return True
    if numar % 2 == 0:
        return False
    for x in range(3, int(math.sqrt(numar)) + 1, 2):
        if numar % x == 0:
            return False
    return True


def invert_floats_with_sqrt_of_int_prim(lista):
    result = []

    for numar in lista:
        sqrt_nr = sqrt(numar)
        sqrt_int = trunc(sqrt_nr)
        if is_prime(sqrt_int):
            numar_str = invert_float_as_string(numar)
            result.append(numar_str)
        else:
            result.append(numar)

    return result


def invert_float_as_string(numar):
    numar_str = str(numar)
    return numar_str[::-1]


def citire_numar():
    return int(input("Dati un numar: "))


def citire_lista1():
    result_list = []
    dimensiune = int(input("Dimensiune lista: "))

    while dimensiune:
        element = float(input("Introduceti un element: "))
        result_list.append(element)
        dimensiune -= 1

    return result_list


def citire_lista2():
    result_list = []
    string_lista = input("Introduceti lista: ")

    string_elemente = string_lista.split(sep=" ")

    for string_element in string_elemente:
        element = float(string_element)
        result_list.append(element)

    return result_list


def main():
    stop = False
    lista = []
    while not stop:
        print("""
            1 -> Citire lista 1
            2 -> Citire lista 2
            3 -> Afisare numere intregi din lista
            4 -> Afișarea celui mai mare număr divizibil cu un număr citit de la tastatură.
            5 -> Afișarea tuturor float-urilor ale căror parte fracționară este palindrom.
            6 -> Afișarea listei obținute din lista inițială în care float-urile cu partea întreagă a radicalului număr prim sunt puse ca string-uri cu caracterele în ordine inversă.
            x -> Exit
         """)
        command = input("Alege comanda: ")
        if command == 'x':
            stop = True
        elif command == '1':
            lista = citire_lista1()
        elif command == '2':
            lista = citire_lista2()
        elif command == '3':
            lista_intregi = gaseste_intregi(lista)
            print(lista_intregi)
        elif command == '4':
            numar_dat = citire_numar()
            rezultat = cmmn_div_k(lista, numar_dat)
            print(rezultat)
        elif command == '5':
            lista_frac_palindroame = gaste_floats_cu_frac_palindroame(lista)
            print(lista_frac_palindroame)
        elif command == '6':
            result = invert_floats_with_sqrt_of_int_prim(lista)
            print(result)



main()

# lista1 = [1, 2]
# # lista2 = lista1
# lista2 = [1, 2]
#
# print(lista1 is lista2)
# print(lista1 == lista2)