import os
import csv
os.system ("cls")

estrutura = ['titulo', 'autor', 'ano', 'codigo', 'status']

def cadastrar_livro (titulo,autor,ano):
    quantidade_de_livros = int(0)

    with open ('livros.csv','r',) as arquivo:
        for line in arquivo:
            quantidade_de_livros += 1
        codigo = int(10000000) + (quantidade_de_livros-1)
        ## Essa é a parte onde é criado o codigo do livro onde usa a quantidade de livros para 
        # conseguir fazer o codigo de cada livro

    with open ('livros.csv','a',newline='') as cadastro_livro:
        livro = {'titulo':titulo, 'autor':autor, 'ano':ano, 'codigo':codigo, 'status':"Disponivel"}
        escritor = csv.DictWriter(cadastro_livro,fieldnames=estrutura)
        escritor.writerow(livro)
    ## A função faz a criação do livro e manda para a pasta de livros.csv, salvando o livro cadastrado no "case 1"
    # e para uma próxima vez que a pessoa acesar esse codigo novamente

def emprestimo_de_livro (codigo):
    linha = []

    with open ('livros.csv','r',newline='') as arquivo:
        buscar_livro = csv.reader(arquivo)
        for itens in buscar_livro:
            if itens[3] == codigo:

                if itens[4] == "Disponivel":
                    itens[4] = "Indisponivel"
                    print("O livro foi emprestado a você\n")

                else:
                    print("O Livro já foi emprestado\n")
            linha.append(itens)

    with open ('livros.csv','w',newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerows(linha)

def devolver_livro (codigo):
    linha = []

    with open ('livros.csv','r',newline='') as arquivo:
        buscar_livro = csv.reader(arquivo)
        for itens in buscar_livro:
            if itens[3] == codigo:
                if itens[4] == "Indisponivel":
                    itens[4] = "Disponivel"
                    print("O livro foi devolvido\n")

                else:
                    print("O livro já foi devolvido\n")
            linha.append(itens)

    with open ('livros.csv','w',newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerows(linha)

def listar_livros ():
    with open ('livros.csv','r') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
                print(f" Livro: {linha["titulo"]} ; Autor: {linha["autor"]} ; Ano: {linha["ano"]} ; Codigo: {linha["codigo"]} ; Status: {linha["status"]}\n")

def busca_de_livro_autor(autor):
    encontrou_autor = 0
    with open ('livros.csv','r',newline='') as arquivo:
        buscar_autor = csv.reader(arquivo)
        for itens in buscar_autor:
            if autor == itens[1]:
                encontrou_autor = 1
                print(f"Livro: {itens[0]} ; Autor: {itens[1]} ; Ano: {itens[2]} ; Codigo: {itens[3]} ; Status: {itens[4]}\n")
        if encontrou_autor == 0:
            print("Não foi encontrado nem um livro com esse autor\n")

def busca_de_livro_titulo(titulo):
    encontrou_livro = 0
    with open ('livros.csv','r',newline='') as arquivo:
        buscar_titulo = csv.reader(arquivo)
        for itens in buscar_titulo:
            if titulo == itens[0]:
                encontrou_livro = 1
                print(f"Livro: {itens[0]} ; Autor: {itens[1]} ; Ano: {itens[2]} ; Codigo: {itens[3]} ; Status: {itens[4]}\n")
        if encontrou_livro == 0:
            print("Não foi encontrado nem um livro com esse título\n")

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
                    break
                except ValueError:
                    print("Não é um número inteiro")
            cadastrar_livro(titulo,autor,ano)
            print("Seu livro foi cadastrado!\n")
        ##Este é a primeira função, que é a de cadastrar um livro, ela pergunta qual o titulo, autor e ano do livro, e automaticamente
        # já o coloca como disponível e da o seu codigo com base no sistema ISBN utilizando a função "cadastrar_livro()"

        case "2":
            codigo_livro = input("Qual o codigo do livro que você deseja pegar?\n")
            emprestimo_de_livro(codigo_livro)

        case "3":
            codigo_livro = input("Qual o codigo do livro que você deseja devolver?\n")
            devolver_livro(codigo_livro)

        case "4":
            print("Todos os livros estão a seguir:\n")
            listar_livros()

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
        case "6":
            escolha_de_ordenar = int(input("Escolaha um tipo de ordenação\n1 -- [Por título]\n2 -- [Por autor]\n3 -- [Por ano]"))
            if escolha_de_ordenar == 1:
                pass
            elif escolha_de_ordenar == 2:
                pass
            elif escolha_de_ordenar == 3:
                pass
            else:
                print("Número invalida\n")
        case "7":
            break
        case _:
            print("Número inválido")