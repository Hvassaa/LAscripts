#!/usr/bin/python3

from sympy import *

def ekspFunk15_2(A, F):
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
        print("1: Holder")
    else:
        print("1: Fejler")
        return False

    # 2.
    if nsimplify(A*F(t))==diff(F(t),t):
        print("2: Holder")
    else:
        print("2: Fejler")
        return False

    # 3.
    if A*F(t)==F(t)*A:
        print("3: Holder")
    else:
        print("3: Fejler")
        return False

    # Alle holdte
    return True
