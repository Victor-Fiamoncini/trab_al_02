from custom_types import Vector, VectorBase
from get_orthogonal_projection import get_orthogonal_projection
from get_vector_norm import get_vector_norm, is_unitary_vector

'''
Executa a ortonormalização de Gram-Schmidt para a base de vetores passada como parâmetro
Optei por fazer sem usar recursão, pois achei que ficou mais simples de visualizar o procedimento
'''
def get_gram_schmidt_orthonormalization(base: VectorBase) -> VectorBase:
    x1 = base[0]
    xs = [x1]

    base.pop(0)

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

    orthonormalizated_base = []

    for xs_index in range(len(xs)):
        current_x = xs[xs_index]
        current_norm = get_vector_norm(current_x)

        if current_norm == 0:
            continue

        orthonormalizated_base.append([])

        for x_index in range(len(current_x)):
            unit_value = current_x[x_index] / current_norm

            if isinstance(unit_value, int):
                orthonormalizated_base[xs_index].append(unit_value)
            else:
                orthonormalizated_base[xs_index].append(round(unit_value, 4))

    return orthonormalizated_base

'''
Calcula a subtração entre os dois vetores passados como parâmetro
'''
def subtract_vectors(vector_a: Vector, vector_b: Vector) -> Vector:
    subtracted_vector = []

    for index in range(len(vector_a)):
        subtracted_vector.append(vector_a[index] - vector_b[index])

    return subtracted_vector

'''
Calcula a soma entre os dois vetores passados como parâmetro
'''
def sum_vectors(vector_a: Vector, vector_b: Vector) -> Vector:
    summed_vector = []

    for index in range(len(vector_a)):
        summed_vector.append(vector_a[index] + vector_b[index])

    return summed_vector

'''
Verifica se a base de vetores passada como parâmetro é ortonormal
'''
def is_orthonormal_base(base: VectorBase) -> bool:
    base_size = len(base)
    vectors_size = len(base[0])

    intern_products = []

    for base_index in range(base_size - 1):
        intern_product = 0

        for vector_index in range(vectors_size):
            intern_product += base[base_index][vector_index] * base[base_index + 1][vector_index]

        intern_products.append(intern_product)

    all_intern_products_are_zero = all(intern_product == 0 for intern_product in intern_products)

    norms = []

    for index in range(base_size):
        norms.append(get_vector_norm(base[index]))

    all_vectors_are_unitary = all(is_unitary_vector(norm) for norm in norms)

    return all_intern_products_are_zero and all_vectors_are_unitary
