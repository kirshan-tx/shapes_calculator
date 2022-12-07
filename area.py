from math import pi

def circle(radius: float) -> float:
    """
    This function takes the radius of the circle and returns the area.

    :param radius: Radius of the circle
    :return: Area of the circle
    """

    return pi * (radius ** 2)

def rectangle(base: float, height: float) -> float:
    """
    This function takes the base and height of the rectangle and returns the area.

    :param base: Base of the rectangle
    :param height: Height of the rectangle
    :return: Area of the rectangle
    """
    
    return base * height

def triangle(base: float, height: float) -> float:
    """
    This function takes the base and height of the triangle and returns the area.

    :param base: Base of the triangle
    :param height: Height of the triangle
    :return: Area of the triangle
    """
    return 0.5 * base * height
    