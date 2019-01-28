
import requests
import json
import sys

# CLOUD_URL = 'http://127.0.0.1:5000/'
CLOUD_URL = 'https://cloud-broker.herokuapp.com/'
PROV_URL = 'http://127.0.0.1:5000/'

class Provedor:
    def __init__(self):
        self.quantidade = 0
        self.recurso = {}

    def menu(self):
        while True:
            print '1. Divulgar recursos'
            print '2. Sair'
            opc = input('')

            if opc == 1:
                response = self.divulgar()

                if response['Ok'] == True:
                    print '\n--> Recurso divulgado com sucesso.\n'
                else:
                    print '\n--> Erro ao divulgar recurso.\n'
            if opc == 2:
                return 0

    def divulgar(self):
        pid = input('Informe o seu id: ')
        recursos = {
            'vcpu':'',
            'ram':'',
            'hd':'',
            'preco':''
        }
        recursos['vcpu'] = str(input('Quantidade de vCPUs: '))
        recursos['ram'] = str(input('Quantidade de memoria RAM (em GB): '))
        recursos['hd'] = str(input('Quantidade de disco (HD, em GB): '))
        recursos['preco'] = str(input('Preco do recurso (em R$): '))
    
        return self.postRequest(recursos, PROV_URL + 'provedor/cadastrar/' + str(pid))

    def postRequest(self, data, url):
        headers = {'Content-Type': 'application/json',}
        post = requests.post(url=url, data=json.dumps(data), headers=headers)

        return post.json()

if __name__ == '__main__':
    p = Provedor()
    p.menu()