import random
import time

player_pontos = 0
cpu_pontos = 0

while True:

    print('=-=' * 10)
    print('=           PLACAR           =')
    print('=       CPU {} x {} PLAYER     ='.format(cpu_pontos, player_pontos))
    print('=-=' * 10)


    player = str(input('Player: '))

    if player == 'sair':
        if cpu_pontos > player_pontos:
            print("O ganhador foi:")
            print("CPU com {} pontos".format(cpu_pontos))
        elif player_pontos > cpu_pontos:
            print("O ganhador foi:")
            print("Player com {} pontos".format(player_pontos))
        else:
            print("Jogo Empatou!")
        break

    else:
        print('')
        print('jo')
        time.sleep(0.5)
        print('ken')
        time.sleep(0.5)
        print('pow!!')
        print("")

    jogadas_cpu = ['pedra', 'papel', 'tesoura']
    escolha_cpu = random.choice(jogadas_cpu)

    if player == 'pedra':
        if escolha_cpu == 'pedra':
            print('PLAYER: ',player)
            print('CPU: ', escolha_cpu)
            print('Empatou!')

        elif escolha_cpu == 'papel':
            print('PLAYER: ', player)
            print('CPU: ', escolha_cpu)
            print('CPU Ganhou!')
            cpu_pontos = cpu_pontos + 1


        elif escolha_cpu == 'tesoura':
            print('PLAYER: ', player)
            print('CPU: ', escolha_cpu)
            print('Player Ganhou!')
            player_pontos = player_pontos + 1

        else:
            print('ALGO DEU ERRADO!, tente com letras minusculas apenas.')

    elif player == 'papel':
        if escolha_cpu == 'pedra':
            print('PLAYER: ', player)
            print('CPU: ', escolha_cpu)
            print('Player Ganhou!')
            player_pontos = player_pontos + 1

        elif escolha_cpu == 'papel':
            print('PLAYER: ', player)
            print('CPU: ', escolha_cpu)
            print('Empatou!')

        elif escolha_cpu == 'tesoura':
            print('PLAYER: ', player)
            print('CPU: ', escolha_cpu)
            print('CPU Ganhou!')
            cpu_pontos = cpu_pontos + 1

        else:
            print('ALGO DEU ERRADO!, tente com letras minusculas apenas.')

    elif player == 'tesoura':
        if escolha_cpu == 'pedra':
            print('PLAYER: ', player)
            print('CPU: ', escolha_cpu)
            print('CPU Ganhou!')
            cpu_pontos = cpu_pontos + 1

        elif escolha_cpu == 'papel':
            print('PLAYER: ', player)
            print('CPU: ', escolha_cpu)
            print('Player Ganhou!')
            player_pontos = player_pontos + 1

        elif escolha_cpu == 'tesoura':
            print('PLAYER: ', player)
            print('CPU: ', escolha_cpu)
            print('Empatou!')

        else:
            print('ALGO DEU ERRADO!, tente com letras minusculas apenas.')

    else:
        print('ALGO DEU ERRADO!, tente com letras minusculas apenas. ex:(pedra, papel, tesoura)')