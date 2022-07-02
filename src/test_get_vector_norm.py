from get_vector_norm import get_vector_norm

def test_should_get_correct_vectors_norms():
    first_vector = [-2/3, 1/3, 1/3]
    second_vector = [1, 1, 1]
    third_vector = [2, 2, 2]
    fourth_vector = [1, 2]

    first_norm = get_vector_norm(first_vector)
    second_norm = get_vector_norm(second_vector)
    third_norm = get_vector_norm(third_vector)
    fourth_norm = get_vector_norm(fourth_vector)

    assert(first_norm) == 0.8165
    assert(second_norm) == 1.7321
    assert(third_norm) == 3.4641
    assert(fourth_norm) == 2.2361

