import os
import csv
os.system ("cls")

estrutura = ['titulo', 'autor', 'ano', 'codigo', 'status']

def cadastrar_livro (titulo,autor,ano):
    quantidade_de_livros = int(0)

    with open ('livros.csv','r',) as arquivo:
        for line in arquivo:
            quantidade_de_livros += 1
        codigo = int(00000000) + (quantidade_de_livros-1)
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
    livro_encontrado = 0

    with open ('livros.csv','r',newline='') as arquivo:
        buscar_livro = csv.reader(arquivo)
        for itens in buscar_livro:
            if itens[3] == codigo:
                livro_encontrado = 1

                if itens[4] == "Disponivel":
                    itens[4] = "Indisponivel"
                    print("O livro foi emprestado a você\n")

                else:
                    print("O Livro já foi emprestado\n")
            linha.append(itens)

    with open ('livros.csv','w',newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerows(linha)



while True:
    resposta_menu = input("Bem vindo(a) biblíoteca, o que gostaria de fazer?\n1 - [CADASTRAR]\n2 - [EMPRESTAR]\n3 -- [DEVOLVER]\n4 ---- [LISTAR]\n5 ---- [BUSCAR]\n6 --- [ORDENAR]\n7 ------ [SAIR]\n")
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
            pass
        case "4":
            pass
        case "5":
            pass
        case "6":
            pass
        case "7":
            break