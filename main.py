import os
import csv
os.system ("cls")

estrutura = ['titulo', 'autor', 'ano', 'codigo', 'status']

def cadastrar_livro (titulo,autor,ano,codigo,status):
    with open ('gerenciador_de_livros/livros.csv','a',newline='') as cadastro_livro:
        livro = {'titulo':titulo, 'autor':autor, 'ano':ano, 'codigo':codigo, 'status':status}
        writer = csv.DictWriter(f,fieldnames=estrutura)
        writer.writerow(livro)


while True:
    resposta_menu = input("Bem vindo(a) biblíoteca, o que gostaria de fazer?\n1 - [CADASTRAR]\n2 - [EMPRESTAR]\n3 -- [DEVOLVER]\n4 ---- [LISTAR]\n5 ---- [BUSCAR]\n6 --- [ORDENAR]\n7 ------ [SAIR]\n")
    match resposta_menu:
        case "1":
            titulo = input("Informe qual o título do livro:\n")
            autor = input()
            while True:
                try:
                    ano = int(input("Informe qual o ano do livro (Apenas números):\n"))
                    break
                except ValueError:
                    print("Não é um número inteiro")
                try:
                    


        case "2":
            pass
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