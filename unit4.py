"""Math Problem Generator - Unit 4: Trigonometry

Description
============================================
This module contains code for Unit 4 functions
"""

import sympy
import random
from sympy.abc import x
from sympy import pi


# from sympy.solvers.inequalities import reduce_rational_inequalities


def rad_to_degree(radian: int | sympy.core.numbers.Pi) -> int:
    """
    Converts radians to degrees
    Precondition:
    - radian represents a special angle such as pi, pi / 2, pi / 3, pi / 4, pi / 6 etc.
    >>> rad_to_degree(pi / 2)
    90
    """
    return round(radian * 180 / pi, 1)


def degree_to_rad(degree: int) -> int:
    """
    Converts degrees to radians
    Preconditions:
    - degree represents a speical angle such as 30, 45, 60, 90 etc.
    >>> degree_to_rad(90)
    pi/2
    """
    return degree * pi / 180


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


def generate_angle():
    """
    Generates a random special angle in radians (pi format)
    """
    special_angles = [0, pi / 6, pi / 4, pi / 3, pi / 2, 2 * pi / 3, 3 * pi / 4, 5 * pi / 6, pi, 7 * pi / 6, 5 * pi / 4,
                      4 * pi / 3, 3 * pi / 2, 5 * pi / 3, 11 * pi / 6, 2 * pi]
    # 0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 330, 360
    return random.choice(special_angles)


# TODO: Provide a simple diagram of an angle? Might be tough
# Can prob use desmos for this https://www.youtube.com/watch?v=RUm0NevyrlA


def rad_to_degree_explain(radian: int | sympy.core.numbers.Pi):
    """
    Converts radians to degrees and explains the degree return
    Precondition:
    - radian represents a special angle such as pi, pi / 2, pi / 3, pi / 4, pi / 6 etc.
    """
    str_so_far = f"When converting {radian} into degree format, we must multiply the radian with 180 / pi. \n" \
                 f"That means {radian} * 180 / pi will result in {rad_to_degree(radian)}."

    print(str_so_far)


def degree_to_rad_explain(degree: int):
    """
    Converts degrees to radians
    Preconditions:
    - degree represents a speical angle such as 30, 45, 60, 90 etc.
    """
    str_so_far = f"When converting {degree} into radian format, we must multiply the degree with pi / 180. \n" \
                 f"That means {degree} * pi / 180 will result in {degree_to_rad(degree)}."

    print(str_so_far)


def calculate_angular_velocity(revolutions: int) -> list[int]:
    """
    Returns a list where index 0 is the angular velocity in degree and index 1 is the angular
    velocity in radians

    >>> calculate_angular_velocity(7200)
    [43200.0, 240*pi]
    """
    # Degrees per second
    dps = revolutions * 360 / 60
    # Radians per second
    rps = revolutions * 2 * pi / 60

    return [dps, rps]


# TODO: Find the related acute angle and the principal angle and give diagram
def find_raa(principal_angle: int | sympy.core.numbers.Pi) -> int | sympy.core.numbers.Pi:
    """
    Return the related acute angle from the principal angle

    Preconditions:
    - principal_angle not in [0, 90, 180, 270, 360, pi / 2, pi, 3 * pi / 2, 2 * pi]
    - 0 < principal_angle < 360 or 0 < principal_angle < 2 * pi
    """
    if isinstance(principal_angle, sympy.core.numbers.Pi):    # When principal angle is in radians
        if principal_angle < pi / 2:    # Quadrant 1
            return principal_angle
        elif principal_angle > pi / 2 and principal_angle < pi:    # Quadrant 2
            return pi - principal_angle
        elif principal_angle > pi and principal_angle < 3 * pi / 2:
            return principal_angle - pi
        else:   # Quadrant 4
            return 2 * pi - principal_angle
    else:   # When principal angle is in degrees
        if principal_angle < 90:    # Quadrant 1
            return principal_angle
        elif principal_angle > 90 and principal_angle < 180:    # Quadrant 2
            return 180 - principal_angle
        elif principal_angle > 180 and principal_angle < 270:
            return principal_angle - 180
        else:   # Quadrant 4
            return 360 - principal_angle


# TODO: given some random radian find the exact value of sinx or tanx or cosx or cscx secx cotx
# TODO: a helper function to show simple work for the function above

# TODO: Genrate a equation of a combination of random trig functions and simplfy it in exact values

# TODO: Trig word problem, kite flying or ladder leaning on wall, or some other scenario that requires someone to look
# for the distance or heieght etc


###############################################################################
# Question Functions
###############################################################################

if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)  # Forcing verbose to be true will provide full details of doctests
