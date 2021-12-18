import numpy as np
import math

Inst = []

with open('Day4.txt', 'r') as l:
    lines = l.readlines()

losy = [17,2,33,86,38,41,4,34,91,61,11,81,3,59,29,71,26,44,54,89,46,9,85,62,23,76,45,24,78,14,58,48,57,40,21,49,7,99,8,56,50,19,53,55,10,94,75,68,6,83,84,88,52,80,73,74,79,36,70,28,37,0,42,98,96,92,27,90,47,20,5,77,69,93,31,30,95,25,63,65,51,72,60,16,12,64,18,13,1,35,15,66,67,43,22,87,97,32,39,82]
losyexe = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
#losy = losyexe
losy = list(map(str, losy))

#Definiowanie plansz
class Plansza:
    def __init__(self, T):
        self.wyniki = np.zeros((5,5))
        self.plansza = np.asmatrix(T)

#Inicjowanie plansz z textu
linie = int(math.ceil(float(len(lines))/6))
for n in range(linie):
    l = (6*n)
    A = lines[l].split()
    B = lines[l+1].split()
    C = lines[l+2].split()
    D = lines[l+3].split()
    E = lines[l+4].split()

    T = [A, B, C, D, E]
    P = Plansza(T)
    Inst.append(P)


#Funkcje
def Sprawdzanko(Plansza, Los):
    test = Plansza.plansza
    result = np.where(test == Los)
    if len(result[0]) == 1:
        x = result[0][0]
        y = result[1][0]
        Plansza.wyniki[x][y] = 1

def Wygrana(Plansza):
    win = [1,1,1,1,1]
    for n in range(5):
        if np.all(Plansza.wyniki[n,:]) == 1:
            return 'WINNER WINNER, CHICKEN DINNER!'
        if np.all(Plansza.wyniki[:,n]) == 1:
            return 'WINNER WINNER, CHICKEN DINNER!'

def Losowanie(Losy):
    for los in Losy:
        for obj in Inst:
                Sprawdzanko(obj, los)
                if Wygrana(obj) == 'WINNER WINNER, CHICKEN DINNER!':
                    return [obj, los]

def Losowanie2(Losy):
    for los in Losy:
        Instcopy = Inst[:]
        for obj in Instcopy:
                Sprawdzanko(obj, los)
                print
                if len(Inst) == 1 and Wygrana(obj) == 'WINNER WINNER, CHICKEN DINNER!':
                    return [obj, los]
                else:
                    if Wygrana(obj) == 'WINNER WINNER, CHICKEN DINNER!':
                        Inst.remove(obj)



def Punkty(Plansza):
    a = Plansza.wyniki
    pktzero = 0
    pktjeden = 0
    jeden = np.where(a == 1)
    zero = np.where(a == 0)
    n = len(zero[0])
    for i in range(n):
        x = zero[0][i]
        y = zero[1][i]
        pktzero += int(Plansza.plansza[x, y])

    return pktzero



pierwsza = Losowanie2(losy)

Suma = int(Punkty(pierwsza[0]))
Ostatnia = int(pierwsza[1])
print(pierwsza[0].wyniki)
print(pierwsza[0].plansza)

print(Suma*Ostatnia)
