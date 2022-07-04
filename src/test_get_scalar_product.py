from get_scalar_product import get_scalar_product

first_vector_u = [1, 4, -3]
first_vector_v = [-1, 2, 0]

second_vector_u = [7, 3, 5]
second_vector_v = [-8, 4, 2]

def test_should_get_correct_scalar_products():
    first_scalar_product = get_scalar_product(first_vector_u, first_vector_v)
    second_scalar_product = get_scalar_product(second_vector_u, second_vector_v)

    assert(first_scalar_product) == 7
    assert(second_scalar_product) == -34
