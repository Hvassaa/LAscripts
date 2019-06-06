#!/usr/bin/python3

from sympy import *

def ekspFunk(A, F):
    """
    Til at tjekke om en funktion
    er en eksponentialfunktion for
    en kvadratisk matrix.
    Følger def. 15.2

    A = den kvadratiske matrix
    F = funktionen der skal tjekkes

    A skal være en matrix
    F skal defineres som normalt:
        def F(t):
            <kode>...
    """

    # Tjek at matrixen faktisk er kvadratisk
    dim = A.shape
    if dim[0] != dim[1]:
        print("Matrixen er ikke kvadratisk")
        return False

    # Parameteren til funktionen
    t = symbols("t")

    # 1.
    if F(0) == eye(dim[0]):
        print("1: Da F(0)  = I er første krav opfyldt")
        print("F(0):")
        pprint(F(0))
    else:
        print("1: Fejler")
        return False

    # 2.
    if nsimplify(A*F(t))==diff(F(t),t):
        print("2: Da F' = A * F er andet krav opfyldt")
        print("F' og A*F:")
        pprint(diff(F(t),t))
    else:
        print("2: Fejler")
        return False

    # 3.
    if A*F(t)==F(t)*A:
        print("3: Da F * A = A * F er tredje og sidste krav opfyldt")
        print("F*A og A*F:")
        pprint(A*F(t))
    else:
        print("3: Fejler")
        return False

    # Alle holdte
    print("Pr. definition 15.2, er F en eksponentialfunktion for F")
    return True
