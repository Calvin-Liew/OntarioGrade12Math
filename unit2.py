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
    return [unit1.generate_polynomial(degree1, coefficient_range),
            unit1.generate_polynomial(degree2, coefficient_range)]


# TODO: Given two functions, one bigger, one smaller, return the remiander. (from plugging in the solution of the smaller
# function ie. 2 from (x-2) into the bigger function)
def find_remainder(big_poly, small_poly):
    """Return the remainder of the division of two functions <big_poly> and <small_poly>

    Precondition: deg of <big_poly> > deg of <small_poly>
    """

    # Returns in format (quotient, remainder)
    return sympy.div(big_poly, small_poly)[1]

# TODO: Generate two functions where the bigger one has a constant K, and with the remainder for questions
# that ask what the coffeicent is given the constant and the two functions that divide

# NOTE: It would be better if we could actually show the steps to divide the function using long or synthetic divison
# TODO: synthetic(short) division. Given a polynomial and a bionomial function

# TODO: long division Given a polynomial and a bionomial function

# TODO: factor theorem stuff
"""Factoor theorem states that x-b is a factor of polynomial P(x) iff P(b) = 0 
and ax-b is a factor if P(b/a) = 0 """

"""What we could do is, already create some factors given a degree, than expand it and return the full equation"""

def is_factor(polynomial: Poly, factor: float) -> bool:
    """
    Return whether or not <factor> is a factor of the polynomial <polynomial>

    """
    if (polynomial.subs(x, factor) == 0):
        return True
    return False

# Series of functions that provide 'factorable' equations such that the person has to divide one or twice and end up
# with a easily factorable equation (like quadractic or simple linear) to completely factor it
# TODO: we may have to do a little bit of hardcoding in this one.


def generate_cubic(coefficient_range: typing.Tuple[int, int]):
    """
    Generates a factorable cubic function.
    First, it generates three linear functions.
    Then it will simplify the three functions by multiplying them.

    Preconditions:
    - coefficient_range != ()
    - coefficient_range[0] <= coefficient_range[1]
    """
    f = unit1.generate_polynomial(1, coefficient_range)
    g = unit1.generate_polynomial(1, coefficient_range)
    h = unit1.generate_polynomial(1, coefficient_range)

    return sympy.expand(f * g * h)


def generate_quartic(coefficient_range: typing.Tuple[int, int]):
    """
    Generates a factorable quartic function.
    First, it generates four linear functions.
    Then it will simplify the four functions by multiplying them.

    Preconditions:
    - coefficient_range != ()
    - coefficient_range[0] <= coefficient_range[1]
    """
    f = unit1.generate_polynomial(1, coefficient_range)
    g = unit1.generate_polynomial(1, coefficient_range)
    h = unit1.generate_polynomial(1, coefficient_range)
    k = unit1.generate_polynomial(1, coefficient_range)

    return sympy.expand(f * g * h * k)

# TODO: rational zero theorem
# TODO: given a polynomial fucntion. a is the leading coffeicnet. b is the constant.
# The possible factors of a function is any combination of facotrs of b/factors of a.

# TODO: find possible factors rational zero thereom given a function,
# return a factor ie. if -2 is a factor then return x + 2


def compare(polynomial, inequality, value) -> str:
    """
    Evaluates inequality by comparing between polynomial and value.

    Preconditions:
    - polynomial is a valid polynomial function from <generate_polynomial>
    - inequality in ['<', '>', '<=', '>=']
    - value is constant number
    """
    if inequality == '<':
        return sympy.printing.pretty(sympy.solveset(polynomial < value, x, sympy.S.Reals))
    elif inequality == '>':
        return sympy.printing.pretty(sympy.solveset(polynomial > value, x, sympy.S.Reals))
    elif inequality == '<=':
        return sympy.printing.pretty(sympy.solveset(polynomial <= value, x, sympy.S.Reals))
    else:
        return sympy.printing.pretty(sympy.solveset(polynomial >= value, x, sympy.S.Reals))
    

# TODO: provide the x-intercepts of a factorable polynomial. For questions for people
# to write the equation of the polynomial given a point or not


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)  # Forcing verbose to be true will provide full details of doctests
