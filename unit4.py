"""Math Problem Generator - Unit 4: Trigonometry

Description
============================================
This module contains code for Unit 4 functions
"""

import sympy
# from typing import Tuple, List, Dict
# from sympy import symbols, Function, Symbol, solve, expand, solve, Poly
# from sympy.abc import x, y
# from sympy.solvers.inequalities import reduce_rational_inequalities


def rad_to_degree(radian: int) -> int:
    """Converts radians to degrees and round to the first decimal point
    """
    return round(radian * 180 / sympy.pi, 1)


def degree_to_rad(degree: int) -> int:
    """Converts degrees to radians and round to the first decimal point
    """
    return round(degree * sympy.pi / 180, 1)


# def sin(radian) -> float:
#     """Evaluates sin function
#     """
#     return sympy.sin(radian)
#
#
# def cos(radian) -> float:
#     """Evaluates cos function
#     """
#     return syp.cos(radian)
#
#
# def tan(radian) -> float:
#     """Evaluates tan function
#     """
#     return syp.tan(radian)
#
#
# def csc(radian) -> float:
#     """Evaluates csc function
#     """
#     return syp.csc(radian)
#
#
# def sec(radian) -> float:
#     """Evaluates sec function
#     """
#     return syp.sec(radian)
#
#
# def cot(radian) -> float:
#     """Evaluates sin function
#     """
#     return syp.cot(radian)

#Unit 4 Planning 

#TODO: Generate random angle in radian or degree. Maybe we need to specific range

#TODO: Trig ratios of a given angle 

#TODO: Provide a simple diagram of an angle? Might be tough 

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





 
