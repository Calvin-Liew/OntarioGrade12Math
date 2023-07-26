"""Math Problem Generator - Unit 1: Polynomial Functions

Description
============================================
This module contains code for Unit 1 functions
"""

import random
import typing
import sympy
from math import isqrt
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from sympy import degree, factorial, symbols, simplify, Eq, expand, Add, Mul,  Rational, sqrt, solve, sympify, Poly, Symbol, factor, diff
from sympy.abc import x
from sympy.printing.latex import latex
from fractions import Fraction

# from prettytable import PrettyTable

# from sympy import symbols, Function, Symbol
# from sympy.plotting import plot


engine = create_engine("sqlite:///questions.db", echo=True)
Base = declarative_base()


class Question(Base):
    __tablename__ = "Questions"
    id = Column(Integer, primary_key=True)
    unit = Column(Integer)
    chapter = Column(Integer)
    topic = Column(String)
    question = Column(String)
    answer = Column(String)
    graph_qustion = Column(String)
    graph_answer = Column(String)

    def __repr__(self):
        return "<Questions(question='%s', answer='%s')>" % (
            self.question,
            self.answer)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()


# test = Question(unit=0, chapter=0, topic='test topic', question='test answer', answer='test answer', graph='test graph')
# session.add(test)
# session.commit()


def generate_polynomial(degree: int, coefficient_range: typing.Tuple[int, int]):
    """
    Generates polynomial function based on <degree> and <coefficient_range>.
    <degree> is used for the highest degree of the function and
    <coefficient_range> is used for the range of the coefficient in the function.

    Preconditions:
    - degree > 0
    - coefficient_range != ()
    - coefficient_range[0] <= coefficient_range[1]
    """
    x_exponent = degree
    expr = random.randint(coefficient_range[0], coefficient_range[1]) * x ** degree
    for i in range(0, x_exponent):
        expr += random.randint(coefficient_range[0], coefficient_range[1]) * x ** i
        x_exponent -= 1
    return expr


# TODO: Put a failsafe in case there is no possible factorable function (if it loops 100 times then return false)
def generate_factorable_polynomial(degree: int, coefficient_range: typing.Tuple[int, int]):
    """
    Generates factorable polynomial where the degree is 2 to 4

    Preconditions:
    - 2 <= degree <= 4
    - coefficient_range != ()
    - coefficient_range[0] <= coefficient_range[1]
    """
    while True:
        possible_function = generate_polynomial(degree, coefficient_range)
        # print(find_discriminant(possible_function))
        if find_discriminant(possible_function) >= 0:
            return possible_function


def find_discriminant(polynomial) -> int:
    """
    Helper function for <generate_factorable_polynomial>.
    Calculates discriminants up to polynomial functions where the degree is less than or equal to 4.

    Preconditions:
    - polynomial is a valid polynomial function from <generate_polynomial>

    >>> find_discriminant(x**2 + 2*x + 1)
    0
    >>> find_discriminant(x**3 - 3*x + 2)
    0
    >>> find_discriminant(x**4 - 4*x**3 + 6*x**2 - 4*x + 1)
    0
    """
    expr = sympy.Poly(polynomial, x)
    coeff_list = expr.all_coeffs()
    if sympy.degree(polynomial) == 2:  # Degree 2
        discriminant = (coeff_list[1]) ** 2 - 4 * coeff_list[0] * coeff_list[2]
        return discriminant
    elif sympy.degree(polynomial) == 3:  # Degree 3
        discriminant = (coeff_list[1]) ** 2 * (coeff_list[2]) ** 2 - 4 * coeff_list[0] * (coeff_list[2]) ** 3 - 4 * (
            coeff_list[1]) ** 3 * coeff_list[3] - 27 * (coeff_list[0]) ** 2 * (coeff_list[3]) ** 2 + 18 * coeff_list[
                           0] * \
                       coeff_list[1] * coeff_list[2] * coeff_list[3]
        return discriminant
    else:  # Degree 4
        discriminant = 256 * (coeff_list[0]) ** 3 * (coeff_list[4]) ** 3 - 192 * (coeff_list[0]) ** 2 * coeff_list[1] * \
                       coeff_list[3] * (coeff_list[4]) ** 2 - 128 * (coeff_list[0]) ** 2 * (coeff_list[2]) ** 2 * (
                           coeff_list[4]) ** 2 + 144 * (coeff_list[0]) ** 2 * coeff_list[2] * (coeff_list[3]) ** 2 * \
                       coeff_list[4] - 27 * (coeff_list[0]) ** 2 * (coeff_list[3]) ** 4 + 144 * coeff_list[0] * (
                           coeff_list[1]) ** 2 * coeff_list[2] * (coeff_list[4]) ** 2 - 6 * coeff_list[0] * (
                           coeff_list[1]) ** 2 * (coeff_list[3]) ** 2 * coeff_list[4] - 80 * coeff_list[0] * coeff_list[
                           1] * (coeff_list[2]) ** 2 * coeff_list[3] * coeff_list[4] + \
                       18 * coeff_list[0] * coeff_list[1] * coeff_list[2] * (coeff_list[3]) ** 3 + 16 * coeff_list[
                           0] * (coeff_list[2]) ** 4 * coeff_list[4] - \
                       4 * coeff_list[0] * (coeff_list[2]) ** 3 * (coeff_list[3]) ** 2 - 27 * (coeff_list[1]) ** 4 * (
                           coeff_list[4]) ** 2 + \
                       18 * (coeff_list[1]) ** 3 * coeff_list[2] * coeff_list[3] * coeff_list[4] - 4 * (
                           coeff_list[1]) ** 3 * (coeff_list[3]) ** 3 - \
                       4 * (coeff_list[1]) ** 2 * (coeff_list[2]) ** 3 * coeff_list[4] + (coeff_list[1]) ** 2 * (
                           coeff_list[2]) ** 2 * (coeff_list[3]) ** 2
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
    - coefficient_range[0] <= coefficient_range[1]
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


