def is_valid_triangle(sides):
    a, b, c = sides
    return a > 0 and b > 0 and c > 0 and a + b > c and b + c > a and a + c > b


def equilateral(sides):
    if is_valid_triangle(sides) and sides[0] == sides[1] == sides[2]:
        return True
    return False


def isosceles(sides):
    if is_valid_triangle(sides) and (sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]):
        return True
    return False


def scalene(sides):
    if is_valid_triangle(sides) and sides[0] != sides[1] and sides[1] != sides[2] and sides[0] != sides[2]:
        return True
    return False