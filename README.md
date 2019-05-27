LA-scripts til lineær algebra 2019
==================================

Her følger en liste af funktioner og en beskrivelse.

## ekspFunk(A, F):

Til at tjekke om en funktion
er en eksponentialfunktion for
en kvadratisk matrix.
Følger def. 15.2

A = den kvadratiske matrix

F = funktionen der skal tjekkes

F skal defineres som normalt:

```python
def F(t):
	return ...
```

## diffLig(A, F, v)

(Ved brug af 15.12 eller 15.15)

Til at finde at finde løsningen z til 
et differentialligningssystemet:

x' = Ax

med begyndelsesværdi v.

A = den kvadratiske matrix 

F = A's eksponential funktion

(Hvis ikke der er sådan en, skriv bare 0 i stedet)

v = begyndelsesværdien (vektor)

F skal defineres som normalt:

```python
def F(t):
	return ...
```

## gs(*args)

Ved brug af 10.25.
En funktion til at udskrive mellemregninger
i Gram-Schmidt processen. Dobbeltjek evt.
med GramSchmidt() metoden fra Sympy.

funktionen tager en vilkårlig lang liste
af vektorer som den udfører GramSchmidt på.

(så funktionen kaldes gs(v1, v2, v3 ... ))

Betydningen af det printede (u og p) stemmer 
overens med lemma 10.25.

