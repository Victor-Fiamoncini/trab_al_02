from math import sqrt

from get_gram_schmidt_orthonormalization import get_gram_schmidt_orthonormalization, is_orthonormal_base

first_vector_base = [[1, 1, 1], [0, 1, 1], [0, 0, 1]]
second_vector_base = [[1, 0], [1, 1]]
third_vector_base = [[2, 0], [1, 1], [0, 1]]
fourth_vector_base = [[3, 4], [4, 4]]
fifth_vector_base = [[1, 0, 0], [1, 2, 0], [0, 2, 2]]

first_orthonormal_vector_base = [[1, 0, 0], [0, 1/sqrt(2), 1/sqrt(2)], [0, 1/sqrt(2), -1/sqrt(2)]]

def test_should_get_correct_gram_schmidt_orthonormalizations():
    first_orthonormalization = get_gram_schmidt_orthonormalization(first_vector_base)
    second_orthonormalization = get_gram_schmidt_orthonormalization(second_vector_base)
    third_orthonormalization = get_gram_schmidt_orthonormalization(third_vector_base)
    fourth_orthonormalization = get_gram_schmidt_orthonormalization(fourth_vector_base)
    fifth_orthonormalization = get_gram_schmidt_orthonormalization(fifth_vector_base)

    assert(first_orthonormalization) == [[0.5773, 0.5773, 0.5773], [-0.8164, 0.4083, 0.4083], [0, -0.7071, 0.7071]]
    assert(second_orthonormalization) == [[1, 0], [0, 1]]
    assert(third_orthonormalization) == [[1, 0], [0, 1]]
    assert(fourth_orthonormalization) == [[0.6, 0.8], [0.8, -0.6]]
    assert(fifth_orthonormalization) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

def test_should_verify_if_bases_are_orthonormal():
    first_orthonormal_verification = is_orthonormal_base(first_vector_base)
    second_orthonormal_verification = is_orthonormal_base(second_vector_base)
    third_orthonormal_verification = is_orthonormal_base(third_vector_base)
    fourth_orthonormal_verification = is_orthonormal_base(get_gram_schmidt_orthonormalization(fourth_vector_base))
    fifth_orthonormal_verification = is_orthonormal_base(fifth_vector_base)
    sixth_orthonormal_verification = is_orthonormal_base(first_orthonormal_vector_base)

    assert(False) == first_orthonormal_verification
    assert(False) == second_orthonormal_verification
    assert(False) == third_orthonormal_verification
    assert(True) == fourth_orthonormal_verification
    assert(False) == fifth_orthonormal_verification
    assert(True) == sixth_orthonormal_verification
