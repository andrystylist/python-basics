from ast import Div, Mult
from difflib import Differ
from pdb import Restart
from unittest.case import DIFF_OMITTED


numero: int = 10
otro: int = 3

suma: int = (10 + otro)
div: float = (10 / otro)
abs_div: int = (10 // otro)
mult: int = (10 * otro)
modulo: int = (10 % otro)
resta: int = (10 - otro)

if __name__ == "__main__":
    print(__name__)
    print(f"sum: {suma}")
    print(f"div: {div}")
    print(f"abs_div: {abs_div}")
    print(f"mult: {mult}")
    print(f"modulo: {modulo}")
    print(f"resta: {resta}")