def even_or_odd(f) -> str:
    """
    Determines whether the function is even or odd

    Preconditions:
    - f is a valid polynomial function from <generate_polynomial>

    >>> even_or_odd(x**2 + x**4 + x**6)
    'The function is even: $f(x) = x^{2} + x^{4} + x^{6}$, because $f(-x) = f(x)$ algebraically simplifies to $x^{2} + x^{4} + x^{6} = x^{2} + x^{4} + x^{6}$'
    >>> even_or_odd(x**3 - 8*x)
    'The function is odd: $f(x) = x^{3} - 8x$, because $f(-x) = -f(x)$ algebraically simplifies to $-x^{3} + 8x = -(x^{3} - 8x)$'
    >>> even_or_odd(1 + x + x**2)
    'The function is neither even nor odd: $f(x) = 1 + x + x^{2}$, because $f(-x) = -f(x)$ algebraically simplifies to $-(1 + x + x^{2}) \\neq 1 + x + x^{2}$'
    """
    x = symbols('x')
    f_of_neg_x = f.subs(x, -x)
    evenness = simplify(f - f_of_neg_x)
    oddness = simplify(f + f_of_neg_x)
    if evenness.equals(0):
        return "The function is even: $f(x) = " + latex(
            f) + "$, because $f(-x) = f(x)$ algebraically simplifies to $" + latex(expand(f_of_neg_x)) + " = " + latex(
            expand(f)) + "$"
    elif oddness.equals(0):
        return "The function is odd: $f(x) = " + latex(
            f) + "$, because $f(-x) = -f(x)$ algebraically simplifies to $" + latex(
            expand(f_of_neg_x)) + " = -(" + latex(expand(f)) + ")$"
    else:
        return "The function is neither even nor odd: $f(x) = " + latex(
            f) + "$, because $f(-x) = -f(x)$ algebraically simplifies to $" + latex(
            expand(f_of_neg_x)) + " \\neq " + latex(expand(f)) + "$"


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

    >>> turning_points(x**3)
    0
    >>> turning_points(x**2)
    1
    """

    count = 0
    derivative = sympy.diff(polynomial, x)
    second_derivative = sympy.diff(derivative, x)
    critical_points = sympy.solveset(derivative, x, sympy.S.Reals)

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
    return sympy.solveset(polynomial, x, sympy.S.Reals)


def y_int(polynomial) -> int:
    """
    Returns y-intercept of polynomial

    Preconditions:
    - polynomial is a valid polynomial function from <generate_polynomial>

    >>> y_int(x**2 - 1)
    -1
    """
    return polynomial.subs(x, 0)


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

def count_turning_points(polynomial):
    x = symbols('x')
    derivative = diff(polynomial, x)
    critical_points = solve(derivative, x)
    turning_points = len(critical_points)
    return turning_points

def characteristic(polynomial):
    """
    Returns a basic description about the polynomial function

    >>> characteristic(x**2-1)
    x-int: -1, 1
    y-int: -1
    Turning Points: 1
    """
    x_intercept = x_int(polynomial)
    y_intercept = y_int(polynomial)
    points = count_turning_points(polynomial)

    return_str = 'X-int: '
    for x_point in x_intercept:
        return_str += f'{x_point}, '
    return_str = return_str[:-2]  # Take out last two elements
    return_str = return_str + '\n'

    return_str += f'y-int: {y_intercept} \n'
    return_str += f'Turning Points: {points}'

    return return_str# \n does not work for return


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

    >>> transformation_of_function(x, 0, 0, 0, 0)
    0
    >>> transformation_of_function(x**(1/2), 1, 1, 1, 1)
    x**(1/2)
    >>> transformation_of_function(x, -1, -1, -1 , -1)
    x+2
    >>> transformation_of_function(x**3, 0.5, 0.25, 0.3, 0.7)
    0.5*(4*(x-0.7))**3 + 0.3
    """

    a = float_to_fraction(a)
    k = float_to_fraction(k)
    d = float_to_fraction(d)
    c = float_to_fraction(c)
    new_func = parent.subs(x, k * (x - d))  # Horizontal shift and strech
    new_func = new_func + c  # Vertical shift
    new_func = a * new_func  # Vertical strech

    return new_func


# TODO: Given some variables of A, K, C, D return text explaining what each does

def transformation_explanation(a: float, k: float, c: float, d: float) -> list:
    """
    Return simple word descriptions of each transformation

    >>> transformation_explanation(-3, 2, 5, -1)
    ['Vertically stretched by a factor of 3', 'Reflection in x-axis', 'Vertical translation 5 units upwards', 'Horizontally compressed by a factor of 1/2', 'Horziontal translation 1 units to the left']
    """
    desc = []
    if abs(a) > 1:
        desc.append(f"Vertically stretched by a factor of {float_to_fraction(abs(a))}")
    elif 0 < abs(a) < 1:
        desc.append(f"Vertically compressed by a factor of {float_to_fraction(abs(a))}")
    if a < 0:
        desc.append(f"Reflection in x-axis")
    if c > 0:
        desc.append(f"Vertical translation {float_to_fraction(abs(c))} units upwards")
    elif c < 0:
        desc.append(f"Vertical translation of {float_to_fraction(abs(c))} units downwards")
    if abs(k) > 1:
        desc.append(f"Horizontally compressed by a factor of 1/{float_to_fraction(abs(k))}")
    elif 0 < abs(k) < 1:
        desc.append(f"Horizontally stretched by a factor of 1/{float_to_fraction(abs(k))}")
    if k < 0:
        desc.append(f"Reflection in y-axis")
    if d > 0:
        desc.append(f"Horizontal translation {float_to_fraction(abs(d))} units to the right")
    elif d < 0:
        desc.append(f"Horziontal translation {float_to_fraction(abs(d))} units to the left")
    return desc 


