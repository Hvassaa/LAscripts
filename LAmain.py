#!/usr/bin/python3

from sympy import *
init_printing(use_unicode=True)
print("sympy importeret\nUnicode sat")

from ekspFunk import *
from egenværdi import *
from invertable import *
from diffLig import *
from mindsteKvadrater import *
from singulær import *
from sympy import *
from nulrum import *
from gs import *
init_printing(use_unicode=True)
print("sympy importeret\nUnicode sat")



print("Alle scripts importeret")



# Nogle test-værdier
testM = Matrix([
        [1,-1,0],
        [-1,0,1],
        [0,1,-1]
        ])

testBegVær = Matrix([
        [1],
        [0]
        ])

def testF(t):
    return (S(1)/6)*exp(6*t)*A-(S(1)/6)*A+eye(3)

