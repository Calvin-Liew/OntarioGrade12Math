"""Math Problem Generator - Unit 7: 

Description
============================================
This module contains code for Unit 7 functions
"""

import sympy
import random
import typing
from sympy.abc import x
import unit1


def generate_combined_sum():
    """
    Generates two functions then returns the combined sum function.
    """
    random_degree1 = random.randint(1, 3)
    random_degree2 = random.randint(1, 3)
    coefficient_range = (-5, 5)
    f = unit1.generate_polynomial(random_degree1, coefficient_range)
    g = unit1.generate_polynomial(random_degree2, coefficient_range)
    h = f + g
    return [f, g, h]


def generate_combined_difference():
    """
    Generates two functions then returns the combined difference function.
    """
    random_degree1 = random.randint(1, 3)
    random_degree2 = random.randint(1, 3)
    coefficient_range = (-5, 5)
    f = unit1.generate_polynomial(random_degree1, coefficient_range)
    g = unit1.generate_polynomial(random_degree2, coefficient_range)
    h = f - g
    return [f, g, h]


def generate_combined_product():
    """
    Generates two functions then returns the combined product function.
    """
    random_degree1 = random.randint(1, 3)
    random_degree2 = random.randint(1, 3)
    coefficient_range = (-5, 5)
    f = unit1.generate_polynomial(random_degree1, coefficient_range)
    g = unit1.generate_polynomial(random_degree2, coefficient_range)
    h = f * g
    return [f, g, h]


def generate_combined_quotient():
    """
    Generates two functions then returns the combined quotient function.
    """
    random_degree1 = random.randint(1, 3)
    random_degree2 = random.randint(1, 3)
    coefficient_range = (-5, 5)
    f = unit1.generate_polynomial(random_degree1, coefficient_range)
    g = unit1.generate_polynomial(random_degree2, coefficient_range)
    h = f / g
    return [f, g, h]


def combined_domain(combined) -> str:
    """
    Returns domain of <combined> in str format

    """
    domain = sympy.calculus.util.continuous_domain(combined, x, sympy.S.Reals)
    return sympy.printing.pretty(domain)


def combined_range(combined) -> str:
    """
    Returns range of <combined> in str format

    """
    Range = sympy.calculus.util.function_range(combined, x, sympy.S.Reals)
    return sympy.printing.pretty(Range)


# TODO: combined function applicatiosn think about later


def generate_composite(degree1, coefficient_range1, degree2, coefficient_range2) -> list:
    """
    Generates composite function f(g(x))
    """
    f = unit1.generate_polynomial(degree1, coefficient_range1)
    g = unit1.generate_polynomial(degree2, coefficient_range2)
    composite = sympy.compose(f, g)
    return [f, g, composite]


def composite_domain(composite) -> str:
    """
    Returns domain of composite function in str format
    """
    domain = sympy.calculus.util.continuous_domain(composite, x, sympy.S.Reals)
    return sympy.printing.pretty(domain)


def composite_range(composite) -> str:
    """
    Returns range of composite function in str format
    """
    Range = sympy.calculus.util.function_range(composite, x, sympy.S.Reals)
    return sympy.printing.pretty(Range)

# TODO: coomposite abolsute value # Unit 7 Day 5 Q4

# TODO: composite word prolbems


def function_compare(polynomial1, inequality, polynomial2) -> str:
    """
    Evaluates function inequalities. ie f(x) > g(x)

    Preconditions:
    - inequality in ['<', '>', '<=', '>=']
    """
    if inequality == '<':
        return sympy.printing.pretty(sympy.solveset(polynomial1 < polynomial2, x, sympy.S.Reals))
    elif inequality == '>':
        return sympy.printing.pretty(sympy.solveset(polynomial1 > polynomial2, x, sympy.S.Reals))
    elif inequality == '<=':
        return sympy.printing.pretty(sympy.solveset(polynomial1 <= polynomial2, x, sympy.S.Reals))
    else:
        return sympy.printing.pretty(sympy.solveset(polynomial1 >= polynomial2, x, sympy.S.Reals))


###############################################################################
# Question Functions
###############################################################################

# TODO: solving function inequalities word problems. ie f(x) > g(x). 

if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)  # Forcing verbose to be true will provide full details of doctests