# TODO: return number of x-intercepts, turning points, least possible degree, any symmtery intervals
# where graph is positive or negative
def least_possible_degree(polynomial) -> int:
    """
    Given a polynomial function <polynomial>, return the least possible
    degree of the function if one were to just see the graph. (ie: turning points)

    >>> least_possible_degree(x**8)
    2
    """
    return turning_points(polynomial) + 1


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


def translate_end_behavior(quadrant1, quadrant2):
    # Define the translation mappings
    quadrant_map = {
        'Q1': "as x approaches positive infinity, y approaches positive infinity",
        'Q2': "as x approaches negative infinity, y approaches positive infinity",
        'Q3': "as x approaches negative infinity, y approaches negative infinity",
        'Q4': "as x approaches positive infinity, y approaches negative infinity"
    }

    # Translate the end behavior of each quadrant
    translation1 = quadrant_map.get(quadrant1, "Invalid quadrant")
    translation2 = quadrant_map.get(quadrant2, "Invalid quadrant")

    # Return the combined translation
    return f"For {quadrant1} -> {quadrant2}: {translation1} and {translation2}"

def interval_notation_single(num, symbol, side):
    if side == "left":
        if symbol == "<":
            interval = "(-∞, " + str(num) + ")"
        elif symbol == "<=":
            interval = "(-∞, " + str(num) + "]"
        elif symbol == ">":
            interval = "(" + str(num) + ", +∞)"
        elif symbol == ">=":
            interval = "[" + str(num) + ", +∞)"
    elif side == "right":
        if symbol == "<":
            interval = "(" + str(num) + ", +∞)"
        elif symbol == "<=":
            interval = "[" + str(num) + ", +∞)"
        elif symbol == ">":
            interval = "(-∞, " + str(num) + ")"
        elif symbol == ">=":
            interval = "(-∞, " + str(num) + "]"
    return interval

def interval_notation_between(num1, symbol1, num2, symbol2):
    if symbol1 == "<":
        left_interval = "(" + str(num1) + ", "
    elif symbol1 == "<=":
        left_interval = "[" + str(num1) + ", "
    elif symbol1 == ">":
        left_interval = "(" + str(num1) + ", "
    elif symbol1 == ">=":
        left_interval = "[" + str(num1) + ", "

    if symbol2 == "<":
        right_interval = str(num2) + ")"
    elif symbol2 == "<=":
        right_interval = str(num2) + "]"
    elif symbol2 == ">":
        right_interval = str(num2) + ")"
    elif symbol2 == ">=":
        right_interval = str(num2) + "]"

    interval = left_interval + right_interval
    return interval

def generate_equation_fail_vertical_line_test():
    y = symbols('y')
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)
    d = random.randint(-10, 10)
    e = random.randint(-10, 10)
    f = random.randint(-10, 10)
    expression = Add(
        Mul(a, y**2),
        Mul(b, y),
        c,
        Mul(d, y**3),
        Mul(e, y**2),
        Mul(f, y)
    )
    return expression

def generate_failed_vlt_points(num_points, same_x_points):
    points = set()

    # Generate points with unique x and y values
    for _ in range(num_points - same_x_points):
        x = random.randint(-100, 100)  # Adjust the range as needed
        y = random.randint(-100, 100)  # Adjust the range as needed
        points.add((x, y))

    # Generate points with the same x but different y values
    unique_x_values = len(points)
    if same_x_points > unique_x_values:
        same_x_points = unique_x_values

    unique_x_values = list({point[0] for point in points})
    random.shuffle(unique_x_values)
    for x in unique_x_values[:same_x_points]:
        y1 = random.randint(-100, 100)  # Adjust the range as needed
        y2 = random.randint(-100, 100)  # Adjust the range as needed
        while y2 == y1:
            y2 = random.randint(-100, 100)  # Adjust the range as needed
        points.add((x, y1))
        points.add((x, y2))

    return points


def generate_points(num_points):
    points = set()

    for _ in range(num_points):
        x = random.randint(0, 100)  # Adjust the range as needed

        while x in {point[0] for point in points}:
            x = random.randint(0, 100)  # Adjust the range as needed

        y = random.randint(0, 100)  # Adjust the range as needed

        points.add((x, y))

    return points

def generate_factorable_quadratic(leading_coefficient=1):
    x = symbols('x')

    # Randomly select the method to generate the quadratic equation
    method = random.choice(['gcf', 'difference_of_squares', 'decomposition'])

    if method == 'gcf':
        # Generate quadratic using GCF method
        a = random.randint(1, 10)
        b = random.randint(2, 10) * a
        c = random.randint(2, 10) * a

        if leading_coefficient > 1:
            a *= leading_coefficient
            b *= leading_coefficient
            c *= leading_coefficient

        equation = a * x**2 + b * x + c

    elif method == 'difference_of_squares':
        # Generate quadratic using Difference of Squares method
        a = random.randint(1, 10)
        b = 2 * random.randint(1, 5) * a

        if leading_coefficient > 1:
            a *= leading_coefficient
            b *= leading_coefficient

        equation = a * x**2 - b**2

    else:
        # Generate quadratic using decomposition method
        a = random.randint(1, 10)
        b = random.randint(2, 10) * a
        c = random.randint(2, 10) * a

        if leading_coefficient > 1:
            a *= leading_coefficient
            b *= leading_coefficient
            c *= leading_coefficient

        equation = a * x**2 + b * x + c

    return expand(equation)


def factor_quadratic_equation(equation):
    factored_equation = sympy.factor(equation)
    
    return factored_equation

def is_perfect_square(value):
    root = 1
    while root * root <= value:
        if root * root == value:
            return True
        root += 1
    return False

def quadractic_equation():    
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)

    discriminant = b**2 - 4*a*(c-d)

    while discriminant != 0 and not is_perfect_square(discriminant):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        c = random.randint(1, 10)
        d = random.randint(1, 10)
        discriminant = b**2 - 4*a*(c-d)

    x = symbols('x')
    equation = Eq(a * x**2 + b * x + c, d)
    solutions = solve(equation, x)
    return equation, solutions

