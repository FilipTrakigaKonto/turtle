import math
import time
import turtle


BREDD = 800
HOJD = 600
SKALA = 40
X_MIN = -10
X_MAX = 10
STEG = 0.1


screen = turtle.Screen()
screen.setup(BREDD, HOJD)
screen.title("Dålig Desmos")
screen.tracer(1)

penna = turtle.Turtle()
penna.hideturtle()
penna.speed(1)
penna.pensize(2)


TILLATET = {
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


def skarm_x(x):
    return x * SKALA


def skarm_y(y):
    return y * SKALA


def rita_axlar():
    penna.color("black")
    penna.pensize(2)

    penna.penup()
    penna.goto(-BREDD // 2 + 30, 0)
    penna.pendown()
    penna.goto(BREDD // 2 - 30, 0)

    penna.penup()
    penna.goto(0, -HOJD // 2 + 30)
    penna.pendown()
    penna.goto(0, HOJD // 2 - 30)

    penna.pensize(1)
    for x in range(X_MIN, X_MAX + 1):
        penna.penup()
        penna.goto(skarm_x(x), -5)
        penna.pendown()
        penna.goto(skarm_x(x), 5)

    for y in range(-7, 8):
        penna.penup()
        penna.goto(-5, skarm_y(y))
        penna.pendown()
        penna.goto(5, skarm_y(y))


def rakna_ut_y(ekvation, x):
    lokala_namn = TILLATET.copy()
    lokala_namn["x"] = x
    return eval(ekvation, {"__builtins__": {}}, lokala_namn)


def rita_graf(ekvation):
    penna.color("red")
    penna.pensize(3)
    penna.speed(1)

    for punkt_nr in range(int((X_MAX - X_MIN) / STEG) + 1):
        x = X_MIN + punkt_nr * STEG

        if punkt_nr % 15 == 0:
            time.sleep(0.35)

        try:
            y = rakna_ut_y(ekvation, x)
        except (ArithmeticError, ValueError, OverflowError, ZeroDivisionError):
            penna.penup()
            continue

        if not math.isfinite(y):
            penna.penup()
            continue

        sx = skarm_x(x)
        sy = skarm_y(y)

        if sy < -HOJD // 2 or sy > HOJD // 2:
            penna.penup()
            continue

        if penna.isdown():
            penna.goto(sx, sy)
        else:
            penna.penup()
            penna.goto(sx, sy)
            penna.pendown()


def main():
    print("Skriv en ekvation med x, till exempel:")
    print("sin(x), x**2, sqrt(abs(x)), eller 2*x + 1")
    ekvation = input("y = ")

    rita_axlar()
    rita_graf(ekvation)
    turtle.done()


main()
