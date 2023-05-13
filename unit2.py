"""Math Problem Generator - Unit 2: Polynomial Equations

Description
============================================
This module contains code for Unit 2 functions
"""
import unit1
import sympy
import typing
from sympy.abc import x

from sympy import symbols, Function, Symbol, solve, expand, solve, Poly
from sympy.solvers.inequalities import reduce_rational_inequalities


def quotient(polynomial1, polynomial2):
    """
    Returns quotient after dividing the two polynomial functions

    Preconditions:
    - polynomial1 and polynomial2 are valid polynomial functions from <generate_polynomial>

    >>> quotient(5 * x**2 + 10 * x + 3, 2 * x + 2)
    5*x/2 + 5/2
    >>> quotient((x + 1) ** 2, x + 1)
    x + 1
    """
    f = polynomial1
    g = polynomial2
    q, r = sympy.div(f, g, domain='QQ')
    return q


def remainder(polynomial1, polynomial2):
    """
    Returns remainder after dividing the two polynomial functions

    Preconditions:
    - polynomial1 and polynomial2 are valid polynomial functions from <generate_polynomial>

    >>> quotient(5 * x**2 + 10 * x + 3, 2 * x + 2)
    -2
    >>> quotient((x + 1) ** 2, x + 1)
    0
    """
    f = polynomial1
    g = polynomial2
    q, r = sympy.div(f, g, domain='QQ')
    return r


# def factorable(degree: int, coefficient_range: typing.Tuple[int, int]) -> typing.Dict:
#     """Returns a polynomial function that is factorable and the answers
#     """
#     function_so_far = 1
#     for _ in range(degree):
#         function_so_far *= unit1.generate_polynomial(1, coefficient_range)
#     return {expand(function_so_far): solve(function_so_far)}


def generate_poly_big_small1(degree, coefficient_range: typing.Tuple[int, int]) -> list:
    """
    Generates two polynomial functions, one linear function and another one with a bigger degree (at most 6).
    degree is for the polynomial function with the bigger degree

    Preconditions:
    - 2 <= degree <= 6
    - coefficient_range != ()
    - coefficient_range[0] <= coefficient_range[1]
    """
    return [unit1.generate_polynomial(1, coefficient_range), unit1.generate_polynomial(degree, coefficient_range)]


def generate_poly_big_small2(degree1, degree2, coefficient_range: typing.Tuple[int, int]) -> list:
    """
    Generates two polynomial functions, one with a bigger degree than the other (both at most 6).
    degree1 is for the polynomial function with the smaller degree and
    degree2 is for the polynomial function with the bigger degree

    Preconditions:
    - 1 <= degree1 <= 6
    - 1 <= degree2 <= 6
    - degree1 < degree2
    - coefficient_range != ()
    - coefficient_range[0] <= coefficient_range[1]
    """
    return [unit1.generate_polynomial(degree1, coefficient_range), unit1.generate_polynomial(degree2, coefficient_range)]


# TODO: Given two functions, one bigger, one smaller, return the remiander. (from plugging in the solution of the smaller
# function ie. 2 from (x-2) into the bigger function)

# TODO: Generate two functions where the bigger one has a constant K, and with the remainder for questions
# that ask what the coffeicent is given the constant and the two functions that divide

# NOTE: It would be better if we could actually show the steps to divide the function using long or synthetic divison
# TODO: synthetic(short) division. Given a polynomial and a bionomial function

# TODO: long division Given a polynomial and a bionomial function

# TODO: factor theorem stuff
"""Factoor theorem states that x-b is a factor of polynomial P(x) iff P(b) = 0 
and ax-b is a factor if P(b/a) = 0 """

"""What we could do is, already create some factors given a degree, than expand it and return the full equation"""

# TODO: Is factor. Given a factor and a equation, check if its a factor

# Series of functions that provide 'factorable' equations such that the person has to divide one or twice and end up
# with a easily factorable equation (like quadractic or simple linear) to completely factor it
# TODO: we may have to do a little bit of hardcoding in this one.

# TODO: generate factorable cubic function. generate three factors ie x-4, x-3, 3x+2.
# combine the three factors into one equation.

# TODO: generate factorable quartic function. Generate four factors, combine the four factors into
# one equation

# TODO: rational zero theorem
# TODO: given a polynomial fucntion. a is the leading coffeicnet. b is the constant.
# The possible factors of a function is any combination of facotrs of b/factors of a.

# TODO: find possible factors rational zero thereom given a function,
# return a factor ie. if -2 is a factor than return x + 2

# TODO: inequalities of polynomials. (with factorable and nonfactorable(cubic) polynomials)

# TODO: provide the x-intercepts of a factorable polynomial. For questions for people
# to write the equation of the polynomial given a point or not