def find_vertex(expr):
    x = Symbol('x')
    # Convert expression to standard form: ax^2 + bx + c
    standard_form = simplify(expr)
    a = standard_form.coeff(x, 2)
    b = standard_form.coeff(x, 1)
    c = standard_form.coeff(x, 0)

    # Calculate the x-coordinate of the vertex: x = -b / (2a)
    vertex_x = -b / (2 * a)
    # Calculate the y-coordinate of the vertex: y = f(x)
    vertex_y = expr.subs(x, vertex_x)

    # Convert to vertex form: a(x - h)^2 + k
    vertex_form = simplify(a * (x - vertex_x) ** 2 + vertex_y)

    return vertex_form, (vertex_x, vertex_y)

def points_to_string(points):
    """
    Converts a list of points into a string representation.
    Returns a string of points in the format "(x, y), (x, y), ...".
    """
    point_strings = [f"({point[0]}, {point[1]})" for point in points]
    points_string = ", ".join(point_strings)
    return points_string

def factor_polynomial(polynomial):
    x = symbols('x')
    factored_polynomial = factor(polynomial, x)
    return factored_polynomial

def float_to_fraction(number):
    fraction = Rational(number).limit_denominator()
    return fraction


def generate_random_polynomial_char():
    degree = random.randint(3, 6)
    num_roots = 0
    root_desc = []
    equation = 1  # Initialize the equation as a symbolic expression
    negative_coeffcient = False

    # Quadrants stuff
    if degree % 2 == 0:
        first_quadrant = random.randint(2, 3)
        if first_quadrant == 2:
            second_quadrant = 1
        else:
            second_quadrant = 4
            negative_coeffcient = True
    else:
        first_quadrant = random.randint(2, 3)
        if first_quadrant == 2:
            second_quadrant = 4
            negative_coeffcient = True
        else:
            second_quadrant = 1

    while num_roots < degree:
        x = random.randint(1, 3)
        if x == 1 and num_roots + 1 <= degree:
            root = random.randint(-10, 10)
            root_desc.append(f"Root at x = {root}")
            equation *= (sympy.Symbol('x') - root)  # Multiply the expression with (x - root)
            num_roots += 1
        elif x == 2 and num_roots + 2 <= degree:
            root = random.randint(-10, 10)
            root_desc.append(f"Double root at x = {root}")
            equation *= (sympy.Symbol('x') - root)**2  # Multiply the expression with (x - root)**2
            num_roots += 2
        elif x == 3 and num_roots + 3 <= degree:
            root = random.randint(-10, 10)
            root_desc.append(f"Inflection point at x = {root}")
            equation *= (sympy.Symbol('x') - root)**3  # Multiply the expression with (x - root)**3

            num_roots += 3

    # Multiply the equation by the variable a at the beginning
    a = sympy.Symbol('a')
    pure = equation
    equation *= a

    # Convert the symbolic expression to a polynomial equation string
    equation_str = sympy.latex(equation)
    if negative_coeffcient:
        coefficient = "where a < 0"
    else:
        coefficient = "where a > 0"
    # where a > 0
    return pure, equation, equation_str, coefficient, root_desc, first_quadrant, second_quadrant, degree
    
def analyze_expression(expr):
    # Find x-intercepts
    x_intercepts = sympy.solve(expr, sympy.Symbol('x'))

    # Find y-intercepts
    y_intercept = expr.subs('x', 0)

    # Find the degree of the expression
    degree = sympy.degree(expr)

    # Find the sign of the leading coefficient
    leading_coefficient = sympy.LC(expr)

    # Find intervals where the graph is positive/negative
    intervals_positive = sympy.solveset(sympy.StrictGreaterThan(expr, 0), sympy.Symbol('x'), domain=sympy.S.Reals)
    intervals_negative = sympy.solveset(sympy.StrictLessThan(expr, 0), sympy.Symbol('x'), domain=sympy.S.Reals)

    # Convert results to LaTeX format
    x_intercepts_latex = ', '.join(sympy.latex(x) for x in x_intercepts)
    y_intercept_latex = sympy.latex(y_intercept)
    degree_latex = sympy.latex(degree)
    leading_coefficient_latex = sympy.latex(leading_coefficient)
    intervals_positive_latex = sympy.latex(intervals_positive)
    intervals_negative_latex = sympy.latex(intervals_negative)

    # Return the results
    return [
        f"x_intercepts: {x_intercepts_latex}",
        f"y_intercept: {y_intercept_latex}",
        f"degree: {degree_latex}",
        f"leading coefficient: {leading_coefficient_latex}",
        f"intervals positive: {intervals_positive_latex}",
        f"intervals negative: {intervals_negative_latex}"
    ]

def analyze_expression2(expr):
    # Find x-intercepts
    x_intercepts = sympy.solve(expr, sympy.Symbol('x'))

    # Find y-intercepts
    y_intercept = expr.subs('x', 0)

    # Find the degree of the expression
    degree = sympy.degree(expr)

    # Find the sign of the leading coefficient
    leading_coefficient = sympy.LC(expr)

    # Find intervals where the graph is positive/negative
    intervals_positive = sympy.solveset(sympy.StrictGreaterThan(expr, 0), sympy.Symbol('x'), domain=sympy.S.Reals)
    intervals_negative = sympy.solveset(sympy.StrictLessThan(expr, 0), sympy.Symbol('x'), domain=sympy.S.Reals)

    # Convert results to LaTeX format
    x_intercepts_latex = ', '.join(sympy.latex(x) for x in x_intercepts)
    y_intercept_latex = sympy.latex(y_intercept)
    degree_latex = sympy.latex(degree)
    leading_coefficient_latex = 'Positive' if leading_coefficient > 0 else 'Negative'
    intervals_positive_latex = sympy.latex(intervals_positive)
    intervals_negative_latex = sympy.latex(intervals_negative)

    # Return the results
    return [
        f"x_intercepts: {x_intercepts_latex}",
        f"y_intercept: {y_intercept_latex}",
        f"degree: {degree_latex}",
        f"leading_coefficient sign: {leading_coefficient_latex}",
        f"intervals positive: {intervals_positive_latex}",
        f"intervals negative: {intervals_negative_latex}"
    ]

