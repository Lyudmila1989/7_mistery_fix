from math import sqrt


def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c              # discriminant calculation.
    if discriminant < 0:   # If discriminant < 0 then there are not any roots.
        root1 = None
        root2 = None
    elif discriminant == 0:  # If discriminant = 0 then there's one real root.
        root1 = -b / (2 * a)
        root2 = None
    else:                 # If discriminant > 0 then there are two real roots.
        root1 = (-b - sqrt(discriminant)) / (2 * a)
        root2 = (-b + sqrt(discriminant)) / (2 * a)
    return root1, root2


# Over code version


def get_roots_s(a, b, c):
    discriminant = b ** 2 - 4 * a * c              # discriminant calculation.
    if discriminant < 0:  # If discriminant < 0 then there are not real roots.
        return None, None
    elif discriminant == 0:  # If discriminant = 0 then there's one real root.
        return -b / (2 * a), None
    else:                 # If discriminant > 0 then there are two real roots.
        root1 = (-b - sqrt(discriminant)) / (2 * a)
        root2 = (-b + sqrt(discriminant)) / (2 * a)
    return root1, root2
