# Implementação de Tabela Hash para Estados Brasileiros

Este é um projeto fictício de uma implementação simples de uma Tabela Hash para armazenar e gerenciar informações sobre os estados brasileiros e o Distrito Federal, através do emplacamento de veículos. O último número da placa representará seu respectivo estado.

## Descrição

O código define duas classes:

- `Estado`: Representa um estado brasileiro com uma sigla e um nome.
- `TabelaHash`: Implementa uma tabela hash para armazenar e buscar estados utilizando a sigla como chave.

A tabela hash é implementada com uma função de hash básica e trata colisões usando encadeamento.

## Estrutura do Código

### Classe `Estado`

A classe `Estado` possui os seguintes atributos:
- `sigla`: A sigla do estado (ex: 'AC' para Acre).
- `nomeEstado`: O nome completo do estado.
- `proximo`: Referência para o próximo estado em caso de colisão na tabela hash.

#### Métodos:
- `__init__(self, sigla, nomeEstado)`: Inicializa um novo objeto `Estado`.

### Classe `TabelaHash`

A classe `TabelaHash` possui os seguintes atributos:
- `tamanho`: O número de posições na tabela hash.
- `tabela`: Lista que armazena os estados.

#### Métodos:
- `__init__(self, tamanho)`: Inicializa a tabela hash com o tamanho especificado.
- `hash_function(self, sigla)`: Função de hash que calcula a posição na tabela com base na sigla do estado.
- `inserir(self, estado)`: Insere um estado na tabela hash.
- `imprimir_tabela(self)`: Imprime o conteúdo da tabela hash.

## Como Usar

1. Clone o repositório ou copie o código para seu ambiente de desenvolvimento.
2. Execute o código para ver a tabela hash em ação.

# Sistema de Fila de Pacientes com Lista Encadeada

Este é um projeto fictício de uma implementação de um sistema de fila para pacientes utilizando uma Lista encadeada. O sistema categoriza pacientes com base na cor do cartão e prioriza o atendimento conforme a cor do cartão.

## Descrição

O código define duas classes principais:

- `Nodo`: Representa um paciente com um número de cartão e uma cor de cartão.
- `ListaEncadeada`: Gerencia a fila de pacientes, permitindo inserção com ou sem prioridade, e fornece funcionalidades para exibir e atender pacientes.

### Classe `Nodo`

A classe `Nodo` possui os seguintes atributos:
- `numero`: Número do cartão do paciente.
- `cor`: Cor do cartão do paciente (Amarelo ou Verde).
- `proximo`: Referência para o próximo `Nodo` na lista encadeada.

#### Métodos:
- `__init__(self, numero, cor)`: Inicializa um novo objeto `Nodo` com o número e a cor do cartão.

### Classe `ListaEncadeada`

A classe `ListaEncadeada` gerencia a fila de pacientes com os seguintes métodos:

#### Métodos:
- `__init__(self)`: Inicializa a lista encadeada com a cabeça vazia.
- `inserirSemPrioridade(self, nodo)`: Insere um novo `Nodo` no final da lista quando a cor do cartão é verde.
- `inserirComPrioridade(self, nodo)`: Insere um novo `Nodo` na lista com prioridade quando a cor do cartão é amarelo. Pacientes com cartões amarelos são priorizados sobre os verdes.
- `inserir(self)`: Solicita ao usuário o número e a cor do cartão e insere o `Nodo` na lista conforme a cor do cartão.
- `imprimirListaEspera(self)`: Imprime todos os pacientes na fila, mostrando a cor e o número do cartão.
- `atenderPaciente(self)`: Atende o próximo paciente na fila (o paciente no início da lista).

## Como Usar

1. Clone o repositório ou copie o código para seu ambiente de desenvolvimento.
2. Execute o código Python para iniciar o menu do sistema.

### Exemplo de Uso

Ao executar o código, um menu será exibido com as seguintes opções:

1. **Adicionar paciente à fila**: Insira o número e a cor do cartão do paciente.
2. **Mostrar pacientes na fila**: Exiba todos os pacientes na fila de espera.
3. **Chamar próximo paciente**: Atenda o próximo paciente na fila.
4. **Sair**: Encerre o programa.


