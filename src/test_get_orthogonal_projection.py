from get_orthogonal_projection import get_orthogonal_projection

first_vector_u = [1, 2, 3]
first_vector_v = [-1, 2, 0]

def test_should_get_correct_orthogonal_projection():
    first_orthogonal_projection = get_orthogonal_projection(first_vector_u, first_vector_v)

    assert(first_orthogonal_projection) == [1.6, 0.8, 3]
