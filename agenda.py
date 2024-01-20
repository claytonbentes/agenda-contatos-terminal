def adicionar_contato(contatos,nome_contato,telefone_contato,email_contato):
    contato = {"Contato": nome_contato, "Telefone": telefone_contato, "Email": email_contato, "Favorito":False}
    contatos.append(contato)
    print(f"\nContato adicionado com sucesso! Dados: {nome_contato}, {telefone_contato}, {email_contato}")
    return

def visualizar_contato(contatos):
    print("\nLista de Contatos: ")
    for indice,contato in enumerate(contatos,start=1):
        status = "☆" if contato["Favorito"] else " "
        nome_contato = contato["Contato"]
        telefone_contato = contato["Telefone"]
        email_contato = contato["Email"]
        print(f"{indice}. [{status}] {nome_contato} - {telefone_contato} - {email_contato}")
    return

def editar_contato(contatos, indice_contato, novo_nome_contato, novo_telefone_contato, novo_email_contato):
    indice_ajustado = int(indice_contato) - 1
    if indice_ajustado >=0 and indice_ajustado < len(contatos):
        contatos[indice_ajustado]["Contato"] = novo_nome_contato
        contatos[indice_ajustado]["Telefone"] = novo_telefone_contato
        contatos[indice_ajustado]["Email"] = novo_email_contato
    else:
        print("Indice de contato invalido.")        
    return

def favoritar_contato(contatos,indice_contato):
    indice_ajustado = int(indice_contato) - 1
    if indice_ajustado>=0 and indice_ajustado<len(contatos):
        if contatos[indice_ajustado]["Favorito"]==False:
            contatos[indice_ajustado]["Favorito"]=True
            print(f"Contato {indice_contato} marcado como favorito")
        else:
            contatos[indice_ajustado]["Favorito"]=False
            print(f"Contato {indice_contato} desmarcado como favorito")
    else:
        print("Indice do contato invalido")
    return

def lista_favoritos(contatos):
    print("\nLista de Favoritos: ")
    for indice,contato in enumerate(contatos,start=1):
        if contato["Favorito"]==True:
            status = "☆"
            nome_contato = contato["Contato"]
            telefone_contato = contato["Telefone"]
            email_contato = contato["Email"]
            print(f"{indice}. [{status}] {nome_contato} - {telefone_contato} - {email_contato}")
    return

def deletar_contato(contatos,indice_contato):
    indice_ajustado =  int(indice_contato) - 1
    if indice_ajustado>= 0 and indice_ajustado<len(contatos):
        del contatos[indice_ajustado]
        print("Contato deletado com sucesso!")
    else:
        print("Indice do contato invalido")
    return

contatos=[]

while True:
    print("\nMinha agenda:")
    print("1. Adicionar contato")
    print("2. Visualizar lista de contato")
    print("3. Editar contato")
    print("4. Marcar/Desmarcar como favorito")
    print("5. Lista de favoritos")
    print("6. Deletar contato")
    print("7. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nome_contato = input("Qual o nome do contato? ")
        telefone_contato = input("Qual o telefone do contato? ")
        email_contato = input("Qual o email do contato? ")
        adicionar_contato(contatos,nome_contato,telefone_contato,email_contato)

    elif escolha == "2":
        visualizar_contato(contatos)
    
    elif escolha == "3":
        visualizar_contato(contatos)
        indice_contato = input("Qual contato deseja editar? ")
        novo_nome = input("Digite o novo nome: ")
        novo_telefone = input("Digite o novo telefone: ")
        novo_email = input("Digite o novo email: ")
        editar_contato(contatos, indice_contato,novo_nome,novo_telefone, novo_email)

    elif escolha == "4":
        visualizar_contato(contatos)
        indice_contato = input("Qual contato deseja favoritar/desfavoritar? ")
        favoritar_contato(contatos, indice_contato)

    elif escolha == "5":
        lista_favoritos(contatos)

    elif escolha == "6":
        visualizar_contato(contatos)
        indice_contato = input("Qual contato deseja deletar? ")
        deletar_contato(contatos,indice_contato)

    elif escolha == "7":
        break

print("\nAGENDA FECHADA")