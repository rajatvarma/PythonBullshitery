from math import sqrt
import sys
import re

n = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
print("This is a quadratic equation calculator to find the real roots!")
print("You have to enter a quadratic equation of the form ax^2+bx+c")
equation = ""


def quadratic_equation(equation):
    parse = re.compile(r'(\d*)x\^2([+|-]\d*)x([+|-]\d)')
    mo2 = parse.search(equation)
    print(mo2.group())
    a, b, c = mo2.group(1, 2, 3)
    # print(a, b, c)
    if a == '':
        a = 1
    a = int(a)
    b = int(b)
    c = int(c)
    # print(a, b, c)
    try:
        alpha = (((-1 * b) + sqrt((b ** 2) - (4 * a * c))) / 2 * a)
        beta = (((-1 * b) - sqrt((b ** 2) - (4 * a * c))) / 2 * a)
        answer = alpha, beta
        graph_equation = str(a)+"*x**2"+str(b)+"*x"+"+"+str(c)
        return answer, graph_equation
    except:
        return "No Real Roots"
