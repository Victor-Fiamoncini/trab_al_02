from get_gram_schmidt_orthonormalization import get_gram_schmidt_orthonormalization

first_vector_base = [[1, 1, 1], [0, 1, 1], [0, 0, 1]]

def test_should_get_correct_gram_schmidt_orthonormalizations():
    first_orthonormalization = get_gram_schmidt_orthonormalization(first_vector_base)

    assert(first_orthonormalization) == 1
