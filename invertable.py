from sympy import *
A = Matrix([[5,2,-1],[2,2,2],[-1,2,5]])


def singleNicePrint(x):
    pprint(x, use_unicode=True)


def invertable(m):
    # Checks if matrix is quadratic
    if m.shape[1] == m.shape[0]:
        if m.rref()[0] == eye(3):
            singleNicePrint(m.rref()[0])
            print("Da matricen kvadratisk og på rref er lig I er den ifølge prop 4.8(PDF) invertibel")
            return
        else:
            singleNicePrint(m.rref()[0])
            print("Da matricen er kvadratisk og på rref IKKE er lig I er den ifølge prop 4.8(PDF) IKKE invertibel")
            return
    print("Da matricen ikke er kvadratisk kan den ikke være invertibel")


invertable(A)

