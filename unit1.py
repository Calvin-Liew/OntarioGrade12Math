"""Math Problem Generator - Unit 1: Polynomial Functions

Description
============================================
This module contains code for Unit 1 functions
"""

import random
import typing
import sympy
from sympy import degree, factorial
from sympy.abc import x

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

# TODO: generate image of graph given equation, into image file. (should keep track of both image and the equation)


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


# TODO: least possible degree of given function ie. degree of polynomial function
# For questions that will give a image of a graph, student will have to see what the 
# least possible degree is. 

def polynomial_degree(polynomial) -> list[int | float]:
    """
    Returns the degree of a polynomial. 
    
    Preconditons: 
    Polynomial is a valid polynomial from <generate_polynomial>
    
    >>> polynomial_degree(x**2+x+3)
    [2]
    """
    return [degree(polynomial)]

# Finite differences stuff

# TODO: Given a equation, generate x and y values for a simple range ie
# First 5 differences 
def points_of_polynomial(polynomial) -> list[set]:
    """ 
    Returns a list of points of a polynomial with x's from -7 to 7.
    
    Preconditions:
    Polynomial is a valid polynomial from <generate_polynomial>
    
    >>> points_of_polynomial(x**2+4)
    [(-7, 53.000), (-6, 40.000), (-5, 29.000), (-4, 20.000), (-3, 13.000), (-2, 8.0000), (-1, 5.0000), (0, 4.0000), (1, 5.0000), (2, 8.0000), (3, 13.000), (4, 20.000), (5, 29.000), (6, 40.000), (7, 53.000)]
    
    """
    points = []
    for i in range(-7, 8):
        point = (i, polynomial.evalf(5, subs={x:i}))
        points.append(point)
    return points
        

# TODO: Given a list of y's, find differences until its constant N. N is the degree of the polynomial.

def all_differences(degree, points):
    """
    Computes all the differences for a given polynomial of a given degree, evaluated at the given points.
    """
    n = len(points)
    result = [[y for x, y in points]]

    for level in range(1, n):
        row = []
        for i in range(n - level):
            j = i + level
            diff = result[level - 1][i + 1] - result[level - 1][i]
            row.append(diff)
        result.append(row)

    differences = []
    for i in range(n - 1):
        differences.append(result[i])
        if len(result[i]) == n-degree:
            break

    return differences, result[i][-1]

# TODO: Given equation find which finite difference is constant (ie. the degree of leading coffcient), find the value
# The value is the leading coffeicnet, A multiplied by the degree N factorial. N! x A

def finite_difference(polynomial):
    """Return the finite difference given a polynomial
    
    >>> finite_difference(-2*x**4+8)
    -48
    """
    leading_coefficent = sympy.LC(polynomial)
    degree = polynomial_degree(polynomial)
    degree = degree[0]
    multiplier = factorial(degree)
    return multiplier*leading_coefficent
    
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

# TODO: Given some variables of A, K, C, D return text explaining what each does


# TODO: return number of x-intercepts, turning points, least possible degree, any symmtery intervals
# where graph is positive or negative

# TODO: Average rate of change, given a function and two points, find the AROC

# TODO: Instantaneous rate of change, given a fucntion and one point find the IROC

# TODO: Insert Questions functions to do


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)   # Forcing verbose to be true will provide full details of doctests
