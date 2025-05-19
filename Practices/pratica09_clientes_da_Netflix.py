class Cliente():
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_de_planos = ['basic', 'premium']
        if plano in self.lista_de_planos:
            self.plano = plano
        else:
            print('Plano inválido')
    def mudar_de_plano(self, novo_plano):
        if novo_plano in self.lista_de_planos:
            self.plano = novo_plano
        else:
            print(f'O plano é inválido. Não foi possível realizar a troca.')

    def ver_um_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f'Ver o filme {filme}.')
        elif self.plano == 'premium':
            print(f'Ver o filme {filme}.')
        elif self.plano == 'basic':
            print(f'Faça o upgrade para premium para ver esse filme.')
        else:
            print('Plano inválido!')

#Código principal

#Quem é o cliente:
novo_cliente = Cliente('Fernanda', 'fernanda@pyhton.com', 'basic')
print(f'O plano de {novo_cliente.nome} é {novo_cliente.plano}.')

#Qual filme quer ver:
novo_cliente.ver_um_filme('Harry Potter', 'premium')

novo_cliente.mudar_de_plano('premium')
print(f'O seu novo plano é o {novo_cliente.plano}.')

novo_cliente.ver_um_filme('Harry Potter', 'premium')
