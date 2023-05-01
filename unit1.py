"""Math Problem Generator - Unit 1: Polynomial Functions

Description
============================================
This module contains code for Unit 1 functions
"""

import random
import typing
import sympy
from sympy.abc import x


# from sympy import symbols, Function, Symbol
# from sympy.plotting import plot


def generate_polynomial(degree: int, coefficient_range: typing.Tuple[int, int]):
    """
    Generates polynomial function
    Preconditions:
    - degree > 0
    - coefficient_range != ()
    """
    x_exponent = degree
    expr = random.randint(coefficient_range[0], coefficient_range[1]) * x ** degree
    for i in range(0, x_exponent):
        expr += random.randint(coefficient_range[0], coefficient_range[1]) * x ** i
        x_exponent -= 1
    return expr


# TODO: Generate factorable polynomial and/or prefactored polynomial
# Disciminatn is defined differently for different degree functions
# So we might need to put a limit to degree
# def generate_factorable_polynomial(degree: int, coefficient_range: typing.Tuple[int, int]):
#     """
#     Generates factorable polynomial.
#     Will just return a non-factored polynomial if the generated
#
#     Preconditions:
#     - degree > 1
#     - coefficient_range != ()
#     """
#     possible_factorable = sympy.factor(generate_polynomial(degree, coefficient_range))


def sympy_to_mathjax(polynomial) -> str:
    """
    Converts sympy polynomial function to mathjax syntax
    # >>> from sympy import symbols
    # >>> polynomial = x**3 + 7*x**2 + 4*x + 3
    # >>> sympy_to_mathjax(polynomial)
    # 'x^3 + 7x^2 + 4x + 3'

    Preconditions:
    - polynomial is a valid polynomial function from <generate_polynomial>
    """
    txt = str(polynomial)
    x = txt.replace("**", "^")
    y = x.replace("*", "")

    # return (y)
    return y


def end_behaviour(first_quadrant: str, second_quadrant: str, coefficient_range: typing.Tuple[int, int]):
    """
    Returns function based on end behaviour input

    Preconditions:
    - first_quadrant in ['Q1', 'Q2', 'Q3', 'Q4']
    - second_quadrant in ['Q1', 'Q2', 'Q3', 'Q4']
    - coefficient_range != ()
    """
    quadrant_list = ['Q1', 'Q2', 'Q3', 'Q4']
    if first_quadrant not in quadrant_list or second_quadrant not in quadrant_list:
        return 'Wrong Input'
    else:
        if (first_quadrant == 'Q1' and second_quadrant == 'Q2') or (first_quadrant == 'Q2' and second_quadrant == 'Q1'):
            # Even function
            degree = random.randrange(2, 7, 2)
            function = generate_polynomial(degree, coefficient_range)
            return function
        elif (first_quadrant == 'Q3' and second_quadrant == 'Q4') or (
                first_quadrant == 'Q3' and second_quadrant == 'Q4'):
            # Even function
            degree = random.randrange(2, 7, 2)
            function = generate_polynomial(degree, coefficient_range)
            return function
        elif (first_quadrant == 'Q1' and second_quadrant == 'Q3') or (
                first_quadrant == 'Q3' and second_quadrant == 'Q1'):
            # Odd function
            degree = random.randrange(1, 6, 2)
            function = generate_polynomial(degree, coefficient_range)
            return - + function
        else:
            # Odd function
            degree = random.randrange(1, 6, 2)
            function = generate_polynomial(degree, coefficient_range)
            return - + function

# Even or odd function, provide another return showing a quick proof of why the function is even or odd or neither
# TODO: function doesnt work
# def even_or_odd_function(polynomial) -> str:
#   f = Function('f')
#   if f(-polynomial) == f(polynomial):
#     return 'Even'
#   elif f(-polynomial) == -f(polynomial):
#     return 'Odd'
#   else:
#     return 'None'


# TODO: coefficent of given equation

# TODO: domain range of given equation
def function_domain(polynomial) -> sympy.polys.domains.integerring.IntegerRing:
    """
    Returns domain of polynomial

    Preconditions:
    - polynomial is a valid polynomial function from <generate_polynomial>
    """
    p = sympy.Poly(polynomial)
    return p.domain


def function_range(polynomial) -> sympy.polys.domains.integerring.IntegerRing:
    """
    Returns range of polynomial

    Preconditions:
    - polynomial is a valid polynomial function from <generate_polynomial>
    """


# TODO: table of intervals of given equation

# TODO: generate image of graph given equation, into image file. (should keep track of both image and the equation)

# TODO: number of turning points of given equation

# TODO: intercepts of given function

def x_int(polynomial):
    """
    Returns x-intercept of polynomial

    Preconditions:
    - polynomial is a valid polynomial function from <generate_polynomial>
    """
    return sympy.solveset(polynomial, x)


def y_int(polynomial):
    """
    Returns y-intercept of polynomial

    Preconditions:
    - polynomial is a valid polynomial function from <generate_polynomial>
    """
    return [polynomial.coeff(x, 0)]  # return just the y-intercept


# TODO: least possible degree of given function ie. degree of polynomial function

# Finite differences stuff

# TODO: Given a equation, generate x and y values for a simple range ie. -4-4 or -6-6

# TODO: Given a list of y's, find differences until its constant N. N is the degree of the polynomial.

# TODO: Given equation find which finite difference is constant (ie. the degree of leading coffcient), find the value
# The value is the leading coffeicnet, A multiplied by the degree N factorial. N! x A

# TODO: Given equation, write word descriptions about the function ie. x-intercept at x=, y-intercept at blah, domain, range, points

# TODO: Given variables that transform a function, return the equation, a,k,c,d values

# TODO: Given some variables of A, K, C, D return text explaining what each does

# TODO: return number of x-intercepts, turning points, least possible degree, any symmtery intervals
# where graph is positive or negative
