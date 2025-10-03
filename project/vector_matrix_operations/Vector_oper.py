import math


def scalar_product(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors should have same length")

    return sum(v1[i] * v2[i] for i in range(len(v1)))


def vector_length(v1):
    return sum(v1[i] ** 2 for i in range(len(v1))) ** 0.5


def angle_between_vectors(v1, v2, form="r"):
    if form == "r":
        return math.acos(scalar_product(v1, v2) / vector_length(v1) / vector_length(v2))
    elif form == "d":
        return angle_between_vectors(v1, v2) * 180 / math.pi
    else:
        raise SyntaxError('angle_between_vectors(v1, v2, form=["r" / "d"])')
