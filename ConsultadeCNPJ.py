import requests
import PySimpleGUI as sg

class TelaConsulta:
    def __init__(self):
        #layout da tela
        layout = [
            [sg.Text('CNPJ',size=(14,0)),sg.Input(size=(14,0),key='cnpj')],
            [sg.Button('Consultar os dados')],
            [sg.Output(size=(60,20), key='output')]

        ]

        #janela
        self.janela = sg.Window("Consulta de CNPJ").layout(layout)

    def Iniciar(self):
        while True:

            # extrair os dados da tela
            self.Button, self.values = self.janela.Read()
            cnpj = self.values['cnpj']

            # Biblioteca para consulta do cnpj
            request = requests.get('https://www.receitaws.com.br/v1/cnpj/{}'.format(cnpj))
            address_data = request.json()

            # Caso o cnpj digitado não tenha o padrão de 14 digitos retorna uma msg de erro
            if len(cnpj) != 14:
                print('Quantidade de digitos inválida\n')
                tela.Iniciar()

            print('Razão social: {}'.format(address_data['nome']))
            print('Status: {}'.format(address_data['status']))
            print('Tipo: {}'.format(address_data['tipo']))
            print('Abertura: {}'.format(address_data['abertura']))
            print('CEP: {}'.format(address_data['cep']))
            print('Bairro: {}'.format(address_data['bairro']))
            print('Municipio: {}'.format(address_data['municipio']))
            print()

tela = TelaConsulta()
tela.Iniciar()
