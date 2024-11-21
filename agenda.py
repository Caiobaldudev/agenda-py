# Project Agenda
def adicionar_contato(contatos, nome_contato, telefone, email):
  contato = {"nome": nome_contato, "telefone": telefone, "email": email, "favorito": False}
  contatos.append(contato)
  print(f"Contato de: {nome_contato} adicionado com sucesso!")
  return

def ver_contatos(contatos):
  print("\nLista de contatos:")
  if not contatos:
    print("Nenhum contato cadastrado.")
  for indice, contato in enumerate(contatos, start=1):
    status = "★" if contato ["favorito"] else " "
    print(f"{indice}. [{status}] {contato['nome']} - {contato['telefone']} - {contato['email']} .")
  return

def atualizar_contatos(contatos):
  ver_contatos(contatos)
  try:
    indice = int(input("\nDigite o número do contato que deseja editar: ")) - 1
    if 0 <= indice < len(contatos):
      nome = input("Digite o novo nome (ou pressione Enter para manter o atual): ")
      telefone = input("Digite o novo telefone (ou pressione Enter para manter o atual):")
      email = input("Digite o novo email (ou pressione Enter para manter o atual):")
      contatos[indice].update({"nome": nome, "telefone": telefone, "email": email})
      print("\nContato atualizado com sucesso!")
    else:
      print("Contato inválido!")
  except ValueError:
    print("Entrada inválida!")
  return

def add_favorito(contatos):
  ver_contatos(contatos)
  try:
    indice = int(input("\nDigite o número do contato para marcar/desmarcar como favorito: ")) - 1
    if 0 <= indice < len(contatos):
      contatos[indice]["favorito"] = not contatos[indice]["favorito"]
      estado = "favorito" if contatos[indice]["favorito"] else "não favorito"
      print(f"\nContato {contatos[indice]['nome']} marcado como {estado}.")
    else:
      print("Contato inválido!")
  except ValueError:
    print("Entrada inválida!")
  return

def ver_lista_favoritos(contatos):
  print("\nLista de contatos favoritos:")
  favoritos = [contato for contato in contatos if contato['favorito']]
  if not favoritos:
    print("Nenhum contato favorito.")
  for contato in favoritos:
    print(f"★ {contato['nome']} - {contato['telefone']} - {contato['email']}")
  return

def apagar_contato(contatos):
  ver_contatos(contatos)
  try:
    indice = int(input("\nDigite o número do contato que deseja apagar: ")) - 1
    if 0 <= indice < len(contatos):
      removido = contatos.pop(indice)
      print(f"\nContato {removido['nome']} apagado com sucesso!")
    else:
      print("Contato inválido!")
  except ValueError:
    print("Entrada inválida!")
  return

contatos = []

while True:
  print("\nMenu do Gerenciador de Lista de Contatos:")
  print("1. Adicionar Contato")
  print("2. Ver lista de contatos")
  print("3. Editar um contato")
  print("4. Marcar como favorito")
  print("5. Ver lista de favoritos")
  print("6. Apagar um contato")
  print("7. Sair")

  escolha = input("Digite a sua escolha: ")

  if escolha == "1":
    nome_contato = input("Digite o nome do contato que deseja adicionar: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    adicionar_contato(contatos, nome_contato, telefone, email)
  elif escolha == "2":
    ver_contatos(contatos)
  elif escolha == "3":
    atualizar_contatos(contatos)
  elif escolha == "4":
    add_favorito(contatos)
  elif escolha == "5":
    ver_lista_favoritos(contatos)
  elif escolha == "6":
    apagar_contato(contatos)
  elif escolha == "7":
    print("\nPrograma Finalizado!")
    break
  else:
    print("\nOpção inválida! Tente novamente.")