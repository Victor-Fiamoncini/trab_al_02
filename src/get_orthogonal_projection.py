from typing import List, TypeVar, Union

from get_vector_norm import get_vector_squared_norm

Number = Union[float, int]

NumberInsideList = TypeVar('NumberInsideList', int, float)

def get_orthogonal_projection(u: List[NumberInsideList], v: List[NumberInsideList]) -> List[NumberInsideList]:
    if len(u) != len(v):
        raise Exception('Para obter a projeção ortogonal o tamanho dos vetores informados deve ser o mesmo')

    vectors_size = len(u)
    distributive_value = 0

    for index in range(vectors_size):
        distributive_value += u[index] * v[index]

    v_squared_norm = get_vector_squared_norm(v)
    norm_distributive_scalar_fraction = distributive_value / v_squared_norm

    first_orthogonal_part = []

    for index in range(vectors_size):
        first_orthogonal_part.append(norm_distributive_scalar_fraction * v[index])

    final_orthogonal_part = []

    for index in range(vectors_size):
        index_projection_value = u[index] - first_orthogonal_part[index]

        if isinstance(index_projection_value, int):
            final_orthogonal_part.append(index_projection_value)
        else:
            final_orthogonal_part.append(round(index_projection_value, 4))

    return final_orthogonal_part
