from sympy import *

def singleNicePrint(x):
    pprint(x, use_unicode=True)


def egenvalue(m: Matrix):
    """
    !!Hvis du skal finde egenværdier til en lineæroperator!!
    !!fortæller def 12.25 og prop 12.26 at du kan bruge   !!
    !!matrixræpresentationen : v[L]v og finde egenværdier !!
    !!for denne. BEMÆRK at begge baser i ræp er de samme  !!
    Laver først det karekteristiske poly med def 12.17
    Herefter findes egenværdier med prop 12.18
    Til sidst findes egenrum for hver af egenværdierne med lemma 12.11

    :param m: Matrix
    """
    # Først laves det karekteristiske P :
    t = symbols("t")
    P = det(m-eye(m.shape[0])*t)
    eV = solve(P)
    print("Det karekteristiske polynomiom jvf. def 12.17(pdf):")
    singleNicePrint("P = " + str(P))
    print("Jvf. prop 12.18(pdf) kan man nu finde egenværdier ved at løse P = 0:")
    singleNicePrint(eV)
    print("Jvf. Lemma 12.11 findes egenrummene:")
    for e in eV:
        eR = (m - e*eye(m.shape[0])).nullspace()
        print("E("+str(e)+") :")
        singleNicePrint(eR)


