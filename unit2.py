"""Math Problem Generator - Unit 2: Polynomial Equations

Description
============================================
This module contains code for Unit 2 functions
"""
import unit1
import sympy
import random
import typing
from sympy.abc import x
from sympy import symbols, Function, Symbol, solve, expand, solve, Poly
from sympy.solvers.inequalities import reduce_rational_inequalities
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker


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


def factorable(degree: int, coefficient_range: typing.Tuple[int, int]) -> typing.Dict:
    """
    Returns a polynomial function that is factorable and the answers in the format of:
    {polynomial: [answers]}
    """
    function_so_far = 1
    for _ in range(degree):
        function_so_far *= unit1.generate_polynomial(1, coefficient_range)
    return {expand(function_so_far): solve(function_so_far)}


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


def find_remainder(big_poly, small_poly):
    """Return the remainder of the division of two functions <big_poly> and <small_poly>

    Precondition: deg of <big_poly> > deg of <small_poly>

    >>> find_remainder(x**2 - 4, x + 2)
    0
    >>> find_remainder(x**2 - 4, x + 1)
    -3
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

    >>> is_factor(x**2, 0)
    True
    >>> is_factor(x**2 - 1, 1)
    True
    >>> is_factor(x**2, 1)
    False
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
def rational_zero(polynomial: sympy.Poly, a: int, b: int) -> bool:
    """
    Return whether <b>/<a> is a zero for the polynomial <polynomial>

    Preconditions:
    - a != 0
    """
    return polynomial.subs(x, b/a) == 0
# TODO: given a polynomial fucntion. a is the leading coffeicnet. b is the constant.
# The possible factors of a function is any combination of facotrs of b/factors of a.

def find_factors(x: int) -> list[int]:
    """
    Return the factors of <x>
    """
    factors = set()
    factors.add(1)
    factors.add(x)
    for i in range(2, x//2):
        if x % i == 0:
            factors.add(i)
            factors.add(x//i)
    factors = list(factors)
    factors.sort()
    return factors

def find_polynomial_factors(a: int, b: int) -> list[str]:
    """
    Return the possible factors of a polynomial which has the leading coefficient <a>
    and the constant <b>

    Preconditions:
    - a != 0
    """
    a_factors = find_factors(a)
    b_factors = find_factors(b)
    factors = []

    for i in a_factors:
        for j in b_factors:
            factors.append(str(j) + '/' + str(i))
    
    return factors

# TODO: find possible factors rational zero thereom given a function,
# return a factor ie. if -2 is a factor then return x + 2


def compare(polynomial, inequality, value) -> str:
    """
    Evaluates inequality by comparing between polynomial and value.

    NOTE: Consider using solve_poly_inequalities instead of solveset

    Preconditions:
    - polynomial is a valid polynomial function from <generate_polynomial>
    - inequality in ['<', '>', '<=', '>=']
    - isinstance(value, float) == True

    >>> compare(x**2, '<', 3)
    '(-√3, √3)'
    >>> compare(x**2, '<=', 4)
    '[-2, 2]'
    >>> compare(x**3, '>', 1)
    '(1, ∞)'
    >>> compare(x**4, '>=', 4)
    '(-∞, -√2] ∪ [√2, ∞)'
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


def replace_leading_coefficient_with_variable(eq, variable_name='a'):
    # Parse the equation
    eq = sympy.sympify(eq)
    
    if eq.is_polynomial(x):  # Replace 'x' with the appropriate symbol if needed
        # Get the leading coefficient
        leading_coeff = eq.as_poly().all_coeffs()[0]
        
        # Create a new variable
        new_var = sympy.symbols(variable_name)
        
        # Replace the leading coefficient with the new variable
        modified_eq = eq - leading_coeff * x**eq.as_poly().degree() + new_var * x**eq.as_poly().degree()
        
        return leading_coeff, modified_eq
    else:
        raise ValueError("Input equation is not a polynomial.")


###############################################################################
# Question Functions
###############################################################################

def remainder_theorem():
    degree = random.randint(3, 6)
    coeffcient_range = (-10, 10)
    while(coeffcient_range == 0):
        coeffcient_range = (-10, 10)
    polynomials = generate_poly_big_small1(degree, coeffcient_range)
    polynomial1 = polynomials[0]
    polynomial2 = polynomials[1]
    question = f"""Use the remainder theorem to find the remiander of {sympy.latex(polynomial2)} ÷ {sympy.latex(polynomial1)}"""
    remainder_answer = remainder(polynomial2, polynomial1)
    answer = f"""Find the solution of {sympy.latex(polynomial1)} and plug it in to {sympy.latex(polynomial2)} to find the remainder. Answer: {remainder_answer}"""
    question_to_add = Question(unit=2, topic='Remainder Theorem',
                        question=question, answer=answer)
    session.add(question_to_add)
    session.commit()
    
def remainder_theorem_2():
    degree = random.randint(3, 6)
    coeffcient_range = (-10, 10)
    while(coeffcient_range == 0):
        coeffcient_range = (-10, 10)
    polynomials = generate_poly_big_small1(degree, coeffcient_range)
    polynomial1 = polynomials[0]
    polynomial2 = polynomials[1]
    polynomial3 = replace_leading_coefficient_with_variable(polynomial2)
    remain_answer = remainder(polynomial2, polynomial1)
    question = f"""If {sympy.latex(polynomial3[1])} is divided by {sympy.latex(polynomial1)}, the remainder is {remain_answer}. Find the value of a. """
    answer = f"""If the remainder is {remain_answer} then the equation for the variable a by subsituting the solution of {sympy.latex(polynomial2)} into {sympy.latex(polynomial3[1])} and setting it equal to {remain_answer}. Solve for a, a = {sympy.latex(polynomial3[0])}. """
    question_to_add = Question(unit=2, topic='Remainder Theorem', question=question, answer=answer)
    session.add(question_to_add)
    session.commit()

# TODO: Factor theorem

def factor_theorem():
    pass

# TODO: Solve with long division

# TODO: Solve with synthetic division

# TODO: Divide the following polynomails and write the result

# TODO: Determine whether each given value of x is a zero of the given function

# TODO: Factor fully

# TODO: Solve the following polynomials by factoring

# TODO: Write a general factored equation for the family functions based on the given zeros and one point

# TODO: Solve polynomial inequalities


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)  # Forcing verbose to be true will provide full details of doctests
