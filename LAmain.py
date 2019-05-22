#!/usr/bin/python3

from sympy import *
init_printing(use_unicode=True)
print("sympy importeret\nUnicode sat")

from ekspFunk15_2 import *
from egenværdi import *
from invertable import *
from diffLig import *

print("Alle scripts importeret")



# Nogle test-værdier
testM = Matrix([
        [5,2,-1],
        [2,2,2],
        [-1,2,5]
        ])

testBegVær = Matrix([
        [1],
        [0],
        [1]
        ])

def testF(t):
    return (S(1)/6)*exp(6*t)*A-(S(1)/6)*A+eye(3)
