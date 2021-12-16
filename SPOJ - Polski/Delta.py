# Program do delty
import math

a = int(input("Podaj X^2 "))
b = int(input("Podaj X "))
c = int(input("Podaj to kolejne coś "))

mniejszy_lub_wiekszy = input("Podaj znak (<, <=, >, >=, =)")

delta = pow(b, 2) - (4 * a * c)

def delta_i_X():

    if delta >= 0:
        delta_sqrt = math.sqrt(delta)

    if delta > 0:
        x1 = ((-b + delta_sqrt) / 2 * a)
        x2 = ((-b - delta_sqrt) / 2 * a)
        print(x1, x2)

    if delta < 0:
        print("Delta nie istnieje")

    if delta == 0:
        x1 = ((-b + delta_sqrt) / 2 * a)
        print(x1)

    print(f"Delta to {delta_sqrt}")

    if mniejszy_lub_wiekszy == "<":
        print(f"X E od -nieskończoność; do {x1} U {x2} do nieskończonośc +")
    if mniejszy_lub_wiekszy == ">":
        print(f"X E od {x1} do {x2}")
    if mniejszy_lub_wiekszy == '=':
        print(f"x1 = {x1} x2 = {x2}")


delta_i_X()