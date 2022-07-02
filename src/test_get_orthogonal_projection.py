from get_orthogonal_projection import get_orthogonal_projection

first_vector_u = [1, 2, 3]
first_vector_v = [-1, 2, 0]

second_vector_u = [0, 1, 1]
second_vector_v = [1, 1, 1]

third_vector_u = [3, -8]
third_vector_v = [1, 2]

fourth_vector_u = [0, 0, 1]
fourth_vector_v = [-2/3, 1/3, 1/3]

def test_should_get_correct_orthogonal_projections():
    first_orthogonal_projection = get_orthogonal_projection(first_vector_u, first_vector_v)
    second_orthogonal_projection = get_orthogonal_projection(second_vector_u, second_vector_v)
    third_orthogonal_projection = get_orthogonal_projection(third_vector_u, third_vector_v)
    fourth_orthogonal_projection = get_orthogonal_projection(fourth_vector_u, fourth_vector_v)

    assert(first_orthogonal_projection) == [-0.6, 1.2, 0]
    assert(second_orthogonal_projection) == [0.6666, 0.6666, 0.6666]
    assert(third_orthogonal_projection) == [-2.5999, -5.1999]
    assert(fourth_orthogonal_projection) == [-0.3333, 0.1667, 0.1667]
