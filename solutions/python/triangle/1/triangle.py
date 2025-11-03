def is_valid_triangle(sides):
    # Check if all sides are greater than 0 and triangle inequality holds
    a, b, c = sides
    return a > 0 and b > 0 and c > 0 and a + b > c and b + c > a and a + c > b


def equilateral(sides):
    # Check if all sides are equal and valid triangle
    if is_valid_triangle(sides) and sides[0] == sides[1] == sides[2]:
        return True
    return False


def isosceles(sides):
    # Check if at least two sides are equal and valid triangle
    if is_valid_triangle(sides) and (sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]):
        return True
    return False


def scalene(sides):
    # Check if all sides are different and valid triangle
    if is_valid_triangle(sides) and sides[0] != sides[1] and sides[1] != sides[2] and sides[0] != sides[2]:
        return True
    return False