def solve_leading_coefficient(factored_equation, y_intercept):
    x = sympy.symbols('x')
    leading_coefficient = sympy.symbols('a')

    # Substitute y-intercept into the factored equation
    equation = factored_equation.subs(x, 0) - y_intercept

    # Solve for the leading coefficient
    solutions = sympy.solve(equation, leading_coefficient)

    return solutions


###############################################################################
# Question Functions
###############################################################################

# TODO: Insert Questions functions to do
# NOTE: Our current schema is in the form of (id, unit, chapter, topic, answer, graph_equation)
# NOTE: Confirm that we can put equations and points into desmo api


# TODO: Chapter 0
#Maybe add some more 'chapter 0' questions and answers such as
#expanding, factoring, exponenet power rules, simplifying, solving 
#simple quadractic and linear equations, exponent practice, lines

# image of a graph that may or may not be function
def function_or_not():
    x = random.randint(0, 1)
    if x == 0:
        degree = random.randint(2, 4)
        coeffcient_range = (-10, 10)
        polynomial = generate_polynomial(degree, coeffcient_range)
        graph = latex(polynomial)
        question=f"""Is this a function: """
        answer=f"""Yes this passes the vertical line test."""
        question = Question(unit=1, chapter=1.1, topic="what is a function", question=question, answer=answer, graph=graph)
        session.add(question)
        session.commit()
    else:
        equation = generate_equation_fail_vertical_line_test()
        graph = latex(equation)
        # not latex ing properly
        question=f"""Is this a function: """
        answer=f"""No this fails the vertical line test."""
        question = Question(unit=1, chapter=1.1, topic="is this graph a function?", question=question, answer=answer, graph=graph)
        session.add(question)
        session.commit()

def function_or_not_points():
    x = random.randint(0, 1)
    if x == 0:
        points = generate_points(5)
        question = f"""Determine if the following relation is a function: {points}"""
        answer = f"""Yes it is a function as there are unique Xs,passing the vertical line test."""
        question = Question(unit=1, chapter=1.1, topic="is this relation a function?", question=question, answer=answer)
        session.add(question)
        session.commit()
    else:
        points = generate_failed_vlt_points(5, 1)
        question = f"""Determine if the following relation is a function: {points}"""
        answer = f"""No it is not a function as there are multiple Xs that are the same, failing the vertical line test."""
        question = Question(unit=1, chapter=1.1, topic="is this relation a function?", question=question, answer=answer)
        session.add(question)
        session.commit()

def convert_to_interval_notation_single():
    symbol = [">", "<", ">=", "<="]
    symbol_latex = [">", "<", "\geq", "\leq"]
    side = ["left", "right", "center"]
    num = random.randint(-50, 50)
    side_num = random.randint(0, 1)
    symbol_num = random.randint(0, 3)
    
    inequality_latex = ""
    if side[side_num] == "left":
        inequality_latex += "x " + symbol_latex[symbol_num] + f"{num}" 
        converted = interval_notation_single(num, symbol[symbol_num], side[side_num])
        
    else:
        inequality_latex += f"{num} " + symbol_latex[symbol_num] + " x"
        converted = interval_notation_single(num, symbol[symbol_num], side[side_num])
        
    question = f"""Convert this inequality into interval notation: {inequality_latex}"""
    answer = f"""x ∈ {converted}"""
    question = Question(unit=1, chapter=1.1, topic="interval notation", question=question, answer=answer ,graph=None)
    session.add(question)
    session.commit()

def convert_to_interval_notation_double():
    symbolss = (['<=', '<'], ['>', '>='])
    symbolss_latex = (['\leq', '<'], ['>', '\geq'])
    less_or_greater = random.randint(0, 1)
    symbols = symbolss[less_or_greater]
    symbols_latex = symbolss_latex[less_or_greater]
    num_1 = random.randint(-50, 50)
    num_2 = random.randint(-50, 50)
    if (symbols == symbolss[0]):
        while num_1 == num_2 or num_1 > num_2:
            num_1 = random.randint(-50, 50)
            num_2 = random.randint(-50, 50)
    else:
        while num_1 == num_2 or num_1 < num_2:
            num_1 = random.randint(-50, 50)
            num_2 = random.randint(-50, 50)
        
    symbol_1_num = random.randint(0, 1)
    symbol_2_num = random.randint(0, 1)
    symbol_1 = symbols[symbol_1_num]
    symbol_2 = symbols[symbol_2_num]
    symbol_1_latex = symbols_latex[symbol_1_num]
    symbol_2_latex = symbols_latex[symbol_2_num]
    inequality = f"""{num_1} {symbol_1_latex} X {symbol_2_latex} {num_2}"""
    converted = interval_notation_between(num_1, symbol_1, num_2, symbol_2)
    
    question = f"""Convert this inequality into interval notation: {inequality}"""
    answer = f"""X ∈ {converted}"""
    question = Question(unit=1, chapter=1.1, topic="interval notation", question=question, answer=answer ,graph=None)
    session.add(question)
    session.commit()
    
    
def factoring():
    quadractic = generate_factorable_quadratic()
    solution = factor_quadratic_equation(quadractic)
    
    question = f"""Factor: {latex(quadractic)}"""
    answer = f"""{latex(solution)}"""
    question_to_add = Question(unit=1, chapter=0, topic="factoring quadractic equations", question=question, answer=answer, graph=None)
    session.add(question_to_add)
    session.commit()
    
def solving_quadractic():
    equation, answer = quadractic_equation()
    question = f"""Solve: {latex(equation)}"""
    answer = f"""Answer: x ∈ {latex(answer)}"""
    question_to_add = Question(unit=1, chapter=0, topic="solving quadratic equations", question=question, answer=answer, graph=None)
    session.add(question_to_add)
    session.commit()
    
