#!/usr/bin/python3

from sympy import *

def diffLig(A, F, v):
    """
    (Ved brug af 15.12 eller 15.15)

    Til at finde at finde løsningen z til 
    et differentialligningssystemet:

    x' = Ax

    med begyndelsesværdi v.

    A = den kvadratiske matrix 

    F = A's eksponential funktion

    (Hvis ikke der er sådan en, skriv bare 0 i stedet)

    v = begyndelsesværdien (vektor)
    """

    # Tjek at matrixen er kvadratisk
    dim = A.shape
    if dim[0] != dim[1]:
        print("Matrixen er ikke kvadratisk")
        return None

    # Tjek at vektoren har den rette dimension
    if v.shape[0] != dim[0]:
        print("v har den forkerte højde")
        return None

    # Variablen/parameteren til F/z
    t = symbols("t")

    # Forsøg med 15.15
    for tup in A.eigenvects():
        for vec in tup[2]:
            if vec == v:
                # Hvis dette passer bruger kan vi bruge 15.15
                egenværdi = tup[0]
                print("Vi bruger 15.12 til at bestemme løsning z(t)")
                return S(exp(egenværdi*t)*v)

    # Ellers bruger vi 15.12, såfrem vi har en eksponential funktion
    try:
        res = S(F(t)*v)
        print("Vi bruger 15.15 til at bestemme løsning z")
        return res
    except (TypeError, RuntimeError):
        print("F er ikke funktion, held og lykke")
        return None
