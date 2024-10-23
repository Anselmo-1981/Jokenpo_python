def modulo_checa_opcao(opcao,computador,nome):


    if opcao == 1:
        jogador = "Pedra"
        return comparador(jogador=jogador,computador=computador,nome=nome)


    elif opcao == 2:
        jogador = "Tesoura"
        return comparador(jogador=jogador, computador=computador, nome=nome)


    elif opcao == 3:
        jogador = "Papel"
        return comparador(jogador=jogador, computador=computador, nome=nome)


    elif opcao != 1 or opcao != 2 or opcao != 3:
        print(f"\n\t\t\t\t{opcao} não é uma opção válida.")
        print("\t\t\t\tComo penalidade 1 ponto será atribuído ao computador.")
        resultado = 2
        return resultado

    else:
        pass




def comparador(jogador,computador,nome):


    if jogador == "Pedra" and computador == "Pedra":
        print(f"""\n\t\t\t\t{nome} escolheu: {jogador}\n\t\t\t\tCOMPUTADOR escolheu: {computador}
\t\t\t\tA rodada empatou.""")
        resultado = 0
        return resultado


    elif jogador == "Tesoura" and computador == "Pedra":
        print(f"""\n\t\t\t\t{nome} escolheu: {jogador}\n\t\t\t\tCOMPUTADOR escolheu: {computador}
\t\t\t\tO computador venceu essa rodada.""")
        resultado = 2
        return resultado


    elif jogador == "Papel" and computador == "Pedra":
        print(f"""\n\t\t\t\t{nome} escolheu: {jogador}\n\t\t\t\tCOMPUTADOR escolheu: {computador}
\t\t\t\t{nome}, você venceu essa rodada.""")
        resultado = 1
        return resultado


    elif jogador == "Pedra" and computador == "Tesoura":
        print(f"""\n\t\t\t\t{nome} escolheu: {jogador}\n\t\t\t\tCOMPUTADOR escolheu: {computador}
\t\t\t\t{nome}, você venceu essa rodada.""")
        resultado = 1
        return resultado


    elif jogador == "Pedra" and computador == "Papel":
        print(f"""\n\t\t\t\t{nome} escolheu: {jogador}\n\t\t\t\tCOMPUTADOR escolheu: {computador}
\t\t\t\tO computador venceu essa rodada.""")
        resultado = 2
        return resultado


    elif jogador == "Papel" and computador == "Tesoura":
        print(f"""\n\t\t\t\t{nome} escolheu: {jogador}\n\t\t\t\tCOMPUTADOR escolheu: {computador}
\t\t\t\tO computador venceu essa rodada.""")
        resultado = 2
        return resultado


    elif jogador == "Papel" and computador == "Papel":
        print(f"""\n\t\t\t\t{nome} escolheu: {jogador}\n\t\t\t\tCOMPUTADOR escolheu: {computador}
\t\t\t\tA rodada empatou.""")
        resultado = 0
        return resultado


    elif jogador == "Tesoura" and computador == "Tesoura":
        print(f"""\n\t\t\t\t{nome} escolheu: {jogador}\n\t\t\t\tCOMPUTADOR escolheu: {computador}
\t\t\t\tA rodada empatou.""")
        resultado = 0
        return resultado


    elif jogador == "Tesoura" and computador == "Papel":
        print(f"""\n\t\t\t\t{nome} escolheu: {jogador}\n\t\t\t\tCOMPUTADOR escolheu: {computador}
\t\t\t\t{nome}, você venceu essa rodada.""")
        resultado = 1
        return resultado


    else:
        print("\t\t\t\tVerificar se falta essa opção.")