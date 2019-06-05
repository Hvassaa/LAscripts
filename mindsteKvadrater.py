from sympy import *
init_printing(use_unicode=True)

α, β, γ, δ, ϵ, ζ = symbols("α, β ,γ, δ, ϵ, ζ")


def singleNicePrint(x):
    pprint(x, use_unicode=True)


def mindsteKvadrater(A,b):
    """
    Her bruges prop. 10.42 til at finde alle mindstes kvadraters løsninger.

    Vær opmærksom på hvordan du laver din vector.
    b=Matrix([[4],[4],[4]]) giver:
    ⎡4⎤
    ⎢ ⎥
    ⎢4⎥
    ⎢ ⎥
    ⎣4⎦

    :param A: Matrix
    :param b: Vector(Matrix)
    """
    print("jvf. prop. 10.42(pdf 2019) kan mindstes kvadraters løsninger findes på følgende måde:")
    ATA = Matrix(transpose(A) * A)
    print("AᵀA = ")
    pprint(ATA)
    ATb = Matrix(transpose(A)*b)
    print("Aᵀb=")
    pprint(ATb)
    print()
    system = ATA.col_insert(ATA.shape[1], ATb)
    print("Nu løses ligningsystemet:")
    pprint(system)
    print("RREF:")
    pprint(system.rref()[0])
    if ATA.shape[0] == 1:
        print("Med variablen α")
        singleNicePrint(solve_linear_system(system, α))
    if ATA.shape[0] == 2:
        print("Med variabler α, β")
        singleNicePrint(solve_linear_system(system, α, β))
    if ATA.shape[0] == 3:
        print("Med variabler α, β, γ")
        singleNicePrint(solve_linear_system(system, α, β, γ))
    if ATA.shape[0] == 4:
        print("Med variabler α, β, γ, δ")
        singleNicePrint(solve_linear_system(system, α, β, γ, ϵ))
    if ATA.shape[0] == 5:
        print("Med variabler α, β, γ, δ, ϵ")
        singleNicePrint(solve_linear_system(system, α, β, γ, ϵ))
    if ATA.shape[0] == 6:
        print("Med variabler α, β, γ, δ, ϵ, ζ")
        singleNicePrint(solve_linear_system(system, α, β, γ, ϵ, ζ))
    print("HJÆLP TIL FORSTÅELSE:")
    print("α er første ubekendte, β anden osv...")
    print("Hvis en variabel ikke fremgår i på venstresiden af et kolon er det fordi den er fri")

def mindsteKvadrater2(_M, _B):
    nTotalM = _M.T * _M
    nTotalB = _M.T * _B
    nTotal = nTotalM.row_join(nTotalB)
    nTotalRREF = nTotal.rref()[0]
    nDone = (_M.nullspace()[0] * α) + nTotalRREF.col(-1)

    print("\n\u262D Normalligningen (Brugt til MKL) (M^T * M)x = M^T * B :")
    print("MKL = Mindste Kvadraters Løsninger")
    pprint(nTotalM, use_unicode=True)
    print(" = ")
    pprint(nTotalB, use_unicode=True)
    print("Normalligningen på RREF:")
    pprint(nTotalRREF, use_unicode=True)
    print("Normalligningen færdig:")
    pprint(nDone, use_unicode=True)
    print()
