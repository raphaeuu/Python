import os

print("\n")
print("ｓａｂｏｒ ｅｘｐｒｅｓｓ\n")
nome_usuario = input("Qual o seu nome? ")
print(f'Bem vindo ao nosso restaurante, {nome_usuario}! O que deseja?')

print("\n")

print("1. Cadastrar restaurante")
print("2. Listar restaurante")
print("3. Ativar restaurante")
print("4. Sair\n")

opcao_escolhida = int(input(f'{nome_usuario}, escolha uma opção: '))


def finalizar_app():
    os.system('cls')
    print('Finalizando o app, obrigado!')

if opcao_escolhida == 1:
    print('Cadastar restaurante.')
elif opcao_escolhida == 2:
    print("Listar restaurante.")
elif opcao_escolhida == 3:
    print("Ativar restaurante.")
else:
    finalizar_app()