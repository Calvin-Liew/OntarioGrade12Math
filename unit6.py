"""Math Problem Generator - Unit 6: Exponents/Log

Description
============================================
This module contains code for Unit 6 functions
"""

import sympy
import random
import typing
from sympy.abc import x
from sympy import log


# TODO: exponent stuff

# TODO: product law review stuffs

def product_rule(exp_list: list[float]) -> list[str, sympy.Poly]:
    """
    Returns the expanded and simplified form of the product of a series of powers.
    The expanded form is a string in latex. <exp_list> is the list of the exponents.

    >>> product_rule([8, 2, 1])
    ['x^8*x^2*x', x**11]
    """
    simplified = 1
    full = ''
    for exp in exp_list:
        if full != '':
            full += '*'
        full += sympy.latex(x ** exp)
        simplified *= x ** exp
    return [full, simplified]


def quotient_rule(exp_list: list[float]) -> list[str, sympy.Poly]:
    """
    Returns the expanded and simplified form of the quotient of a series of powers.
    The expanded form is a string in latex. <exp_list> is the list of the exponents.
    
    >>> quotient_rule([10, 3, 1])
    ['x^10/x^3/x', x**6]
    """
    simplified = x ** exp_list[0]
    full = sympy.latex(x ** exp_list[0])
    for exp in exp_list[1:]:
        full += '/' + sympy.latex(x ** exp)
        simplified /= x ** exp
    return [full, simplified]



def power_rule(exp_list: list[float, float]) -> list[str, sympy.Poly]:
    """
    Returns the expanded and simplified form of the a power rule. The expanded
    form is a string in latex. <exp_list> is the list of the exponents, where
    index 0 is the inner exponent and index 1 is the outer exponent
    """
    full = f'(x^{{{exp_list[0]}}})^{{{exp_list[1]}}}'
    simplified = (x ** exp_list[0]) ** exp_list[1]
    return [full, simplified]


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


def log_product(log1: typing.Tuple[float], log2: typing.Tuple[float]) -> list:
    """
    Evaluates the log product law of logarithms (shows both sides). 
    log1[0] is the base for the first log and 
    log1[1] is the argument for the first log.
    log2[0] is the base for the second log and 
    log2[1] is the argument for the second log.

    Preconditions:
    - len(log1) == 2
    - len(log2) == 2
    """
    return [sympy.log(log1[0], log1[1]) + sympy.log(log2[0], log2[1]), sympy.logcombine(sympy.log(log1[0], log1[1]) + sympy.log(log2[0], log2[1]))]


def log_quotient(log1: typing.Tuple[float], log2: typing.Tuple[float]) -> list:
    """
    Evaluates the log quotient law of logarithms (shows both sides). 
    log1[0] is the base for the first log and 
    log1[1] is the argument for the first log.
    log2[0] is the base for the second log and 
    log2[1] is the argument for the second log.

    Preconditions:
    - len(log1) == 2
    - len(log2) == 2
    """
    return [sympy.log(log1[0], log1[1]) - sympy.log(log2[0], log2[1]), sympy.logcombine(sympy.log(log1[0], log1[1]) - sympy.log(log2[0], log2[1]))]


# TODO: log rule evaluation. create some equations like log2(4)+log2(8)=5. Need both sides


def log_power(log1: typing.Tuple[float], power: int) -> list:
    """
    Evaluates the log power law of logarithms (shows both sides). 
    log1[0] is the base for the first log and 
    log1[1] is the argument for the first log.

    Preconditions:
    - len(log1) == 2
    """
    return [power * sympy.log(log1[0], log1[1]), power * sympy.logcombine(sympy.log(log1[0], log1[1]))]


# TODO: change of base rule. create some log equation and do change of base to it. Return both sides. Ie. log5(17) = log17/log5

# TODO: Generarate those write as a single log question. crate some sort of euqation with the same base with simple quadractic or linear or root equations turn it into one log.

# TODO: solving exponetial equations. create some expoential equation such as 100=50(1.03)^2x. try to make it more unique. need the question and the answer.

# TODO: same as above but with questions like 4^2x-1 = 3^x+2.

# TODO: same as above but with questiosn like 3^2x+3^x-12=0 or 5^x-20(5)^-x=1. provide question and answer.

# TODO: expo word problems. think about later

# TODO: solving log equations. remember to include the restrictiosn in the solution.
# generate some random log equations such as log5(2x-3) = 2 or log(x-1)-1=-log(x+2). Try to keep x-value answers integers for ease. Need both answer and solutions.

# TODO: appplciation questions with logs think about later.


###############################################################################
# Question Functions
###############################################################################

if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)  # Forcing verbose to be true will provide full details of doctests
