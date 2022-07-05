from custom_types import Number, VectorBase
from get_scalar_product import get_scalar_product, is_orthogonal_scalar_product

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
    pass

'''
Opção do menu para chamar o cálculo da projeção ortogonal
'''
def orthogonal_projection_option(vectors: VectorBase) -> None:
    pass

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
            print('U =', ' '.join(map(str, u_vector)))
            print('V =', ' '.join(map(str, v_vector)))
            print('W =', ' '.join(map(str, w_vector)))
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
