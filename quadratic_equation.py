from math import sqrt

# Which version of function is better?
# Which is more correct?
# get_roots() or get_roots_s?


def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        root1 = None
        root2 = None
    elif discriminant == 0:
        root1 = -b / (2 * a)
        root2 = None
    else:
        root1 = (-b - sqrt(discriminant)) / (2 * a)
        root2 = (-b + sqrt(discriminant)) / (2 * a)
    return root1, root2


def get_roots_s(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None, None
    elif discriminant == 0:
        return -b / (2 * a), None
    else:
        root1 = (-b - sqrt(discriminant)) / (2 * a)
        root2 = (-b + sqrt(discriminant)) / (2 * a)
    return root1, root2
