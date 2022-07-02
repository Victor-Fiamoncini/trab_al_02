from typing import List, TypeVar, Union
import math

Number = Union[float, int]

NumberInsideList = TypeVar('NumberInsideList', int, float)

def get_vector_norm(vector: List[NumberInsideList]) -> Number:
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

def get_vector_squared_norm(vector: List[NumberInsideList]) -> Number:
    norm = get_vector_norm(vector)
    squared_norm = norm ** 2

    if isinstance(norm, int):
        return norm

    return round(squared_norm, 4)