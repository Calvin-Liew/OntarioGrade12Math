"""Math Problem Generator - Unit 1: Polynomial Functions

Description
============================================
This module contains code for Unit 1 functions
"""

import random
import typing
import sympy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from sympy import degree, factorial, symbols, simplify, Eq
from sympy.abc import x

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
    graph = Column(String)

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

    >>> turning_points(x**3)
    0
    >>> turning_points(x**2)
    1
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


def characteristic(polynomial):
    """
    Returns a basic description about the polynomial function

    >>> characteristic(x**2-1)
    x-int: -1, 1
    y-int: -1
    Domain: ℝ
    Range: [-1, ∞)
    Turning Points: 1
    """
    x_intercept = x_int(polynomial)
    y_intercept = y_int(polynomial)
    domain = function_domain(polynomial)
    range = function_range(polynomial)
    points = turning_points(polynomial)

    return_str = 'x-int: '
    for x_point in x_intercept:
        return_str += f'{x_point}, '
    return_str = return_str[:-2]  # Take out last two elements
    return_str = return_str + '\n'

    return_str += f'y-int: {y_intercept} \n'
    return_str += f'Domain: {domain} \n'
    return_str += f'Range: {range} \nTurning Points: {points}'

    print(return_str)  # \n does not work for return


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
        desc.append(f"Vertically stretched by a factor of {abs(a)}")
    elif 0 < abs(a) < 1:
        desc.append(f"Vertically compressed by a factor of {abs(a)}")
    if a < 0:
        desc.append(f"Reflection in x-axis")
    if c > 0:
        desc.append(f"Vertical translation {abs(c)} units upwards")
    elif c < 0:
        desc.append(f"Vertical translation of {abs(c)} units downwards")
    if abs(k) > 1:
        desc.append(f"Horizontally compressed by a factor of 1/{abs(k)}")
    elif 0 < abs(k) < 1:
        desc.append(f"Horizontally stretched by a factor of 1/{abs(k)}")
    if k < 0:
        desc.append(f"Reflection in y-axis")
    if d > 0:
        desc.append(f"Horizontal translation {abs(d)} units to the right")
    elif d < 0:
        desc.append(f"Horziontal translation {abs(d)} units to the left")
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


# TODO: Insert Questions functions to do
# NOTE: Our current schema is in the form of (id, unit, chapter, topic, answer, graph_equation)
# NOTE: Confirm that we can put equations and points into desmo api

# Function will return the question and the answer in the best way
def degree_and_leading_coff():
    # NOTE: This will be unit 1, chapter 1, topic 1,
    # NOTE: Answer will be in one big latex with the answers plus some form of instructions on how to solve it
    # but not in depth
    # NOTE: The question will also be in one big latex. If the question contains a graph
    degree = random.randint(2, 4)
    coeffcient_range = (-10, 10)
    polynomial = generate_polynomial(degree, coeffcient_range)
    leading = leading_coeff(polynomial)
    question = f"What is the degree and the leading coefficient of this polynomial: {polynomial}"
    answer = f"""The degree of this function is the highest exponent in the polynomial which is {degree}. 
    Therefore the leading coefficent is the coefficent of the term that is degree {degree} which is {leading}"""

    question = Question(unit=1, chapter=1.1, topic='leading coefficient and degree of polynomial function',
                        question=question, answer=answer, graph=None)
    session.add(question)
    session.commit()


# TODO:

if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)  # Forcing verbose to be true will provide full details of doctests
