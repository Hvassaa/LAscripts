from sympy import *

def gs(*args):
    """
    Ved brug af 10.25.
    En funktion til at udskrive mellemregninger
    i Gram-Schmidt processen. Dobbeltjek evt.
    med GramSchmidt() metoden fra Sympy.

    funktionen tager en vilkårlig lang liste
    af vektorer som den udfører GramSchmidt på.

    Betydningen af det printede (u og p) stemmer 
    overens med lemma 10.25.
    """

    ulist = []

    for q in range(len(args)):
        v = args[q]
        i = str(q + 1)

        
        if q == 0:
            u = (S(1)/v.norm()) * v
            ulist.append(u)

            print("u" + i + " = ")
            pprint(u, use_unicode=True)
        else:
            p = zeros(v.shape[0], 1)
            for uk in ulist:
                p += (v.dot(uk)) * uk

            print("p" + str(q) + " =")
            pprint(p, use_unicode=True)

            print()

            u = (S(1)/(v - p).norm()) * (v - p)
            
            print("u" + i + " = ")
            pprint(u, use_unicode=True)

        print("-----------")
        print()
