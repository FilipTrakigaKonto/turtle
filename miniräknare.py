import math

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