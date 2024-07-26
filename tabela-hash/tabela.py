class Estado:
    def _init_(self, sigla, nomeEstado):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.proximo = None

class TabelaHash:
    def _init_(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho

    def hash_function(self, sigla):
        if sigla == 'DF':
            return 7
        else:
            char1_ascii = ord(sigla[0])
            char2_ascii = ord(sigla[1])
            return (char1_ascii + char2_ascii) % self.tamanho

    def inserir(self, estado):
        posicao = self.hash_function(estado.sigla)
        novo_estado = Estado(estado.sigla, estado.nomeEstado)
        if self.tabela[posicao] is None:
            self.tabela[posicao] = novo_estado
        else:
            novo_estado.proximo = self.tabela[posicao]
            self.tabela[posicao] = novo_estado

    def imprimir_tabela(self):
        for i in range(self.tamanho):
            if self.tabela[i] is None:
                print(f"Posição {i}: None")
            else:
                estados_na_posicao = []
                estado_atual = self.tabela[i]
                while estado_atual is not None:
                    estados_na_posicao.append(f"[{estado_atual.sigla} - {estado_atual.nomeEstado}]")
                    estado_atual = estado_atual.proximo
                print(f"Posição {i}: " + " -> ".join(estados_na_posicao))


# criando a tabela hash com 10 posições
tabela_hash = TabelaHash(10)

# imprimindo a tabela hash antes de inserir qualquer informação
print("Saída de console 1:")
tabela_hash.imprimir_tabela()
print()

# inserindo os 26 estados e o Distrito Federal
estados = [
    Estado('AC', 'Acre'), Estado('AL', 'Alagoas'), Estado('AP', 'Amapá'),
    Estado('AM', 'Amazonas'), Estado('BA', 'Bahia'), Estado('CE', 'Ceará'),
    Estado('ES', 'Espírito Santo'), Estado('GO', 'Goiás'), Estado('MA', 'Maranhão'),
    Estado('MT', 'Mato Grosso'), Estado('MS', 'Mato Grosso do Sul'), Estado('MG', 'Minas Gerais'),
    Estado('PA', 'Pará'), Estado('PB', 'Paraíba'), Estado('PR', 'Paraná'),
    Estado('PE', 'Pernambuco'), Estado('PI', 'Piauí'), Estado('RJ', 'Rio de Janeiro'),
    Estado('RN', 'Rio Grande do Norte'), Estado('RS', 'Rio Grande do Sul'), Estado('RO', 'Rondônia'),
    Estado('RR', 'Roraima'), Estado('SC', 'Santa Catarina'), Estado('SP', 'São Paulo'),
    Estado('SE', 'Sergipe'), Estado('TO', 'Tocantins'),
    Estado('DF', 'Distrito Federal')
]

for estado in estados:
    tabela_hash.inserir(estado)

# imprimindo a tabela hash após inserir os 26 estados e o DF
print("Saída de console 2:")
tabela_hash.imprimir_tabela()
print()

# inserindo o estado fictício
estado_ficticio = Estado('LV', 'Larissa Vieira')
tabela_hash.inserir(estado_ficticio)

# imprimindo a tabela hash após inserir o estado fictício
print("Saída de console 3:")
tabela_hash.imprimir_tabela()