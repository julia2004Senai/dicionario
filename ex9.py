agenda = {}

while True:
    nome = input("Digite o nome completo: ")
    if nome == '':
        break
    telefone = input("Digite o telefone: ")
    agenda[nome] = telefone
   
    nome_pesquisa = input("Digite o nome para pesquisar: ")
    if nome_pesquisa in agenda:
       print("Telefone de", nome_pesquisa, ":", agenda[nome_pesquisa])
    else:
        print("Nome não encontrado na agenda.")