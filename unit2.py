import random
import sympy as syp
from typing import Tuple, List, Dict
from sympy import symbols, Function, Symbol, solve, expand, solve, Poly
from sympy.abc import x, y
from sympy.solvers.inequalities import reduce_rational_inequalities
import unit1


# TODO: why x is not defined
# def quotient(polynomial1, polynomial2):
#   f = polynomial1
#   g = polynomial2
#   q, r = sympy.div(f, g, domain ='QQ')
#   return q

# def remainder(polynomial1, polynomial2):
#   f = polynomial1
#   g = polynomial2
#   q, r = sympy.div(f, g, domain ='QQ')
#   return r

def factorable(degree: int, coefficient_range: Tuple[int, int]) -> Dict:
    """Returns a polynomial function that is factorable and the answers
  """
    function_so_far = 1
    for _ in range(degree):
        function_so_far *= unit1.generate_polynomial(1, coefficient_range)
    return {expand(function_so_far): solve(function_so_far)}

# TODO:
