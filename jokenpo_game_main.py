import random
from jokenpo_game_modulo_checa_opcao import modulo_checa_opcao




resultado = []
apresentacao = "\n\t\t  ****************  ****************  **** JOKENPÔ ****  ****************  ****************"




system_on = True
while system_on == True:




    print(apresentacao)
    print()
    print("\t\t\t\tVamos jogar Jokenpô?")
    print("\t\t\t\tSerão 5 rodadas no total, então o sistema apresentará o vencedor.")
    print("\t\t\t\tSiga as instruções em tela para interagir com o sistema.")
    print("\t\t\t\tVamos lá!")
    nome = input("\n\t\t\t\tInforme seu nome para começar: ").upper()
    print(apresentacao)




    # Rodada 1
    print("\n\t\t\t\tRODADA 1:")

    # COMPUTADOR ESCOLHE SUA OPÇÃO
    pedra_tesoura_papel = ("Pedra", "Tesoura", "Papel")
    computador = random.choice(pedra_tesoura_papel)
    print()

    # JOGADOR ESCOLHE SUA OPÇÃO
    print(f"\t\t\t\t{nome} escolha entre:")
    print("\t\t\t\t[1] Pedra\n\t\t\t\t[2] Tesoura\n\t\t\t\t[3] Papel")
    opcao = int(input("\t\t\t\tDigite agora uma das opções: "))
    resultado.append(modulo_checa_opcao(opcao=opcao, computador=computador, nome=nome))
    print(apresentacao)




    # Rodada 2
    print("\n\t\t\t\tRODADA 2:")

    # COMPUTADOR ESCOLHE SUA OPÇÃO
    pedra_tesoura_papel = ("Pedra", "Tesoura", "Papel")
    computador = random.choice(pedra_tesoura_papel)
    print()

    # JOGADOR ESCOLHE SUA OPÇÃO
    print(f"\t\t\t\t{nome} escolha entre:")
    print("\t\t\t\t[1] Pedra\n\t\t\t\t[2] Tesoura\n\t\t\t\t[3] Papel")
    opcao = int(input("\t\t\t\tDigite agora uma das opções: "))
    resultado.append(modulo_checa_opcao(opcao=opcao, computador=computador, nome=nome))
    print(apresentacao)




    # Rodada 3
    print("\n\t\t\t\tRODADA 3:")

    # COMPUTADOR ESCOLHE SUA OPÇÃO
    pedra_tesoura_papel = ("Pedra", "Tesoura", "Papel")
    computador = random.choice(pedra_tesoura_papel)
    print()

    # JOGADOR ESCOLHE SUA OPÇÃO
    print(f"\t\t\t\t{nome} escolha entre:")
    print("\t\t\t\t[1] Pedra\n\t\t\t\t[2] Tesoura\n\t\t\t\t[3] Papel")
    opcao = int(input("\t\t\t\tDigite agora uma das opções: "))
    resultado.append(modulo_checa_opcao(opcao=opcao, computador=computador, nome=nome))
    print(apresentacao)




    # Rodada 4
    print("\n\t\t\t\tRODADA 4:")

    # COMPUTADOR ESCOLHE SUA OPÇÃO
    pedra_tesoura_papel = ("Pedra", "Tesoura", "Papel")
    computador = random.choice(pedra_tesoura_papel)
    print()

    # JOGADOR ESCOLHE SUA OPÇÃO
    print(f"\t\t\t\t{nome} escolha entre:")
    print("\t\t\t\t[1] Pedra\n\t\t\t\t[2] Tesoura\n\t\t\t\t[3] Papel")
    opcao = int(input("\t\t\t\tDigite agora uma das opções: "))
    resultado.append(modulo_checa_opcao(opcao=opcao, computador=computador, nome=nome))
    print(apresentacao)




    # Rodada 5
    print("\n\t\t\t\tRODADA 5:")

    # COMPUTADOR ESCOLHE SUA OPÇÃO
    pedra_tesoura_papel = ("Pedra", "Tesoura", "Papel")
    computador = random.choice(pedra_tesoura_papel)
    print()

    # JOGADOR ESCOLHE SUA OPÇÃO
    print(f"\t\t\t\t{nome} escolha entre:")
    print("\t\t\t\t[1] Pedra\n\t\t\t\t[2] Tesoura\n\t\t\t\t[3] Papel")
    opcao = int(input("\t\t\t\tDigite agora uma das opções: "))
    resultado.append(modulo_checa_opcao(opcao=opcao, computador=computador, nome=nome))
    print(apresentacao)



    print("\n\t\t\t\tRESULTADOS:\n")

    jogador = resultado.count(1)
    print(f"\t\t\t\t{nome} vitórias: {jogador}")
    computador = resultado.count(2)
    print(f"\t\t\t\tCOMPUTADOR vitórias: {computador}")
    empate = resultado.count(0)
    print(f"\t\t\t\tRodadas empatadas: {empate}")
    print()

    qt = input(f"\t\t\t\tDeseja jogar novamente? S/N: ").upper()
    if qt == "S":
        resultado.clear()
        system_on = True
    else:
        system_on = False

print("\t\t\t\tSistema encerrado")