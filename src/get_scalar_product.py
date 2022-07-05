from custom_types import Number, Vector

'''
Calcula o produto escalar dos dois vetores passados como parâmetro
'''
def get_scalar_product(u: Vector, v: Vector) -> Number:
    if len(u) != len(v):
        raise Exception('Para obter o produto escalar o tamanho dos vetores informados deve ser o mesmo')

    scalar_product = 0

    for index in range(len(u)):
        scalar_product += u[index] * v[index]

    if isinstance(scalar_product, int):
        return scalar_product

    return round(scalar_product, 4)

'''
Verifica se o produto escalar passado como parâmetro é ortogonal
'''
def is_orthogonal_scalar_product(scalar_product: Number) -> bool:
    return True if scalar_product == 0 else False
