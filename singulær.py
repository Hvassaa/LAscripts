from sympy import *


def singulær(m:Matrix):
    if m.shape[1] == m.shape[0]:
        if m.rref()[0] == eye(3):
            print("RREF:")
            pprint(m.rref()[0])
            print("Da matricen på RREF er lig med I overholder den de ækvevilænte udsagn i lemma 4.6, dermed er den i følge prop 4.8 invertibel og dermed ikke singulær")
            return
        else:
            print("RREF:")
            pprint(m.rref()[0])
            print("Da matricen på RREF ikke er lig med I overholder den ikke de ækvevilænte udsagn i lemma 4.6, dermed er den i følge prop 4.8 ikke invertibel og dermed singulær")
            return


