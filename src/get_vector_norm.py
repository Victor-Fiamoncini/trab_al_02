import math

from custom_types import Number, Vector

def get_vector_norm(vector: Vector) -> Number:
    squared_vector = []

    for index in range(len(vector)):
        squared_vector.append(vector[index] ** 2)

    sumed_squared_vector_values = 0
    index = 0

    while index < len(squared_vector):
        sumed_squared_vector_values += squared_vector[index]
        index += 1

    norm = math.sqrt(sumed_squared_vector_values)

    if isinstance(norm, int):
        return norm

    return round(norm, 4)

def get_vector_squared_norm(vector: Vector) -> Number:
    norm = get_vector_norm(vector)
    squared_norm = norm ** 2

    if isinstance(norm, int):
        return norm

    return round(squared_norm, 4)