# TODO: fix
def complete_the_square_problem():
    quadractic = generate_factorable_quadratic()
    completed = complete_the_square(quadractic)
    print(completed)

def degree_and_leading_coff():
    # NOTE: This will be unit 1, chapter 1, topic 1,
    # NOTE: Answer will be in one big latex with the answers plus some form of instructions on how to solve it
    # but not in depth
    # NOTE: The question will also be in one big latex. If the question contains a graph
    degree = random.randint(2, 4)
    coeffcient_range = (-10, 10)
    polynomial = generate_polynomial(degree, coeffcient_range)
    leading = leading_coeff(polynomial)
    polynomial = sympy.latex(polynomial)
    question = f"What is the degree and the leading coefficient of this polynomial: {polynomial}?"
    answer = f"""The degree of this function is the highest exponent in the polynomial which is {degree}. 
    Therefore the leading coefficent is the coefficent of the term that is degree {degree} which is {leading}"""

    question = Question(unit=1, chapter=1.1, topic='leading coefficient and degree of polynomial function',
                        question=question, answer=answer, graph=None)
    session.add(question)
    session.commit()


# TODO: Given Polynomial, what is the end behvaiour?

def end_behaviour_question():
    quadrants = ["Q1", "Q2", "Q2", "Q4"]
    q1 = random.randint(0, 3)
    q2 = random.randint(0, 3)
    while q1 == q2:
        q2 = random.randint(0, 3)
    print(q1, q2)
    end_behaviour_eq = end_behaviour(quadrants[q1], quadrants[q2], (-10, 10))
    polynomial = sympy.latex(end_behaviour_eq)
    question = f""""What is the end behaviour of this function {polynomial}?"""
    end_behaviour_answer = translate_end_behavior(quadrants[q1], quadrants[q2])
    answer = f"""Find where f(x) approaches when x->∞ and x ->-∞. Answer: {end_behaviour_answer}."""

    question = Question(unit=1, chapter=1.1, topic='end behaviour', question=question, answer=answer, graph=None)
    session.add(question)
    session.commit()


# TODO: given graph polynomial what is the end behavior

def end_behaviour__graph_question():
    quadrants = ["Q1", "Q2", "Q2", "Q4"]
    q1 = random.randint(0, 3)
    q2 = random.randint(0, 3)
    while q1 == q2:
        q2 = random.randint(0, 3)
    print(q1, q2)
    end_behaviour_eq = end_behaviour(quadrants[q1], quadrants[q2], (-10, 10))
    polynomial = sympy.latex(end_behaviour_eq)
    question = f""""What is the end behaviour of this graph?"""
    end_behaviour_answer = translate_end_behavior(quadrants[q1], quadrants[q2])
    answer = f"""Find where f(x) approaches when x->∞ and x ->-∞. Answer: {end_behaviour_answer}."""

    question = Question(unit=1, chapter=1.1, topic='end behaviour', question=question, answer=answer, graph=polynomial)
    session.add(question)
    session.commit()


# TODO: odd or even given a fucntion

def odd_or_even():
    degree = random.randint(2, 4)
    coeffcient_range = (-10, 10)
    polynomial = generate_polynomial(degree, coeffcient_range)
    answer = even_or_odd(polynomial)
    polynomial = sympy.latex(polynomial)
    question = f"""Show that the following function is even, odd or neither: {polynomial}"""
    question = Question(unit=1, chapter=1.1, topic='odd or even', question=question, answer=answer, graph=None)
    session.add(question)
    session.commit()


# TODO: domain and range of a function

def domain_range():
    types = [x**2, x**(1/2), 1/x]
    type_num = random.randint(0, 2)
    function_type = types[type_num]
    a = random.randint(-20, 20)
    d = random.randint(-20, 20)
    c = random.randint(-20, 20)
    k = random.randint(-20, 20)
    while a == 0 or d == 0 or c == 0 or k==0:
        a = random.randint(-20, 20)
        d = random.randint(-20, 20)
        c = random.randint(-20, 20)
        k = random.randint(-20, 20)
    function = transformation_of_function(function_type, a, k, c ,d)
    domain = function_domain(function)
    range = function_range(function)
    question = f"""What is the domain and range of this function: {latex(function)}"""
    answer = f"Domain: x ∈ {domain} Range: y ∈ {range}"
    question_to_add = Question(unit=0, chapter=0, topic='domain and range of functions', question=question, answer=answer, graph=None)
    session.add(question_to_add)
    session.commit()

# Points are stored in the graph attribute
def finite_differences_type_points():
    types = ['linear', 'quadractic', 'neither']
    differences = ['first', 'second', "neither first or second"]
    type_of_graph = random.randint(0, 2)
    type_of_graph = 0 #delete this
    coeffcient_range = (1, 4)
    if types[type_of_graph] == 1:
        degree = 1
        polynomial = generate_polynomial(degree, coeffcient_range)
        points = points_of_polynomial(polynomial)
        answer = all_differences(1, points)
    elif types[type_of_graph] == 2:
        degree = 2
        
        polynomial = generate_polynomial(degree, coeffcient_range)
        points = points_of_polynomial(polynomial)
        answer = all_differences(1, points)
    else:
        degree = 3
        polynomial = generate_polynomial(degree, coeffcient_range)
        points = points_of_polynomial(polynomial)
        answer = all_differences(1, points)
    points = points_to_string(points)
    question = f"""Given these points, determine if the function is linear, quadractic or neither. """
    answer = f"""It is {types[type_of_graph]}. {differences[type_of_graph].title()} diferences are the same. """
    question_to_add = Question(unit=0, topic="finite differences", question=question, answer=answer, graph=points)
    session.add(question_to_add)
    session.commit()
    
