"""Math Problem Generator - Unit 6: Exponents/Log

Description
============================================
This module contains code for Unit 6 functions
"""

import sympy
import random
from sympy.abc import x
from sympy import log


# TODO: exponent stuff

# TODO: product law review stuffs

# def product_rule(exp_list: list[float]):
#     """
#     Generate simple product rule. <exp_list> is the list of the exponents.
#     """
#     return_so_far = 1
#     for exp in exp_list:
#         return_so_far *= x ** exp
#     return [return_so_far, sympy.simplify(return_so_far)]
#
#
# def quotient_rule(exp_list: list[float]):
#     """
#     Generate simple quotient rule. <exp_list> is the list of the exponents.
#     """
#     return_so_far = 1
#     for exp in exp_list:
#         return_so_far /= x ** exp
#     return [return_so_far, sympy.simplify(return_so_far)]


# def power_rule(exp_list: list[float]):
#     """
#     Generate simple power rule. <exp_list> is the list of the exponents.
#     Index 0 is the inner exponent while index 1 is the outer exponent.
#     """
#     return [(x ** exp_list[0]) ** exp_list[1], sympy.simplify((x ** exp_list[0]) ** exp_list[1])]


# TODO: review of inverse functions. Provide random points in domain and range. return the inverse domain and range.

# TODO: transformations of exponention functions

# TODO: explanation of transformations

# TODO: generating exponent equations. ex. 4^2x = 16^2x-1. Yeah have fun with this. You gotta think about how to make some nice equations that are easy to solve for x. Make sure they are same base.

# TODO: more complicated simplifying equatiosn using all three expoent rules.

# TODO: simplfying exponent numbers with no variables. ie. (1/2)**-1 = 2


# TODO: rewrite into log stuff. Generate a exponential equation like 5^2=25 and rewrite in log ie. Log5. Need both sides

# TODO: rewrite into expontential stuff. Ie. log(6)36 = 2, 6^2=36

# TODO: generate simple log equation. ie. log3(81) = x, solve for x need both sides. the base should be unique.

# TODO: transformations of log functions.

# TODO: explanation of transformations


def exp_domain(exp_function) -> str:
    """
    Returns domain of exponent function in str format

    >>> exp_domain(2**x)
    'ℝ'
    """
    domain = sympy.calculus.util.continuous_domain(exp_function, x, sympy.S.Reals)
    return sympy.printing.pretty(domain)


def exp_range(exp_function) -> str:
    """
    Returns range of exponent function in str format

    >>> exp_range(2**x)
    '∅'
    """
    Range = sympy.calculus.util.function_range(exp_function, x, sympy.S.Reals)
    return sympy.printing.pretty(Range)


def log_domain(exp_function) -> str:
    """
    Returns domain of exponent function in str format

    >>> log_domain(log(x, 2))
    '(0, ∞)'
    """
    domain = sympy.calculus.util.continuous_domain(exp_function, x, sympy.S.Reals)
    return sympy.printing.pretty(domain)


def log_range(exp_function) -> str:
    """
    Returns range of exponent function in str format

    >>> log_range(log(x, 2))
    '(-∞, ∞)'
    """
    Range = sympy.calculus.util.function_range(exp_function, x, sympy.S.Reals)
    return sympy.printing.pretty(Range)


# TODO: log laws: product law of logarithms, create simple equation to use product log ie. log11 + log4 = log44 etc. use different bases to make it more unique. need both sides

# TODO: log laws: quotient law, same thhing as above but with quotient rule ie. log5-log2 = log5/2

# TODO: log rule evaluation. create some equations like log2(4)+log2(8)=5. Need both sides

# TODO: power log rule. power log rule evaluation. create some equation like log3(9)^4 = 8. Need both sides.

# TODO: change of base rule. create some log equation and do change of base to it. Return both sides. Ie. log5(17) = log17/log5

# TODO: Generarate those write as a single log question. crate some sort of euqation with the same base with simple quadractic or linear or root equations turn it into one log.

# TODO: solving exponetial equations. create some expoential equation such as 100=50(1.03)^2x. try to make it more unique. need the question and the answer.

# TODO: same as above but with questions like 4^2x-1 = 3^x+2.

# TODO: same as above but with questiosn like 3^2x+3^x-12=0 or 5^x-20(5)^-x=1. provide question and answer.

# TODO: expo word problems. think about later

# TODO: solving log equations. remember to include the restrictiosn in the solution.
# generate some random log equations such as log5(2x-3) = 2 or log(x-1)-1=-log(x+2). Try to keep x-value answers integers for ease. Need both answer and solutions.

# TODO: appplciation questions with logs think about later.


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)  # Forcing verbose to be true will provide full details of doctests
