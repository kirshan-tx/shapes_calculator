from math import pi

def circle(radius: float) -> float:
    """
    This function takes the radius of the circle and returns the perimeter.

    :param radius: Radius of the circle
    :return: Perimeter of the circle
    """

    return 2 * pi * radius

def rectangle(base: float, height: float) -> float:
    """
    This function takes the base and height of the rectangle and returns the perimeter.

    :param base: Base of the rectangle
    :param height: Height of the rectangle
    :return: Perimeter of the rectangle
    """

    return 2 * (base + height)

def triangle(side1: float, side2: float, side3: float) -> float:
    """
    This function takes the three sides of the triangle and returns the perimeter.

    :param side1: First side of the triangle
    :param side2: Second side of the triangle
    :param side3: Third side of the triangle
    :return: Perimeter of the triangle
    """
    return side1 + side2 + side3