# degree of polynomial, find the value of leading coefficnet, and sign
def finite_differences_continued():
    coefficent_range = (-7, 7)
    degree = random.randint(1, 4)
    polynomial = generate_polynomial(degree, coefficent_range)
    points = points_of_polynomial(polynomial)
    difference = all_differences(degree, points)[-1]
    co = finite_difference(polynomial)/factorial(degree)
    points = points_to_string(points)
    if co < 0: sign = "+" 
    else: sign="-"
    question = f""""What is the leading coefficient and the sign of this polynomial given the table? """
    answer = f"""To find the leading coefficient, find the constant difference and divide it by the factorial of the degree. 
    The constant difference is {difference}. {difference}/{degree}! = {co}. Sign is {sign}. """
    question_to_add = Question(unit=1, chapter=1.2, topic = "constant differences", question=question, answer=answer, graph=points)
    session.add(question_to_add)
    session.commit()

def finite_differences_constant():
    coefficent_range = (-7, 7)
    degree = random.randint(2, 4)
    polynomial = generate_polynomial(degree, coefficent_range)
    constant_difference = finite_difference(polynomial)
    co = finite_difference(polynomial)/factorial(degree)
    question = f"""Find which finite difference is constant and its value of this polynomial: {latex(polynomial)}"""
    answer = f"""Since the degree of the polynomial is {degree}, the {degree} differences will be constant. To find the 
    value of the constant difference, multiply the leading coefficient and the factorial of the degree. {degree}!*{co} = {constant_difference}"""
    question_to_add = Question(unit=1, chapter=1.2, topic="constant differences", question=question, answer=answer, graph=None)
    session.add(question_to_add)
    session.commit()

# TODO: transformations of quadractic, vertex, charertistics
# currently not working
def quadractic_characteristics():
    coefficient_range  = (-7, 7)
    degree = 2
    polynomial = generate_polynomial(degree,coefficient_range)
    print(find_vertex(polynomial))

# TODO: Given image of graph, ask for the end behavior, even or odd, domain and range, symmetry. Table of intervals when function is positive, negative domain and range
# Describe the transformations
def transformations():
    parent_functions = [x**2, x**3, x**(1/2), 1/x]
    some_fracs = [1/2, 1/3, 1/4, -1/2, 1/2, -1/4, 1/5, -1/5, 2/6, 4/5]
    function = random.choice(parent_functions)
    a = random.choice([random.randint(-10, -1), random.randint(1, 10), random.choice(some_fracs)])
    k = random.choice([random.randint(-10, -1), random.randint(1, 10), random.choice(some_fracs)])
    c = random.choice([random.randint(-10, -1), random.randint(1, 10), random.choice(some_fracs)])
    d = random.choice([random.randint(-10, -1), random.randint(1, 10), random.choice(some_fracs)])
    transformed = transformation_of_function(function, a, k , c, d)
    transformations = transformation_explanation(a, k, c, d)
    transformations.extend([f"""a = {float_to_fraction(a)} c = {float_to_fraction(c)} d = {float_to_fraction(d)} k = {float_to_fraction(k)}"""])
    question = f"""Describe the transformations of the following function and find values of a, k, c, d: {latex(transformed)}"""
    answers = ', '.join(transformations)
    question_to_add = Question(unit=1, chapter=1.4, topic="transformations of polynomials", question=question, answer=answers)
    session.add(question_to_add)
    session.commit()

# Given a description of the transformations of the parent function, write a function of it
def transformations_2():
    parent_functions = [x**2, x**3, x**(1/2), 1/x]
    some_fracs = [1/2, 1/3, 1/4, -1/2, 1/2, -1/4, 1/5, -1/5, 2/6, 4/5]
    function = random.choice(parent_functions)
    a = random.choice([random.randint(-10, -1), random.randint(1, 10), random.choice(some_fracs)])
    k = random.choice([random.randint(-10, -1), random.randint(1, 10), random.choice(some_fracs)])
    c = random.choice([random.randint(-10, -1), random.randint(1, 10), random.choice(some_fracs)])
    d = random.choice([random.randint(-10, -1), random.randint(1, 10), random.choice(some_fracs)])
    transformed = transformation_of_function(function, a, k , c, d)
    transformations = transformation_explanation(a, k, c, d)
    question = f"""Given the transformations of this parent function {latex(function)}, write the transformed equation for this function: {', '.join(transformations)}"""
    answer = f"""y = {latex(transformed)}"""
    question_to_add = Question(unit=1, chapter=1.4, topic="transformations of polynomials", question=question, answer=answer)
    session.add(question_to_add)
    session.commit()
    
# TODO: given the parent function and the transformed functions graph

def transformations_3():
    parent_functions = [x**2, x**3, x**(1/2), 1/x]
    some_fracs = [1/2, 1/3, 1/4, -1/2, 1/2, -1/4, 1/5, -1/5, 2/6, 4/5]
    function = random.choice(parent_functions)
    a = random.choice([random.randint(-10, -1), random.randint(1, 10), random.choice(some_fracs)])
    k = random.choice([random.randint(-10, -1), random.randint(1, 10), random.choice(some_fracs)])
    c = random.choice([random.randint(-10, -1), random.randint(1, 10), random.choice(some_fracs)])
    d = random.choice([random.randint(-10, -1), random.randint(1, 10), random.choice(some_fracs)])
    transformed = transformation_of_function(function, a, k , c, d)
    question = f"""Graph this function: {transformed}"""
    question_to_add = Question(unit=1, chapter=1.4, topic="transformations of polynomial functions: graphing", question=question, answer=None, graph=latex(transformed))
    session.add(question_to_add)
    session.commit()

# TODO: Given the graph, end behavior, x-intercepts, global maximia,
# add other characteristics
# Not working 
def characteristics_1():
    polynomial = generate_random_polynomial_char()[0]
    polynomial = polynomial * random.sample([random.randint(-10, -1), random.randint(1, 10)], 1)[0]
    characteristics = analyze_expression(polynomial)
    question = f"""Find the degree, the coefficent, x-intercepts, and the intervals of this function: {latex(polynomial)}"""
    answer = ", ".join(characteristics)
    question_to_add = Question(unit=1, chapter=1.4, topic="characteristics of polynomials from equation", question=question, answer=answer, graph=latex(polynomial))
    session.add(question_to_add)
    session.commit()

