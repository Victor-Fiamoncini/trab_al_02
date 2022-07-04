from custom_types import VectorBase

'''
Opção do menu para chamar o cálculo do produto escalar
'''
def scalar_product_option(vectors: VectorBase) -> None:
    pass

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
def exit_option() -> None:
    print('CLI finalizada, até breve :)')
    exit()

cli_options = {
    1: scalar_product_option,
    2: norm_option,
    3: orthogonal_projection_option,
    4: gram_schmidt_orthonormalization,
    5: exit_option
}

'''
Inicia a CLI exibindo o menu principal no stdout
'''
def main() -> None:
    u_vector = []
    v_vector = []
    w_vector = []

    try:
        print('---------------------------------------------------------------')

        for index in range(3):
            value = float(input(f'Informe o {index + 1}º valor do vetor U: '))
            u_vector.append(value if value > 0 else 0)

        for index in range(3):
            value = float(input(f'Informe o {index + 1}º valor do vetor V: '))
            v_vector.append(value if value > 0 else 0)

        for index in range(3):
            value = float(input(f'Informe o {index + 1}º valor do vetor W: '))
            w_vector.append(value if value > 0 else 0)

        vectors = [u_vector, v_vector, w_vector]

        while True:
            print('---------------------------------------------------------------')
            print('Abaixo segue seus vetores informados:')
            print('U =', ' '.join(map(str, u_vector)))
            print('V =', ' '.join(map(str, v_vector)))
            print('W =', ' '.join(map(str, w_vector)))
            print('---------------------------------------------------------------')
            print('O que deseja fazer com eles?')
            print('1 - Calcular produto escalar')
            print('2 - Calcular a norma')
            print('3 - Calcular a projeção ortogonal')
            print('4 - Calcular a ortonormalização de Gram-schmidt')
            print('5 - Sair')
            print('---------------------------------------------------------------')

            selected_option = int(input('Digite o número da opção desejada: '))

            if selected_option in cli_options:
                cli_options[selected_option](vectors)
            else:
                print('Opção inválida')
    except Exception as ex:
        print(f'CLI finalizada, ocorreu o seguinte erro: {ex}')

'''
Chamada da função main
'''
if __name__ == '__main__':
    main()
