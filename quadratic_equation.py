from math import sqrt


def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant == 0:
        root1 = (-b - sqrt(discriminant)) / (2 * a)
        return root1, None
    elif discriminant < 0:
        # При отрицательном дискриминанте тоже корни есть, они просто комплексные
        # (-b - discriminant) / (2 * a), (-b + discriminant) / (2 * a)
        return None, None
    else:
        root1 = (-b - sqrt(discriminant)) / (2 * a)
        root2 = (-b + sqrt(discriminant)) / (2 * a)
        return root1, root2
