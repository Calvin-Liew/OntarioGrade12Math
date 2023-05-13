"""Math Problem Generator - Unit 3: Rational Functions

Description
============================================
This module contains code for Unit 3 functions
"""

import unit1
import typing
import sympy
from sympy.abc import x

#Generate rational functions

#TODO: Generate any rational function ie. functions with no asymptotes, functions with horzontal asymptote, etc

#TODO: Generate quadractic rational functions

#TODO: Generate rational function with asymptotes so we just need to have the denominator be a factorable polynomial

#TODO: Generate rational function that has one as the numerator and the deonominator be a simple factorable polynomial for questions asking about what the asymptotes are

#TODO: Intervals where function is positive ornegative

#TODO: Intercepts of rational function ie. when the numerator = 0.


def rational_domain(rational) -> str:
    """
    Returns domain of rational in str format

    Preconditions:
    - rational is a valid rational function

    >>> rational_domain(1/(x - 1))
    '(-∞, 1) ∪ (1, ∞)'
    >>> rational_domain(1/x)
    '(-∞, 0) ∪ (0, ∞)'
    """
    domain = sympy.calculus.util.continuous_domain(rational, x, sympy.S.Reals)
    return sympy.printing.pretty(domain)


def rational_range(polynomial) -> str:
    """
    Returns range of rational in str format

    Preconditions:
    - rational is a valid rational function

    >>> rational_range(1/(x - 1))
    '(-∞, 0) ∪ (0, ∞)'
    >>> rational_range(1/x + 1)
    '(-∞, 1) ∪ (1, ∞)'
    """
    Range = sympy.calculus.util.function_range(polynomial, x, sympy.S.Reals)
    return sympy.printing.pretty(Range)

#TODO: graph of rational function

#TODO: Intervals where the function is increasing/decreasing ie. where the deriviative is above zero and below zero


def vertical_asymptote(rational) -> sympy.Set:
    """
    Returns vertical asymptotes of rational

    >>> vertical_asymptote(1/(x-5))
    {5}
    >>> vertical_asymptote(3/(x**2 - 1))
    {-1, 1}
    """
    n, d = sympy.fraction(rational)
    return sympy.solveset(d, x)


def horizontal_asymptote(rational) -> int:
    """
    Returns horizontal asymptote of rational

    >>> horizontal_asymptote((2*x + 1) / (x + 2))
    2
    """
    # right_limit = sympy.limit(rational, x, sympy.oo)
    # left_limit = sympy.limit(rational, x, -sympy.oo)
    return sympy.limit(rational, x, sympy.oo)


def x_int(rational) -> sympy.Set:
    """
    Returns x-intercept of rational

    Preconditions:

    >>> x_int(1/(x**2 + 2*x - 3))
    EmptySet
    >>> x_int((2*x + 1) / (x + 2))
    {-1/2}
    """
    return sympy.solveset(rational, x)


def y_int(rational) -> int:
    """
    Returns y-intercept of rational

    Preconditions:

    >>> y_int((2*x + 1) / (x + 2))
    1/2
    """
    return rational.subs(x, 0)

#TODO: important attributes of rational functions (for graphing questions), ie. x-int, y-int, HA, VA,

#TODO: Generate quotient of linear functions

#TODO: Generate spceial case function: A function with holes

#TODO: Generate a rational fucnction with a oblique asymptote. CASE 1. A quadractic over a linear

#TODO: Generate a rational fucnction with a oblique asymptote. CASE 2. A higher order function over a higher ordeer fucntion
# Have to solve where the function intersects the HA to graph

#TODO: Inequalities of rational functions

#TODO: Solving rational equations


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)  # Forcing verbose to be true will provide full details of doctests
