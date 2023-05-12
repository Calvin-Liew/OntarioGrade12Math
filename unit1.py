"""Math Problem Generator - Unit 1: Polynomial Functions

Description
============================================
This module contains code for Unit 1 functions
"""

import random
import typing
import sympy
from sympy import degree, factorial, symbols, simplify, Eq
from sympy.abc import x

#from prettytable import PrettyTable

# from sympy import symbols, Function, Symbol
# from sympy.plotting import plot


def generate_polynomial(degree: int, coefficient_range: typing.Tuple[int, int]):
    """
    Generates polynomial function based on <degree> and <coefficient_range>.
    <degree> is used for the highest degree of the function and
    <coefficient_range> is used for the range of the coefficient in the function.

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
# Disciminant is defined differently for different degree functions
# So we might need to put a limit to degree
def generate_factorable_polynomial(degree: int, coefficient_range: typing.Tuple[int, int]):
    """
    Generates factorable polynomial where the degree is 2 to 4

    Preconditions:
    - 2 < degree <= 4
    - coefficient_range != ()
    """
    while True:
        possible_function = generate_polynomial(degree, coefficient_range)
        # print(find_discriminant(possible_function))
        if find_discriminant(possible_function) >= 0:
            return possible_function


def find_discriminant(polynomial):
    """
    Helper function for <generate_factorable_polynomial>.
    Calculates discriminants up to polynomial functions where the degree is less than or equal to 4.

    >>> find_discriminant(x**2 + 2*x + 1)
    0
    >>> find_discriminant(x**3 - 3*x + 2)
    0
    >>> find_discriminant(x**4 - 4*x**3 + 6*x**2 - 4*x + 1)
    0
    """
    expr = sympy.Poly(polynomial, x)
    coeff_list = expr.all_coeffs()
    if sympy.degree(polynomial) == 2:    # Degree 2
        discriminant = (coeff_list[1]) ** 2 - 4 * coeff_list[0] * coeff_list[2]
        return discriminant
    elif sympy.degree(polynomial) == 3:  # Degree 3
        discriminant = (coeff_list[1]) ** 2 * (coeff_list[2]) ** 2 - 4 * coeff_list[0] * (coeff_list[2]) ** 3 - 4 * (
        coeff_list[1]) ** 3 * coeff_list[3] - 27 * (coeff_list[0]) ** 2 * (coeff_list[3]) ** 2 + 18 * coeff_list[0] * \
                       coeff_list[1] * coeff_list[2] * coeff_list[3]
        return discriminant
    else:  # Degree 4
        discriminant = 256 * (coeff_list[0]) ** 3 * (coeff_list[4]) ** 3 - 192 * (coeff_list[0]) ** 2 * coeff_list[1] * \
                       coeff_list[3] * (coeff_list[4]) ** 2 - 128 * (coeff_list[0]) ** 2 * (coeff_list[2]) ** 2 * (
                       coeff_list[4]) ** 2 + 144 * (coeff_list[0]) ** 2 * coeff_list[2] * (coeff_list[3]) ** 2 * \
                       coeff_list[4] - 27 * (coeff_list[0]) ** 2 * (coeff_list[3]) ** 4 + 144 * coeff_list[0] * (
                       coeff_list[1]) ** 2 * coeff_list[2] * (coeff_list[4]) ** 2 - 6 * coeff_list[0] * (
                       coeff_list[1]) ** 2 * (coeff_list[3]) ** 2 * coeff_list[4] - 80 * coeff_list[0] * coeff_list[1] * (coeff_list[2]) ** 2 * coeff_list[3] * coeff_list[4] + \
                       18 * coeff_list[0] * coeff_list[1] * coeff_list[2] * (coeff_list[3]) ** 3 + 16 * coeff_list[0] * (coeff_list[2]) ** 4 * coeff_list[4] - \
                       4 * coeff_list[0] * (coeff_list[2]) ** 3 * (coeff_list[3]) ** 2 - 27 * (coeff_list[1]) ** 4 * (coeff_list[4]) ** 2 + \
                       18 * (coeff_list[1]) ** 3 * coeff_list[2] * coeff_list[3] * coeff_list[4] - 4 * (coeff_list[1]) ** 3 * (coeff_list[3]) ** 3 - \
                       4 * (coeff_list[1]) ** 2 * (coeff_list[2]) ** 3 * coeff_list[4] + (coeff_list[1]) ** 2 * (coeff_list[2]) ** 2 * (coeff_list[3]) ** 2
        return discriminant


def sympy_to_mathjax(polynomial) -> str:
    """
    Converts sympy polynomial function to mathjax syntax

    Preconditions:
    - polynomial is a valid polynomial function from <generate_polynomial>

    >>> sympy_to_mathjax(x**3 + 7*x**2 + 4*x + 3)
    'x^{3} + 7 x^{2} + 4 x + 3'
    """
    return sympy.latex(polynomial)


def end_behaviour(first_quadrant: str, second_quadrant: str, coefficient_range: typing.Tuple[int, int]):
    """
    Returns polynomial with degree from 1 to 6 inclusive based on end behaviour input

    Preconditions:
    - first_quadrant in ['Q1', 'Q2', 'Q3', 'Q4']
    - second_quadrant in ['Q1', 'Q2', 'Q3', 'Q4']
    - coefficient_range != ()
    """
    quadrant_list = ['Q1', 'Q2', 'Q3', 'Q4']
    if first_quadrant not in quadrant_list or second_quadrant not in quadrant_list:
        return 'Wrong Input'
    else:
        # Inefficient - Can change later
        if (first_quadrant == 'Q1' and second_quadrant == 'Q2') or (first_quadrant == 'Q2' and second_quadrant == 'Q1'):
            # Even function
            degree = random.randrange(2, 7, 2)  # Degree 2, 4, 6
            function = generate_polynomial(degree, coefficient_range)
            return function
        elif (first_quadrant == 'Q3' and second_quadrant == 'Q4') or (
                first_quadrant == 'Q3' and second_quadrant == 'Q4'):
            # Even function
            degree = random.randrange(2, 7, 2)  # Degree 2, 4, 6
            function = generate_polynomial(degree, coefficient_range)
            return function
        elif (first_quadrant == 'Q1' and second_quadrant == 'Q3') or (
                first_quadrant == 'Q3' and second_quadrant == 'Q1'):
            # Odd function
            degree = random.randrange(1, 6, 2)  # Degree 1, 3, 5
            function = generate_polynomial(degree, coefficient_range)
            return - + function
        else:
            # Odd function
            degree = random.randrange(1, 6, 2)  # Degree 1, 3, 5
            function = generate_polynomial(degree, coefficient_range)
            return - + function


def even_or_odd(f):
    """
    Determines whether the function is even or odd

    Preconditions:
    - f is a valid polynomial function from <generate_polynomial>

    >>> even_or_odd(x**2 + x**4 + x**6)
    'The function is even'
    >>> even_or_odd(x**3 - 8*x)
    'The function is odd'
    >>> even_or_odd(1 + x + x**2)
    'The function is neither even nor odd'
    """
    x = symbols('x')
    f_of_neg_x = f.subs(x, -x)
    evenness = simplify(f - f_of_neg_x)
    oddness = simplify(f + f_of_neg_x)
    if evenness.equals(0):
        return "The function is even"
    elif oddness.equals(0):
        return "The function is odd"
    else:
        return "The function is neither even nor odd"


def leading_coeff(polynomial) -> int:
    """
    Returns leading coefficient of polynomial

    Preconditions:
    - polynomial is a valid polynomial function from <generate_polynomial>

    >>> leading_coeff(x**3 + 7*x**2 + 4*x + 3)
    1
    """
    return sympy.LC(polynomial)


def function_domain(polynomial) -> str:
    """
    Returns domain of polynomial in str format

    Preconditions:
    - polynomial is a valid polynomial function from <generate_polynomial>

    >>> function_domain(x**2 + 1)
    'ℝ'
    >>> function_domain(1/x)
    '(-∞, 0) ∪ (0, ∞)'
    """
    domain = sympy.calculus.util.continuous_domain(polynomial, x, sympy.S.Reals)
    return sympy.printing.pretty(domain)


def function_range(polynomial) -> str:
    """
    Returns range of polynomial in str format

    Preconditions:
    - polynomial is a valid polynomial function from <generate_polynomial>

    >>> function_range(sympy.sqrt(x))
    '[0, ∞)'
    >>> function_range(x**2 + 1)
    '[1, ∞)'
    """
    Range = sympy.calculus.util.function_range(polynomial, x, sympy.S.Reals)
    return sympy.printing.pretty(Range)


# TODO: table of intervals of given equation
# def table_of_intervals(polynomial):
#     # factored = sympy.factor(polynomial)
#     myTable = PrettyTable([])
#
#     roots_list = sympy.real_roots(polynomial)


def turning_points(polynomial) -> int:
    """
    Returns the number of turning points of a polynomial

    Preconditions:
    - polynomial is a valid polynomial function from <generate_polynomial>
    """

    count = 0
    derivative = sympy.diff(polynomial, x)
    second_derivative = sympy.diff(derivative, x)
    critical_points = sympy.solveset(derivative, x)

    for point in critical_points:
        # NOTE: If the second derivative is 0 its not a turning point
        if (not point.has(sympy.I) and (second_derivative.subs(x, point) > 0
                                        or second_derivative.subs(x, point) < 0)):
            count += 1
    return count


def x_int(polynomial) -> sympy.Set:
    """
    Returns x-intercept of polynomial

    Preconditions:
    - polynomial is a valid polynomial function from <generate_polynomial>

    >>> x_int(x**2 - 1)
    {-1, 1}
    """
    return sympy.solveset(polynomial, x)


def y_int(polynomial) -> list[int | float]:
    """
    Returns y-intercept of polynomial

    Preconditions:
    - polynomial is a valid polynomial function from <generate_polynomial>

    >>> y_int(x**2 - 1)
    [-1]
    """
    return [polynomial.coeff(x, 0)]  # return just the y-intercept


def polynomial_degree(polynomial) -> list[int | float]:
    """
    Returns the degree of a polynomial.

    Preconditons:
    Polynomial is a valid polynomial from <generate_polynomial>

    >>> polynomial_degree(x**2+x+3)
    [2]
    """
    return [degree(polynomial)]


def points_of_polynomial(polynomial) -> list[set]:
    """
    Returns a list of points of a polynomial with x's from -7 to 7.

    Preconditions:
    Polynomial is a valid polynomial from <generate_polynomial>

    >>> points_of_polynomial(x**2+4)
    [(-7, 53.000), (-6, 40.000), (-5, 29.000), (-4, 20.000), (-3, 13.000), (-2, 8.0000), (-1, 5.0000), (0, 4.0000), (1, 5.0000),\
    (2, 8.0000), (3, 13.000), (4, 20.000), (5, 29.000), (6, 40.000), (7, 53.000)]

    """
    points = []
    for i in range(-7, 8):
        point = (i, polynomial.evalf(5, subs={x: i}))
        points.append(point)
    return points


def all_differences(degree, points):
    """
    Computes all the differences for a given polynomial of a given degree, evaluated at the given points.

    """
    n = len(points)
    result = [[y for x, y in points]]

    for level in range(1, n):
        row = []
        for i in range(n - level):
            diff = result[level - 1][i + 1] - result[level - 1][i]
            row.append(diff)
        result.append(row)

    differences = []
    for i in range(n - 1):
        differences.append(result[i])
        if len(result[i]) == n - degree:
            break

    return differences, result[i][-1]


def finite_difference(polynomial):
    """Return the finite difference given a polynomial

    >>> finite_difference(-2*x**4+8)
    -48
    """
    leading_coefficent = sympy.LC(polynomial)
    degree = polynomial_degree(polynomial)
    degree = degree[0]
    multiplier = factorial(degree)
    return multiplier * leading_coefficent


# TODO: Given equation, write word descriptions about the function ie. x-intercept at x=, y-intercept at blah,
#  domain, range, points

# def characteristic(polynomial) -> str:
#     """
#     Returns a basic description about the function in the format of:
#     x-int: -1, 1
#     y-int: -1
#     domain: 'ℝ'
#     """
#     x_intercept = x_int(polynomial)
#     y_intercept = y_int(polynomial)
#     domain = function_domain(polynomial)
#     range = function_range(polynomial)
#     points = turning_points(polynomial)
#
#     return_str = 'x-int: '
#     for x_point in x_intercept:
#         return_str += f'{x_point}, '
#     return_str = return_str[:-2]    # Take out last two elements
#     return_str = return_str + '\n y-int: '
#     # for y_point in y_intercept:
#
#     return return_str

