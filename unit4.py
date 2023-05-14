"""Math Problem Generator - Unit 4: Trigonometry

Description
============================================
This module contains code for Unit 4 functions
"""

import sympy
from sympy.abc import x
from sympy import pi
# from sympy.solvers.inequalities import reduce_rational_inequalities


# def rad_to_degree(radian: int) -> int:
#     """Converts radians to degrees and round to the first decimal point
#     """
#     return round(radian * 180 / pi, 1)
#
#
# def degree_to_rad(degree: int) -> int:
#     """Converts degrees to radians and round to the first decimal point
#     """
#     return round(degree * pi / 180, 1)


def sin(radian) -> sympy.core.numbers:
    """Evaluates sin function

    >>> sympy.sin(pi / 2)
    1
    >>> sympy.sin(pi)
    0
    """
    return sympy.sin(radian)


def cos(radian) -> sympy.core.numbers:
    """Evaluates cos function

    >>> sympy.cos(pi / 2)
    0
    >>> sympy.cos(pi)
    -1
    """
    return sympy.cos(radian)


def tan(radian) -> sympy.core.numbers:
    """Evaluates tan function

    >>> tan(0)
    0
    >>> tan(pi / 2)
    zoo
    """
    # zoo is complex infinity https://en.wikipedia.org/wiki/Complex_infinity#Complex_analysis
    return sympy.tan(radian)


def csc(radian) -> sympy.core.numbers:
    """Evaluates csc function

    >>> csc(pi / 6)
    2
    """
    return sympy.csc(radian)


def sec(radian) -> sympy.core.numbers:
    """Evaluates sec function

    >>> sec(pi)
    -1
    """
    return sympy.sec(radian)


def cot(radian) -> sympy.core.numbers:
    """Evaluates sin function

    >>> cot(pi / 4)
    1
    """
    return sympy.cot(radian)


#Unit 4 Planning

#TODO: Generate random angle in radian or degree. Maybe we need to specific range
# Have the range between 0 degrees and 360 degrees maybe

#TODO: Trig ratios of a given angle

#TODO: Provide a simple diagram of an angle? Might be tough
# Can prob use desmos for this https://www.youtube.com/watch?v=RUm0NevyrlA

#TODO: Convert degree to radian and vice versa showing work

#TODO: Angular velocity questions
# In format of The hard disk in a personal computer rotates at x rpm (revolutions per minute), determien its
# angular velocity

#TODO: Find the related acute angle and the principal angle and give diagram

#TODO: given some random radian find the exact value of sinx or tanx or cosx or cscx secx cotx
#TODO: a helper function to show simple work for the function above

#TODO: Genrate a equation of a combination of random trig functions and simplfy it in exact values

#TODO: Trig word problem, kite flying or ladder leaning on wall, or some other scenario that requires someone to look
# for the distance or heieght etc

if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)  # Forcing verbose to be true will provide full details of doctests
