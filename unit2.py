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
  
  # TODO: Generating one polynomial function, one bionomial function(degree 1), one with a bigger degree than the other so that we can divide them
  # Ex. degree 3 and degree 1
  
  # TODO: Generate two polynomial funcntions, one with a bigger degree than the other 
  
  # TODO: Given two functions, one bigger, one smaller, return the remiander. (from plugging in the solution of the smaller 
  # function ie. 2 from (x-2) into the bigger function)
  
  # TODO: Generate two functions where the bigger one has a constant K, and with the remainder for questions 
  # that ask what the coffeicent is given the constant and the two functions that divide
  
  # NOTE: It would be better if we could actually show the steps to divide the function using long or synthetic divison
  # TODO: synthetic(short) division. Given a polynomial and a bionomial function
  
  # TODO: long division Given a polynomial and a bionomial function
  
  #TODO: factor theorem stuff 
"""Factoor theorem states that x-b is a factor of polynomial P(x) iff P(b) = 0 
and ax-b is a factor if P(b/a) = 0 """

"""What we could do is, already create some factors given a degree, than expand it and return the full equation"""

  #TODO: Is factor. Given a factor and a equation, check if its a factor 
  
  # Series of functions that provide 'factorable' equations such that the person has to divide one or twice and end up 
  # with a easily factorable equation (like quadractic or simple linear) to completely factor it 
  #TODO: we may have to do a little bit of hardcoding in this one. 
  
  # TODO: generate factorable cubic function. generate three factors ie x-4, x-3, 3x+2. 
  # combine the three factors into one equation. 
  
  # TODO: generate factorable quartic function. Generate four factors, combine the four factors into 
  # one equation  
  
  # TODO: rational zero theorem 
  # TODO: given a polynomial fucntion. a is the leading coffeicnet. b is the constant. 
  # The possible factors of a function is any combination of facotrs of b/factors of a.
  
  # TODO: find possible factors rational zero thereom given a function, 
  # return a factor ie. if -2 is a factor than return x + 2
  
  # TODO: inequalities of polynomials. (with factorable and nonfactorable(cubic) polynomials)
  
  # TODO: provide the x-intercepts of a factorable polynomial. For questions for people 
  # to write the equation of the polynomial given a point or not 
  
  
  