# from graph
def characteristics_2():
    polynomial = generate_random_polynomial_char()[0]
    polynomial = polynomial * random.sample([random.randint(-10, -1), random.randint(1, 10)], 1)[0]
    characteristics = analyze_expression2(polynomial)
    answer = ", ".join(characteristics)
    question = f"""Find the least possible degree, x-intercepts, and the intervals of this function based on the graph"""
    question_to_add = Question(unit=1, chapter=1.4, topic="characteristics of polynomials from graph", question=question, answer=answer, graph=latex(polynomial))
    session.add(question_to_add)
    session.commit()
    
# TODO: Given equation Ask for degree, leading, coefficent end behaviour, possible number of turning points, x intercepts, y-ints.

def characteristics_3():
    polynomial = generate_polynomial(random.randint(1, 10), [1, 10])
    degree = polynomial_degree(polynomial)
    lc = leading_coeff(polynomial)
    eb = end_behaviour(polynomial)
    tp = turning_points(polynomial)
    x_intercept = x_int(polynomial)
    y_intercept = y_int(polynomial)
    answer = f"""{degree}, {lc}, {eb}, {tp}, {x_intercept}, {y_intercept}"""

    question = f"""Find the degree, leading coefficient, end behaviour, possible number of turning points, x-intercepts and y-intercept of f(x) = {latex(polynomial)}"""
    question_to_add = Question(unit=1, chapter=1.4, topic="characteristics of polynomials from graph", question=question, answer=answer, graph=None)
    session.add(question_to_add)
    session.commit()
    

# TODO: Given a image of a graph. Ask for leading coefficient, even or odd degree, end behaviour, symmetry, number of turning points, number x-intercepts, least possible degree intervals where f(x) <0 or f(x) > 0

def create_equation_chars():
    # Generate random polynomial characteristics
    equation, equation_str, coefficient, root_desc, first_quadrant, second_quadrant, degree= generate_random_polynomial_char()
    question = f"""Write an polynomial based on the descriptions: Degree: {degree}, {', '.join(root_desc)}, Start quadrant: {first_quadrant} End quadrant: {second_quadrant} """
    answer = f"""Equation: {equation_str} {coefficient}"""
    question_to_add = Question(unit=1, chapter=1.4, topic="polynomial properties", question=question, answer=answer)
    session.add(question_to_add)
    session.commit()

# TODO: Write an equation based on images* gotta figure out the details for this one

def create_equation_from_image():
    equation, equation_solve, equation_str, coefficient, root_desc, first_quadrant, second_quadrant, degree= generate_random_polynomial_char()
    question = f"""Write an polynomial equation based on the graph shown: """
    numerator = random.randint(-100, 100)
    denominator = random.randint(1, 100)
    rational_number = sympy.Rational(numerator, denominator)
    equation = equation*rational_number
    y_intercept = equation.subs(x, 0)
    while y_intercept == 0:
        equation, equation_solve, equation_str, coefficient, root_desc, first_quadrant, second_quadrant, degree= generate_random_polynomial_char()
        numerator = random.randint(-100, 100)
        denominator = random.randint(1, 100)
        rational_number = sympy.Rational(numerator, denominator)
        equation = equation*rational_number
        y_intercept = equation.subs(x, 0)
    leading = solve_leading_coefficient(equation_solve, y_intercept)
    answer = f"""To write the polynomial equation based on the graph, first find the roots of the function and write the possible equation in factored form. Then find the y-intercept or some other point, sub it in and solve for the leading coefficent a. 
    In factored form, the potential polynomial equation is {equation_str}, where a is the leading coefficent. The y-intercept is {y_intercept}. Plug in (0, {y_intercept}) into the factored form and solve for a which is {leading}. Therefore, the equation 
    of this polynomial function is {equation}."""
    question_to_add = Question(unit=1, chapter=1.3, topic="finding polynomial equation from graph", question=question, answer=answer, graph=latex(equation))
    session.add(question_to_add)
    session.commit()

# IROC, AROC

def IROC():
    coefficent_range = (-7, 7)
    degree = random.randint(1, 4)
    polynomial = generate_polynomial(degree, coefficent_range)
    x = random.randint(-20, 20)
    question = f"""Find the instantaneous rate of change at x = {x} of the polynomial: f(x) = {latex(polynomial)}"""
    instant_rate_change_answer = instant_rate_of_change(polynomial, x)
    answer = f"""The instantaneous rate of change formula: f(x+0.0001) - f(x) / 0.0001. Applying the formula to {latex(polynomial)} at x = {x}, the instantaneous rate of change is {instant_rate_change_answer} """
    question_to_add = Question(unit=1, chapter=1.5, topic="instantaneous rate of change", question=question, answer=answer)
    session.add(question_to_add)
    session.commit()

def AROC():
    coefficent_range = (-7, 7)
    degree = random.randint(1, 4)
    polynomial = generate_polynomial(degree, coefficent_range)
    x = random.randint(-20, -10)
    x2 = random.randint(x2, 10)
    question = f"""Find the average rate of change between x = {x} and x = {x2} of the polynomial: f(x) = {latex(polynomial)}"""
    average_rate_of_change_answer = average_rate_of_change(polynomial, x)
    answer = f"""The average rate of change formula: (f(b) - f(a)) / (b - a). Applying the formula to {latex(polynomial)} as a = {x} and b = {x2}, the average rate of change is {average_rate_of_change_answer} """
    question_to_add = Question(unit=1, chapter=1.5, topic="average rate of change", question=question, answer=answer)
    session.add(question_to_add)
    session.commit()



if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)  # Forcing verbose to be true will provide full details of doctests
