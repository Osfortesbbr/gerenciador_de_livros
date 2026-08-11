import os
import csv
os.system ("cls")

estrutura = ['titulo', 'autor', 'ano', 'codigo', 'status']

def cadastrar_livro (titulo,autor,ano,codigo):

    with open ('livros.csv','a',newline='') as cadastro_livro:
        livro = {'titulo':titulo, 'autor':autor, 'ano':ano, 'codigo':codigo, 'status':"Disponivel"}
        escritor = csv.DictWriter(cadastro_livro,fieldnames=estrutura)
        escritor.writerow(livro)
    ## A função faz a criação do livro e manda para a pasta livros.csv, salvando o livro cadastrado em uma lista
    # para uma próxima vez que a pessoa acesar esse codigo novamente

def emprestimo_de_livro (codigo):
    linha = []
    with open ('livros.csv','r',newline='') as arquivo:
        buscar_livro = csv.reader(arquivo)
        for itens in buscar_livro:
            if itens[3] == codigo:
                if itens[4] == "Disponivel":
                    itens[4] = "Indisponivel"
                    print("O livro foi emprestado a você\n")
                    # Verifica se o codigo que o usuario colocou existe no livros.csv e se existir muda o status
                    # do livro pedido de "Disponivel" para "Indisponivel" por estar agora com a pessoa e faz um filro 
                    # para ver se o livro já foi empestado ou não vendo o status do livro (Diponivel ou Indisponivel)
                else:
                    print("O Livro já foi emprestado\n")
                    # Se o livro já tiver sido emprestado, mostra que o livro já foi emprestado
            linha.append(itens)

    with open ('livros.csv','w',newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerows(linha)
        # Escreve na pasta livros.csv que o livro está Indisponivel

def devolver_livro (codigo):
    linha = []
    with open ('livros.csv','r',newline='') as arquivo:
        buscar_livro = csv.reader(arquivo)
        for itens in buscar_livro:
            if itens[3] == codigo:
                if itens[4] == "Indisponivel":
                    itens[4] = "Disponivel"
                    print("O livro foi devolvido\n")
                    # Verifica se o codigo que o usuario colocou existe no livros.csv e se existir muda o status
                    # do livro pedido de "Indisponivel" para "Disponivel" por estar agora com a pessoa e faz um filro 
                    # para ver se o livro já foi empestado ou não vendo o status do livro (Diponivel ou Indisponivel)
                else:
                    print("O livro já foi devolvido\n")
                    # Se o livro já tiver sido devolvido, mostra que o livro já foi devolvido
            linha.append(itens)

    with open ('livros.csv','w',newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerows(linha)
        # Escreve na pasta livros.csv que o livro está Disponivel

def listar_livros ():
    with open ('livros.csv','r') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
                print(f" Livro: {linha["titulo"]} ; Autor: {linha["autor"]} ; Ano: {linha["ano"]} ; Codigo: {linha["codigo"]} ; Status: {linha["status"]}\n")
                # Mostra toda a lista de livros que tem na pasta do livros.csv

def busca_de_livro_autor(autor):
    encontrou_autor = 0
    with open ('livros.csv','r',newline='') as arquivo:
        buscar_autor = csv.reader(arquivo)
        for itens in buscar_autor:
            if autor == itens[1]:
                encontrou_autor = 1
                print(f"Livro: {itens[0]} ; Autor: {itens[1]} ; Ano: {itens[2]} ; Codigo: {itens[3]} ; Status: {itens[4]}\n")
                # Procura o autor que o usuario colocar na pasta livros.csv e coloca o "encontrou_autor = 1" para não dar o erro em que
                # o codigo tenta dar a mensagem de não ter encontrado nos livros que não foram os que o usuario solicitou e mostra todas 
                # as, além disso, mostra informações do livro pedido
        if encontrou_autor == 0:
            print("Não foi encontrado nem um livro com esse autor\n")
                # Se não tiver encontrado nem um livro, mostra a mensagem de não ter encontrado nem um livro

def busca_de_livro_titulo(titulo):
    encontrou_livro = 0
    with open ('livros.csv','r',newline='') as arquivo:
        buscar_titulo = csv.reader(arquivo)
        for itens in buscar_titulo:
            if titulo == itens[0]:
                encontrou_livro = 1
                print(f"Livro: {itens[0]} ; Autor: {itens[1]} ; Ano: {itens[2]} ; Codigo: {itens[3]} ; Status: {itens[4]}\n")
                # Procura o título que o usuario colocar na pasta livros.csv e coloca o "encontrou_livro = 1" para não dar o erro em que
                # o codigo tenta dar a mensagem de não ter encontrado nos livros que não foram os que o usuario solicitou, além disso,
                # mostra todas as as informações do livro pedido
        if encontrou_livro == 0:
            print("Não foi encontrado nem um livro com esse título\n")
            # Se não tiver encontrado nem um livro, mostra a mensagem de não ter encontrado nem um livro

def organizar_livros(escolha_organizacao):
    with open ('livros.csv','r') as arquivo:
        tipo_organizacao = escolha_organizacao - 1
        leitor = csv.reader(arquivo)
        next(leitor)
        lista_organizacao= list(leitor)
        if escolha_organizacao == 3:
            lista_organizacao.sort(key=lambda lista_organizacao: int(lista_organizacao[tipo_organizacao]))
        else:
            lista_organizacao.sort(key=lambda lista_organizacao: lista_organizacao[tipo_organizacao])
        # Organiza a lista de acordo com o que o usuario pedir, então se ele colocar o 1, ira buscar na pasta livros.csv e nas
        # listas qual é a em ordem alfabética ou numérica e mostra as informações dos livros na ordem que o usuario pediu para organizar
        for itens in lista_organizacao:
            print(f"Livro: {itens[0]} ; Autor: {itens[1]} ; Ano: {itens[2]} ; Codigo: {itens[3]} ; Status: {itens[4]}\n")


while True:
    resposta_menu = input("Bem vindo(a) a biblíoteca, o que gostaria de fazer?\n1 - [CADASTRAR]\n2 - [EMPRESTAR]\n3 -- [DEVOLVER]\n4 ---- [LISTAR]\n5 ---- [BUSCAR]\n6 --- [ORDENAR]\n7 ------ [SAIR]\n")
    # Este é o menu inicial da biblíoteca, pergunta o que o usuario deseja fazer

    match resposta_menu:
        case "1":
            titulo = input("Informe qual o título do livro:\n")
            autor = input("Informe qual o autor do livro:\n")
            while True:
                try:
                    ano = int(input("Informe qual o ano do livro (Apenas números):\n"))
                except ValueError:
                    print("Não é um número inteiro")
                    continue
                try:
                    codigo = int(input("Informe qual o codigo do livro?"))
                    break
                except ValueError:
                    print("Não é um número inteiro")
            cadastrar_livro(titulo,autor,ano,codigo)
            print("Seu livro foi cadastrado!\n")
            # Esta é a primeira função, que é a de cadastrar um livro, ela pergunta qual o titulo, autor, ano e codigo do livro, e automaticamente
            # já o coloca como disponível utilizando a função "cadastrar_livro()"

        case "2":
            codigo_livro = input("Qual o codigo do livro que você deseja pegar?\n")
            emprestimo_de_livro(codigo_livro)
            # Esta é a função de emprestar o livro, ela pede qual o codigo do livro e empresta para o usuario caso o codigo exista e o livro esteja
            # disponível

        case "3":
            codigo_livro = input("Qual o codigo do livro que você deseja devolver?\n")
            devolver_livro(codigo_livro)
            # Esta é a função de devolver o livro, ela pede qual o codigo do livro e pega de volta caso o codigo exista e o livro esteja
            # indisponivel

        case "4":
            print("Todos os livros estão a seguir:\n")
            listar_livros()
            # Esta é a função que mostra todos os livros que estão na pasta livros.csv

        case "5":
            escolha_de_busca = int(input("Escolha um tipo de busca\n1 ---- [Por autor]\n2 -- [Por título]\n"))
            if escolha_de_busca == 1:
                nome_autor = input("Qual o nome do autor?\n")
                busca_de_livro_autor(nome_autor)
            elif escolha_de_busca == 2:
                titulo_livro = input("Qual o titulo do livro?\n")
                busca_de_livro_titulo(titulo_livro)
            else:
                print("Opção invalida\n")
            # Esta é a função que faz a busca dos livros, que podem ser tanto pelo autor, tanto pelo título do livro e mostra os
            # resultados encontrado
        case "6":
            while True:
                try:
                    escolha_de_ordenagem = int(input("Escolaha um tipo de ordenação\n1 -- [Por título]\n2 -- [Por autor]\n3 -- [Por ano]\n"))
                except ValueError:
                    print("Número invalido\n")
                    continue

                if escolha_de_ordenagem not in [1,2,3]:
                    print("Número invalido\n")
                    continue

                organizar_livros(escolha_de_ordenagem)
                break
            # Esta é a função que mostra uma lista organizada de a cordo com o que o usuario desejar dentre as opções (título, autor e ano)
        case "7":
            break
        case _:
            print("Número inválido")