# TODO: Given variables that transform a function, return the equation, a,k,c,d values
# This has the same problems with factorable polynomials where the creating the vertex form isn't always equally defined
# for functions of varying degrees
def transformation_of_function(parent, a: float, k: float, c: float, d: float) -> sympy.Function:
    """
    Return a function after transformation, given the type of function, and the
    constants of transformation:
    a: vertical stretch factor
    k: horizontal stretch factor
    c: vertical shift factor
    d: horizontal shift factor
    """

    new_func = parent.subs(x, k * x - d)  ## Horizontal shift and strech
    new_func = a * new_func  ## Vertical strech
    new_func = new_func + c  ## Vertical shift

    return new_func


# TODO: Given some variables of A, K, C, D return text explaining what each does


# TODO: return number of x-intercepts, turning points, least possible degree, any symmtery intervals
# where graph is positive or negative


def average_rate_of_change(polynomial, x1, x2) -> float:
    """
    Returns the average rate of change of a polynomial given two x-values

    >>> average_rate_of_change(2*x+19, 3, 7)
    2.00000000000000
    """
    point1 = (x1, polynomial.evalf(subs={x: x1}))
    point2 = (x2, polynomial.evalf(subs={x: x2}))
    return (point1[1] - point2[1]) / (point1[0] - point2[0])


def instant_rate_of_change(polynomial, x1) -> float:
    """
    Returns the instantaneous rate of change at a given x in a given polynomial.

    >>> instant_rate_of_change(x**2, 2)
    4.00000000000000
    """
    derivative = sympy.diff(polynomial, x)
    slope = derivative.evalf(subs={x: x1})
    return slope


# TODO: Insert Questions functions to do


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)  # Forcing verbose to be true will provide full details of doctests
