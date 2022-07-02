from get_vector_norm import get_vector_norm, get_vector_squared_norm

first_vector = [-2/3, 1/3, 1/3]
second_vector = [1, 1, 1]
third_vector = [2, 2, 2]
fourth_vector = [1, 2]
fifth_vector = [1/4, 2, 1, 2/3]

def test_should_get_correct_vectors_norms():
    first_norm = get_vector_norm(first_vector)
    second_norm = get_vector_norm(second_vector)
    third_norm = get_vector_norm(third_vector)
    fourth_norm = get_vector_norm(fourth_vector)
    fifth_norm = get_vector_norm(fifth_vector)

    assert(first_norm) == 0.8165
    assert(second_norm) == 1.7321
    assert(third_norm) == 3.4641
    assert(fourth_norm) == 2.2361
    assert(fifth_norm) == 2.3467

def test_should_get_correct_vectors_squared_norms():
    first_squared_norm = get_vector_squared_norm(first_vector)
    second_squared_norm = get_vector_squared_norm(second_vector)
    third_squared_norm = get_vector_squared_norm(third_vector)
    fourth_squared_norm = get_vector_squared_norm(fourth_vector)
    fifth_squared_norm = get_vector_squared_norm(fifth_vector)

    assert(first_squared_norm) == 0.6667
    assert(second_squared_norm) == 3.0002
    assert(third_squared_norm) == 12
    assert(fourth_squared_norm) == 5.0001
    assert(fifth_squared_norm) == 5.507

