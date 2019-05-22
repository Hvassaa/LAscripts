from sympy import *
A=Matrix([[5,2,-1],[2,2,2],[-1,2,5]])

def singleNicePrint(x):
    pprint(x, use_unicode=True)


def egenvalue(m: Matrix):
    # Først laves det karekteristiske P :
    t = symbols("t")
    P = det(m-eye(m.shape[0])*t)
    eV = solve(P)
    print("Det karekteristiske polynomiom jvf. def 12.17(pdf):")
    singleNicePrint("P = " + str(P))
    print("Jvf. prop 12.18(pdf) kan man nu finde egenværdier ved at løse P = 0:")
    singleNicePrint(eV)
    print("Jvf. Lemma 12.11 findes de to egenrum:")
    for e in eV:
        eR = (m - e*eye(m.shape[0])).nullspace()
        print("E("+str(e)+") :")
        singleNicePrint(eR)


egenvalue(A)

