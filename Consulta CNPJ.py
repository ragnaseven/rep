import requests

def main():
    print('####################')
    print('### Consulta CNPJ ###')
    print('####################\n')

    input_cnpj = input('Digite seu CNPJ: ')

#Gera erro caso a quantidade de digitos seja diferente de 14
    if len(input_cnpj) != 14:
        print('quantidade de digitos invalida\n')
        main()

#Utiliza a biblioteca da receita para realizar a busca
    request = requests.get('https://www.receitaws.com.br/v1/cnpj/{}'.format(input_cnpj))
    address_data = request.json()

#Caso não exista erro na pesquisa, seram retornados os dados referentes ao cnpj
    if 'CNPJ inválido' not in address_data:
        print('**CNPJ encontrado**')
        print('CNPJ: {}'.format(address_data['cnpj']))
        print('Razão social: {}'.format(address_data['nome']))
        print('Status: {}'.format(address_data['status']))
        print('Tipo: {}'.format(address_data['tipo']))
        print('Abertura: {}'.format(address_data['abertura']))
        print('Atividade principal: {}'.format(address_data['atividade_principal']))
        print('CEP: {}'.format(address_data['cep']))
        print('Bairro: {}'.format(address_data['bairro']))
        print('Municipio: {}'.format(address_data['municipio']))
#Caso o cnpj esteja errado retornara "CNPJ INVÁLIDO
    else:
        print('CNPJ INVáLIDO')

#Ao terminar a consulta sera perguntado se você deseja realizar outra
    option = int(input('Deseja realizar uma nova consulta? \n1. Sim \n2. Não \n'))
    if option == 1:
        main()
    else:
        print("**Saindo**")
        exit()

if __name__ == '__main__':
    main()
