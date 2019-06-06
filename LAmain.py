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

print("Alle scripts importeret")

testA=Matrix([[5,2,-1],[2,2,2],[-1,2,5]])

def testF(t):
    return (S(1)/6)*exp(6*t)*testA-(S(1)/6)*testA+eye(3)

ekspFunk(testA,testF)
