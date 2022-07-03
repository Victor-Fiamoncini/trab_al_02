from typing import List, TypeVar, Union

from get_vector_norm import get_vector_squared_norm

NumberInsideList = TypeVar('NumberInsideList', int, float)
Vector = List[NumberInsideList]

def get_orthogonal_projection(u: Vector, v: Vector) -> Vector:
    if len(u) != len(v):
        raise Exception('Para obter a projeção ortogonal o tamanho dos vetores informados deve ser o mesmo')

    vectors_size = len(u)
    distributive_value = 0

    for index in range(vectors_size):
        distributive_value += u[index] * v[index]

    v_squared_norm = get_vector_squared_norm(v)
    norm_distributive_scalar_fraction = distributive_value / v_squared_norm

    ortogonal_projection = []

    for index in range(vectors_size):
        orthogonal_value = norm_distributive_scalar_fraction * v[index]

        if isinstance(orthogonal_value, int):
            ortogonal_projection.append(orthogonal_value)
        else:
            ortogonal_projection.append(round(orthogonal_value, 4))

    return ortogonal_projection

