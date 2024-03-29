"""Math Problem Generator - Unit 4: Trigonometry

Description
============================================
This module contains code for Unit 4 functions
"""

import sympy
import random
from sympy.abc import x
from sympy import pi, sin, cos, tan, csc, sec, cot
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///questions.db", echo=True)
Base = declarative_base()


class Question(Base):
    """
    ...
    """
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


def generate_angle():
    """
    Generates a random special angle in radians (pi format)
    """
    special_angles = [0, pi / 6, pi / 4, pi / 3, pi / 2, 2 * pi / 3, 3 * pi / 4, 5 * pi / 6, pi, 7 * pi / 6, 5 * pi / 4,
                      4 * pi / 3, 3 * pi / 2, 5 * pi / 3, 11 * pi / 6, 2 * pi]
    # 0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 330, 360
    return random.choice(special_angles)


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


def find_raa(principal_angle: int | sympy.core.numbers.Pi) -> int | sympy.core.numbers.Pi:
    """
    Return the related acute angle from the principal angle

    Preconditions:
    - principal_angle not in [0, 90, 180, 270, 360, pi / 2, pi, 3 * pi / 2, 2 * pi]
    - 0 < principal_angle < 360 or 0 < principal_angle < 2 * pi
    """
    if isinstance(principal_angle, sympy.core.numbers.Pi):  # When principal angle is in radians
        if principal_angle < pi / 2:  # Quadrant 1
            return principal_angle
        elif principal_angle > pi / 2 and principal_angle < pi:  # Quadrant 2
            return pi - principal_angle
        elif principal_angle > pi and principal_angle < 3 * pi / 2:
            return principal_angle - pi
        else:  # Quadrant 4
            return 2 * pi - principal_angle
    else:  # When principal angle is in degrees
        if principal_angle < 90:  # Quadrant 1
            return principal_angle
        elif principal_angle > 90 and principal_angle < 180:  # Quadrant 2
            return 180 - principal_angle
        elif principal_angle > 180 and principal_angle < 270:
            return principal_angle - 180
        else:  # Quadrant 4
            return 360 - principal_angle


###############################################################################
# Question Functions
###############################################################################

# TODO: Trig indetities from text file

# TODO: given some random radian find the exact value of sinx or tanx or cosx or cscx secx cotx

# TODO: Convert degree to radian and vice versa

# TODO: Arc, angular velocity solving questions

# TODO: Solving related acute angle from diagram

# TODO: Genrate a equation of a combination of random trig functions and simplfy it in exact values

# TODO: Trig word problem, kite flying or ladder leaning on wall, or some other scenario that requires someone to look
# for the distance or heieght etc
# for the distance or heieght etc. Function just need to change the numbers and scenario.


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)  # Forcing verbose to be true will provide full details of doctests
