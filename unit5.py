"""Math Problem Generator - Unit 5: Trigonometry Functions

Description
============================================
This module contains code for Unit 5 functions
"""

import sympy
import random
from sympy.abc import x
from sympy import pi, sin, cos, tan, csc, sec, cot


# TODOS:

# Remember period, cycle, amp


def generate_trig(trig_function, a: float, k: float, c: float, d: float) -> sympy.sin | sympy.cos | sympy.tan:
    """
    Generates sin, cos or tan graph equation

    Preconditions:
    - trig_function in [sin, cos, tan]
    """
    function_so_far = trig_function(x)
    function_so_far = function_so_far.subs(x, k * (x - d))  # Horizontal shift and strech
    function_so_far = function_so_far + c  # Vertical shift
    function_so_far = a * function_so_far  # Vertical strech
    return function_so_far


# TODO: Describe the transformations

def transformation_explanation(a: float, k: float, c: float, d: float) -> list:
    """
    Return simple word descriptions of each transformation
    """
    # desc = []
    # if abs(a) > 1:
    #     desc.append(f"Vertically stretched by a factor of {abs(a)}")
    # elif 0 < abs(a) < 1:
    #     desc.append(f"Vertically compressed by a factor of {abs(a)}")
    # if a < 0:
    #     desc.append(f"Reflection in x-axis")
    # if c > 0:
    #     desc.append(f"Vertical translation {abs(c)} units upwards")
    # elif c < 0:
    #     desc.append(f"Vertical translation of {abs(c)} units downwards")
    # if abs(k) > 1:
    #     desc.append(f"Horizontally compressed by a factor of 1/{abs(k)}")
    # elif 0 < abs(k) < 1:
    #     desc.append(f"Horizontally stretched by a factor of 1/{abs(k)}")
    # if k < 0:
    #     desc.append(f"Reflection in y-axis")
    # if d > 0:
    #     desc.append(f"Horizontal translation {abs(d)} units to the right")
    # elif d < 0:
    #     desc.append(f"Horziontal translation {abs(d)} units to the left")
    # return desc
    raise NotImplementedError


# TODO: Give a equation of graph and one cycle (give different quadrants)


def generate_cycle_trig():
    """
    Generates a trigonometry function but it restrict it to one cycle
    """
    raise NotImplementedError


# TODO: characteristics of a trig function (cos/tan/sin)
# Provide attributes of ammplitude, max, min, axis of the curve, PLUS DOMAIN AND RANGE
def trig_domain(trig_function):
    """
    Returns domain of <trig_function> in str format

    >>> trig_domain(sin(x))
    'ℝ'
    """
    domain = sympy.calculus.util.continuous_domain(trig_function, x, sympy.S.Reals)
    print(sympy.printing.pretty(domain)) 


def trig_range(trig_function) -> str:
    """
    Returns range of rational in str format

    >>> trig_range(sin(x))
    '[-1, 1]'
    >>> trig_range(tan(x))
    '(-∞, ∞)'
    """
    Range = sympy.calculus.util.function_range(trig_function, x, sympy.S.Reals)
    return sympy.printing.pretty(Range)


def trig_characteristic1(trig_function):
    """
    Prints the characteristics of <trig_function>.
    These attributes include amplitude, max, min, axis of the curve, domain and range.

    Preconditions:
    - trig_function is either a sin, cos or tan function
    """
    raise NotImplementedError


# TODO: Characterisitcs of reciproocl trig graphs, domain, range

def trig_characteristic2(trig_function):
    """
    Prints the characteristics of <trig_function>.
    These attributes include amplitude, max, min, axis of the curve, domain and range.

    Preconditions:
    - trig_function is either a csc, sec or cot function
    """
    raise NotImplementedError


# TODO: some word problems of trig functions

# TODO: transformations of trig functions stuff

# TODO: Solving trig functions. SO we have to generate some random
# trig equations first


def trig_aroc(trig_function, x1, x2) -> float:
    """
    Returns the average rate of change of <trig_function> given two x-values

    >>> trig_aroc(sin(x), pi / 2, 0)
    2.0/pi
    """
    point1 = (x1, trig_function.evalf(subs={x: x1}))
    point2 = (x2, trig_function.evalf(subs={x: x2}))
    return (point1[1] - point2[1]) / (point1[0] - point2[0])


def trig_iroc(trig_function, x1) -> float:
    """
    Returns the instantaneous rate of change at a given x in <trig_function>.

    >>> trig_iroc(sin(x), pi / 2)
    -0.e-189
    """
    derivative = sympy.diff(trig_function, x)
    slope = derivative.subs(x, x1)
    return slope


# TODO: trig proving stuff


###############################################################################
# Question Functions
###############################################################################

# TODO: Sketch the graph based on given characteristic

# TODO: Identify characteristic

# TODO: Application (Ladder, sunlight)

# TODO: State key properties

# TODO: Write trig function based on charactersitics

# TODO: Solve trig function

# TODO: AROC IROC

# TODO: Determine interval where function is greater 

if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)  # Forcing verbose to be true will provide full details of doctests
