"""
rm 550241- Gustavo Akio 
rm 99275 - Breno Silva
rm 99586 - Vitor da Silva
rm 99404 - Thiago Garcia
rm 98667 - Victor Wittner
"""
import sys
import datetime

x = datetime.datetime.now()
dia = x.day
mes = x.month
ano = x.year
hora = x.hour
minutos = x.minute


def ponti():
    print('.' * 33)


def cnpj():
    print('Antes de tudo, nos informe seu CNPJ')
    cnpj = int(input(':'))
    a = str(cnpj)
    if len(a) != 14:
        print('CNPJ inválido, cancelando operação...')
        sys.exit()


ponti()
print("Seja bem-vindo á Vinheria Agnello ")
ponti()
print("1- Estoque\n"
      "2- Visualizar processos anteriores\n"
      "3- Iniciar novo processo\n"
      "4- Checar completude de processo")
ponti()
opcao = input("Selecione a opção desejada:")

# definindo uma função para o estoque, para deixar o código if mais limpo e de fácil entendimento
Estoque = {
    'Vinho 1': 2500,
    'Vinho 2': 2,
    'Vinho 3': 100,
    'Vinho 4': 150,
    'Vinho 5': 120000
}


def addOrRemove():
    which = input('Você deseja adicionar ou remover algum produto?').capitalize()
    match which:

        case 'Adicionar':
            whichAdd = input('Qual produto você deseja adicionar?').capitalize()
            qtdAdd = int(input('Qual é a quantidade desse produto?'))
            Estoque[whichAdd] = qtdAdd

            print(f'"{whichAdd}" adicionado com sucesso!')
            arquivo = open('material adicionado.txt', 'a')
            arquivo1 = open('materiais adicionados e removidos.txt', 'a')
            arquivo.write(
                f'\n{dia}/{mes}/{ano} --- {hora}:{minutos} -- "{whichAdd}({qtdAdd} itens)" adicionado ao estoque.')
            arquivo1.write(
                f'\n{dia}/{mes}/{ano} --- {hora}:{minutos} -- "{whichAdd}({qtdAdd} itens)" adicionado ao estoque.')

            for i, j in Estoque.items():
                print(f'Produto: {i} -- Quantidade: {j}')
                ponti()

            arquivo.close()
            arquivo1.close()
            sys.exit()

        case 'Remover':
            whichRem = input('Qual produto você deseja remover?').capitalize()
            qtdRem = int(input('Qual é a quantidade a ser removida?'))
            if whichRem in Estoque:
                if qtdRem >= Estoque[whichRem]:
                    ponti()
                    print('Quantidade a ser removida maior ou igual que a em estoque, removendo o material inteiro...')
                    del Estoque[whichRem]
                    ponti()
                else:
                    Estoque[whichRem] -= qtdRem
            else:
                ponti()
                print(f'"{whichRem}" não encontrado no estoque')
                sys.exit()
            for i, j in Estoque.items():
                print(f'Produto: {i} - Quantidade: {j}')
                ponti()
            print(f'"{whichRem}" removido com sucesso!')
            arquivo = open('material removido.txt', 'a')
            arquivo1 = open('materiais adicionados e removidos.txt', 'a')
            arquivo.write(f'\n{dia}/{mes}/{ano} --- {hora}:{minutos} -- "{whichRem}" ({qtdRem} itens) removido(s) do estoque.')
            arquivo1.write(f'\n{dia}/{mes}/{ano} --- {hora}:{minutos} -- "{whichRem}" ({qtdRem} itens) removido(s) do estoque.')
            arquivo.close()
            sys.exit()

        case _:
            print('Opção inválida')
            addOrRemove()

    return addOrRemove()

def checkProcesses():
    while True:
        whichCheck = input('Você deseja acessar os itens removidos, adicionados ou ambos?').capitalize()
        ponti()
        match whichCheck:
            case 'Adicionados':
                arquivoR = open('material adicionado.txt', 'r')
                print(arquivoR.read())
                ponti()
                sys.exit()
            case 'Adicionado':
                arquivoR = open('material adicionado.txt', 'r')
                print(arquivoR.read())
                sys.exit()
            case 'Removidos':
                arquivoR = open('material removido.txt', 'r')
                print(arquivoR.read())
                sys.exit()
            case 'Removido':
                arquivoR = open('material removido.txt', 'r')
                print(arquivoR.read())
                sys.exit()
            case 'Ambos':
                arquivoR = open('materiais adicionados e removidos.txt', 'r')
                print(arquivoR.read())
                sys.exit()
            case _:
                print('Insira um dado válido')

def testProcess():
    print('Olá, seja bem-vindo ao simulador de processos da empresa!')
    ponti()
    dataInicial = int(input('Qual é o dia da data inicial do produto?'))
    dataFinal = int(input('Qual é o dia da data final?'))
    dataAtual = 0
    completudeReal = float(input('Qual foi a completude realizada?'))
    completudePlanejada = float(input('Qual é a completude planejada?'))  # Valor fixo para cada item
    responsavel = input('Qual é o nome do responsável?')
    descricao = input('Qual é a descrição da tarefa?')
    plano = input('Qual é o plano de atraso?')


    class Tarefa:

        def __init__(self, dataInicial, dataFinal, dataAtual, completudeReal,
                     completudePlanejada, responsavel, descricao, plano):
            self.__dataInicial = dataInicial
            self.__dataFinal = dataFinal
            self.__dataAtual = dataAtual
            self.__completudePlanejada = completudePlanejada
            self.completudeReal = completudeReal
            self.responsavel = responsavel
            self.descricao = descricao
            self.__plano = plano

        def exec(self):
            self.__dataAtual = dia
            self.dataFinal = dataFinal
            ponti()
            print(f'Tarefa iniciada em {self.__dataAtual}/{mes}/{ano}')
            ponti()
            print(f'Tarefa programada para conclusão no dia {self.__dataFinal}/{mes}/{ano}')
            ponti()
            if self.__dataAtual > self.dataFinal:
                print('Tarefa em atraso')
                ponti()
                atraso = True
            else:
                atraso = False

            if completudePlanejada > completudeReal and atraso == True:
                ponti()
                print('Completude não suficiente e produto em atraso...Produto cadastrado como "em baixa"')

                ponti()
            elif completudePlanejada > completudeReal and atraso == False:
                print(
                    f'Completude não suficiente...a empresa tem cerca de {self.__dataFinal - dia} dia(s) para completar {completudePlanejada - completudeReal:.1f} de completude')
                ponti()

            arquivo = open('testes de processos.txt.txt', 'a')
            arquivo.write(f'========================== \nData inicial: {dataInicial} \nData final: {dataFinal}  \nData Atual: {dataAtual} \nCompletude real: {completudeReal} \nCompletude planejada: {completudePlanejada}  \nResponsável: {responsavel}  \nDescrição: {descricao} \nPlano de atraso: {plano} \n========================== \n\n\n')
            arquivo.close()

    tarefa = Tarefa(dataInicial, dataFinal, dataAtual, completudeReal, completudePlanejada, responsavel, descricao, plano)
    tarefa.exec()


while True:
    match opcao:
        case '1':
            for i, j in Estoque.items():
                print(f'Produto: {i} -- Quantidade: {j}')
            sys.exit()
        case '2':
            checkProcesses()
            pass
            sys.exit()
        case '3':
            addOrRemove()
            sys.exit()
        case '4':
            testProcess()
            sys.exit()
        case _:
            print('Opção inválida')
            sys.exit()







