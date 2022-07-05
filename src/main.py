from custom_types import Number, Vector, VectorBase
from get_orthogonal_projection import get_orthogonal_projection
from get_scalar_product import get_scalar_product, is_orthogonal_scalar_product
from get_vector_norm import get_vector_norm, is_unitary_vector

'''
Opção do menu para chamar o cálculo do produto escalar
'''
def scalar_product_option(vectors: VectorBase) -> None:
    u_vector = vectors[0]
    v_vector = vectors[1]
    w_vector = vectors[2]

    scalar_product_u_v = get_scalar_product(u_vector, v_vector)
    scalar_product_v_w = get_scalar_product(v_vector, w_vector)
    scalar_product_u_w = get_scalar_product(u_vector, w_vector)

    is_scalar_product_u_v_orthogonal = 'Sim' if is_orthogonal_scalar_product(scalar_product_u_v) else 'Não'
    is_scalar_product_v_w_orthogonal = 'Sim' if is_orthogonal_scalar_product(scalar_product_v_w) else 'Não'
    is_scalar_product_u_w_orthogonal = 'Sim' if is_orthogonal_scalar_product(scalar_product_u_w) else 'Não'

    print('---------------------------------------------------------------')
    print(f'Produto escalar de U por V: {scalar_product_u_v}, é ortogonal: {is_scalar_product_u_v_orthogonal}')
    print(f'Produto escalar de V por W: {scalar_product_v_w}, é ortogonal: {is_scalar_product_v_w_orthogonal}')
    print(f'Produto escalar de U por W: {scalar_product_u_w}, é ortogonal: {is_scalar_product_u_w_orthogonal}')
    print('---------------------------------------------------------------')

'''
Opção do menu para chamar o cálculo da norma
'''
def norm_option(vectors: VectorBase) -> None:
    u_vector = vectors[0]
    v_vector = vectors[1]
    w_vector = vectors[2]

    u_norm = get_vector_norm(u_vector)
    v_norm = get_vector_norm(v_vector)
    w_norm = get_vector_norm(w_vector)

    is_u_vector_unitary = 'Sim' if is_unitary_vector(u_norm) else 'Não'
    is_v_vector_unitary = 'Sim' if is_unitary_vector(v_norm) else 'Não'
    is_w_vector_unitary = 'Sim' if is_unitary_vector(w_norm) else 'Não'

    print('---------------------------------------------------------------')
    print(f'A norma de U é: {u_norm}, é um vetor unitário: {is_u_vector_unitary}')
    print(f'A norma de V é: {v_norm}, é um vetor unitário: {is_v_vector_unitary}')
    print(f'A norma de W é: {w_norm}, é um vetor unitário: {is_w_vector_unitary}')
    print('---------------------------------------------------------------')

'''
Opção do menu para chamar o cálculo da projeção ortogonal
'''
def orthogonal_projection_option(vectors: VectorBase) -> None:
    u_vector = vectors[0]
    v_vector = vectors[1]
    w_vector = vectors[2]

    projection_v_u = get_orthogonal_projection(v_vector, u_vector)
    projection_w_u = get_orthogonal_projection(w_vector, u_vector)
    projection_w_v = get_orthogonal_projection(w_vector, v_vector)

    print('---------------------------------------------------------------')
    print(f'Projeção ortogonal de V em U: {humanize_vector(projection_v_u)}')
    print(f'Projeção ortogonal de W em U: {humanize_vector(projection_w_u)}')
    print(f'Projeção ortogonal de W em V: {humanize_vector(projection_w_v)}')
    print('---------------------------------------------------------------')

'''
Opção do menu para chamar o função de ortonormalização de Gram-Schmidt
'''
def gram_schmidt_orthonormalization(vectors: VectorBase) -> None:
    pass

'''
Opção do menu encerrar a CLI
'''
def exit_option(_) -> None:
    print('CLI finalizada, até breve :)')
    exit()

'''
Converte string vinda do stdin para Number
'''
def string_to_number(value: str) -> Number:
    try:
        return float(value)
    except ValueError:
        num, denom = value.split('/')

        try:
            leading, num = num.split(' ')
            whole = float(leading)
        except ValueError:
            whole = 0

        frac = float(num) / float(denom)
        return whole - frac if whole < 0 else whole + frac

'''
Formata o vetor passado como parâmetro para ser legível no stdout
'''
def humanize_vector(vector: Vector) -> str:
    return ' '.join(map(str, vector))

'''
Inicia a CLI exibindo o menu principal no stdout
'''
def main() -> None:
    cli_options = {
        1: scalar_product_option,
        2: norm_option,
        3: orthogonal_projection_option,
        4: gram_schmidt_orthonormalization,
        5: exit_option
    }

    u_vector = []
    v_vector = []
    w_vector = []

    try:
        print('-------------------- Criação dos vetores ----------------------')
        print('Informe valores inteiros ou em formato fracionário, exemplo: 2/6')

        for index in range(3):
            value = string_to_number(input(f'Informe o {index + 1}º valor do vetor U: '))
            u_vector.append(value if value != 0 else 0)

        for index in range(3):
            value = string_to_number(input(f'Informe o {index + 1}º valor do vetor V: '))
            v_vector.append(value if value != 0 else 0)

        for index in range(3):
            value = string_to_number(input(f'Informe o {index + 1}º valor do vetor W: '))
            w_vector.append(value if value != 0 else 0)

        vectors = [u_vector, v_vector, w_vector]

        while True:
            print('----------------------- Menu Principal ------------------------')
            print('Abaixo segue seus vetores informados:')
            print('U =', humanize_vector(u_vector))
            print('V =', humanize_vector(v_vector))
            print('W =', humanize_vector(w_vector))
            print('---------------------------------------------------------------')
            print('O que deseja fazer com eles?')
            print('1 - Calcular produto escalar')
            print('2 - Calcular a norma')
            print('3 - Calcular a projeção ortogonal')
            print('4 - Calcular a ortonormalização de Gram-schmidt')
            print('5 - Sair')
            print('---------------------------------------------------------------')

            selected_option = int(input('Digite o número da opção desejada: '))

            if selected_option in cli_options:
                cli_options[selected_option](vectors)
            else:
                print('Opção inválida')
    except Exception as ex:
        print(f'CLI finalizada :(, ocorreu o seguinte erro: {ex}')

'''
Chamada da função main
'''
if __name__ == '__main__':
    main()
