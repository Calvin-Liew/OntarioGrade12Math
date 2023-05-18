"""Math Problem Generator - Unit 3: Rational Functions

Description
============================================
This module contains code for Unit 3 functions
"""

import unit1
import typing
import sympy
from sympy.abc import x


# Generate rational functions

# TODO: Generate any rational function ie. functions with no asymptotes, functions with horzontal asymptote, etc
# def generate_rational(numerator: float, degree, coefficient_range: typing.Tuple[int, int]):
#     """
#     Generates rational function based on numberator, degree and coefficient_range
#
#     Preconditions:
#     - degree > 0
#     - coefficient_range != ()
#     - coefficient_range[0] <= coefficient_range[1]
#     """
#     denominator = unit1.generate_polynomial(degree, coefficient_range)
#     return numerator / denominator
# Probably need to make numerator a polynomial as well

# TODO: Generate quadractic rational functions

# TODO: Generate rational function with asymptotes so we just need to have the denominator be a factorable polynomial

# TODO: Generate rational function that has one as the numerator and the deonominator be a simple factorable polynomial for questions asking about what the asymptotes are

# TODO: Intervals where function is positive ornegative
def pos_neg_rational(rational) -> list:
    """
    Returns the intervals where the rational function is positive or negative.
    Will be returned in list format where index 0 is the positive interval
    and index 1 is the negative interval
    >>> pos_neg_rational(1/x)
    ['(0, ∞)', '(-∞, 0)']
    >>> pos_neg_rational(1/(x - 5) + 2)
    ['(-∞, 9/2) ∪ (5, ∞)', '(9/2, 5)']
    """

    return [compare_rational(rational, '>', 0),
            compare_rational(rational, '<', 0)]


# TODO: Intercepts of rational function ie. when the numerator = 0.


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


# TODO: graph of rational function


def inc_dec_rational(rational) -> list:
    """
    Returns the intervals where the rational function is increasing or decreasing.
    Will be returned in list format where index 0 is the increasing interval
    and index 1 is the decreasing interval
    >>> inc_dec_rational(1/x)
    ['∅', '(-∞, 0) ∪ (0, ∞)']
    >>> inc_dec_rational(x/(x**2 - 9))
    ['∅', '(-∞, -3) ∪ (-3, 3) ∪ (3, ∞)']
    >>> inc_dec_rational(-1/(x**2 - 4*x - 5))
    ['(2, 5) ∪ (5, ∞)', '(-∞, -1) ∪ (-1, 2)']
    """
    derivative = sympy.diff(rational, x)
    return [compare_rational(derivative, '>', 0),
            compare_rational(derivative, '<', 0)]


def vertical_asymptote(rational) -> sympy.Set:
    """
    Returns vertical asymptotes of rational

    >>> vertical_asymptote(1/(x-5))
    {5}
    >>> vertical_asymptote(3/(x**2 - 1))
    {-1, 1}
    """
    n, d = sympy.fraction(rational)
    return sympy.solveset(d, x, sympy.S.Reals)


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
    return sympy.solveset(rational, x, sympy.S.Reals)


def y_int(rational) -> int:
    """
    Returns y-intercept of rational

    Preconditions:

    >>> y_int((2*x + 1) / (x + 2))
    1/2
    """
    return rational.subs(x, 0)


def attribute(rational):
    """
    Returns a basic description about the polynomial function

    >>> attribute((2*x + 1) / (x + 2))
    x-int: -1/2
    y-int: 1/2
    VA: -2
    HA: 2
    """
    x_intercept = x_int(rational)
    y_intercept = y_int(rational)
    v_asymptotes = vertical_asymptote(rational)
    h_asympototes = horizontal_asymptote(rational)

    return_str = 'x-int: '
    for x_point in x_intercept:
        return_str += f'{x_point}, '
    return_str = return_str[:-2]  # Take out last two elements
    return_str = return_str + '\n'

    return_str += f'y-int: {y_intercept} \n'

    return_str += 'VA: '
    for va in v_asymptotes:
        return_str += f'{va}, '
    return_str = return_str[:-2]  # Take out last two elements
    return_str = return_str + '\n'

    return_str += f'HA: {h_asympototes}'

    print(return_str)


def linear_quotient(coefficient_range: typing.Tuple[int, int]):
    """
    Generate quotient of linear function

    Preconditions:
    - coefficient_range != ()
    - coefficient_range[0] <= coefficient_range[1]
    """
    return 1 / (unit1.generate_polynomial(1, coefficient_range))


# TODO: Generate spceial case function: A function with holes
# def hole_function(coefficient_range: typing.Tuple[int, int]):
#     """
#     Generate a function with holes
#
#     Preconditions:
#     - coefficient_range != ()
#     - coefficient_range[0] <= coefficient_range[1]
#     """
#     f = unit1.generate_polynomial(1, coefficient_range)
#     print(f)
#     g = unit1.generate_polynomial(1, coefficient_range)
#     print(g)
#     fg = sympy.simplify(f * g)
#     print(fg)
#     return fg / f


# TODO: Generate a rational fucnction with a oblique asymptote. CASE 1. A quadractic over a linear

# TODO: Generate a rational fucnction with a oblique asymptote. CASE 2. A higher order function over a higher ordeer fucntion
# Have to solve where the function intersects the HA to graph


def compare_rational(rational, inequality, value) -> str:
    """
    Evaluates inequality by comparing between rational and value.

    Preconditions:
    - inequality in ['<', '>', '<=', '>=']
    - isinstance(value, float) == True
    """
    if inequality == '<':
        return sympy.printing.pretty(sympy.solveset(rational < value, x, sympy.S.Reals))
    elif inequality == '>':
        return sympy.printing.pretty(sympy.solveset(rational > value, x, sympy.S.Reals))
    elif inequality == '<=':
        return sympy.printing.pretty(sympy.solveset(rational <= value, x, sympy.S.Reals))
    else:
        return sympy.printing.pretty(sympy.solveset(rational >= value, x, sympy.S.Reals))


def evaluate_rational(rational, value) -> sympy.Set:
    """
    Evaluates rational = value

    Preconditions:
    - isinstance(value, float) == True

    >>> evaluate_rational(1/x, 1/2)
    {2.0}
    """
    return sympy.solveset(rational - value, x, sympy.S.Reals)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)  # Forcing verbose to be true will provide full details of doctests
