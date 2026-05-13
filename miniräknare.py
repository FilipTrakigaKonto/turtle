import math
import _tkinter as tk #i need help i dont understand this
import cmath


matte = {
    "abs": abs,
    "acos": math.acos,
    "asin": math.asin,
    "atan": math.atan,
    "ceil": math.ceil,
    "cos": math.cos,
    "e": math.e,
    "exp": math.exp,
    "floor": math.floor,
    "log": math.log,
    "log10": math.log10,
    "pi": math.pi,
    "pow": pow,
    "sin": math.sin,
    "sqrt": math.sqrt,
    "tan": math.tan,
    "fac": math.factorial,
    "fmod": math.fmod,
    "remainder": math.remainder,
    "dist": math.dist,
    "deg": math.degrees,
    "rad": math.radians,
    "comp": cmath.phase,
    "polar": cmath.polar,
    "rec": cmath.rect,
    "cexp": cmath.exp,
    "clog": cmath.log,
    "clog10": cmath.log10,
    "csqrt": cmath.sqrt,
    "casin": cmath.asin,
    "cacos": cmath.acos,
    "catan": cmath.atan,
    "csin": cmath.sin,
    "ccos": cmath.cos,
    "ctan": cmath.tan,
    "casin": cmath.asin,
    "cacos": cmath.acos,
    "catan": cmath.atan,
    "casinh": cmath.asinh,
    "csinh": cmath.sinh,
    "cacosh": cmath.acosh,
    "ccosh": cmath.cosh,
    "catanh": cmath.atanh,
    "ctanh": cmath.tanh,
    "cisinf": cmath.isinf,
    "cinf": cmath.inf

}


def rakna_ut_y(ekvation, x):
    IDK = matte.copy()
    IDK["x"] = x
    return eval(ekvation, IDK)


def main():
    print("Skriv en ekvation med x, till exempel:")
    print("sin(x), x**2, sqrt(abs(x)), eller 2*x + 1")
    ekvation = input("y = ")
    print("om du inte har x i ekvationen så skriv 0")
    x = float(input("x = "))
    print(rakna_ut_y(ekvation, x))

main()