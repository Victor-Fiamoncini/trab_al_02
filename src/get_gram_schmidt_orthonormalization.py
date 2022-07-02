from typing import List, TypeVar

from get_orthogonal_projection import get_orthogonal_projection

NumberInsideList = TypeVar('NumberInsideList', int, float)

Vector = List[NumberInsideList]
VectorBase = List[List[NumberInsideList]]

def get_gram_schmidt_orthonormalization(base: VectorBase) -> VectorBase:
    x1 = base[0]
    base.pop(0)

    xs = [x1]
    orthonormalizated_base = [x1]

    for base_index in range(len(base)):
        current_v = base[base_index]
        new_x = []

        count = 0
        projections_accumulator = []

        while count != len(xs):
            current_x = xs[count]
            current_projection = get_orthogonal_projection(current_v, current_x)

            if count == 0:
                projections_accumulator = current_projection
            else:
                projections_accumulator = sum_vectors(projections_accumulator, current_projection)

            count += 1

        new_x = subtract_vectors(current_v, projections_accumulator)

        xs.append(new_x)

    return orthonormalizated_base

def subtract_vectors(vector_a: Vector, vector_b: Vector) -> Vector:
    subtracted_vector = []

    for index in range(len(vector_a)):
        subtracted_vector.append(vector_a[index] - vector_b[index])

    return subtracted_vector

def sum_vectors(vector_a: Vector, vector_b: Vector) -> Vector:
    summed_vector = []

    for index in range(len(vector_a)):
        summed_vector.append(vector_a[index] + vector_b[index])

    return summed_vector
