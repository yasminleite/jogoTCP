import socket

def main():
    while True:

        print("\n")
        print("Tente adivinhar um número de 1 a 20. Você tem 10 tentativas. \n")
        print("╔══════════ ❖ ══════════╗ ")

        # Conecta com o servidor
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 8000))

        for i in range(10):
            palpite = input(" Digite um número: ")
            client_socket.send(palpite.encode('utf-8'))

            resultado = client_socket.recv(1024)
            resultado = resultado.decode('utf-8')

            if resultado == 'Maior':
                print(" ► Tente um número maior.")
            elif resultado == 'Menor':
                print(" ► Tente um número menor.")
            elif resultado == 'Ganhou':
                print(" Parabéns! Você ganhou.")
                print("╚══════════ ❖ ══════════╝")
                client_socket.close()
                break
            elif resultado == 'Perdeu':
                print(" Você perdeu o jogo.")
                print("╚══════════ ❖ ══════════╝")
                client_socket.close()
                break
            elif resultado == 'Empate':
                print(" Empate! \n Nenhum jogador venceu.")
                print("╚══════════ ❖ ══════════╝ \n")
                client_socket.close()
                break

        print("Acabaram as tentativas")

        jogar_novamente = input("◈ Deseja jogar novamente? (s/n) ").lower()
        while jogar_novamente not in ['s', 'n']:
            jogar_novamente = input(
                "◈ Opção inválida. Deseja jogar novamente? (s/n) ").lower()


        if jogar_novamente == 'n':
            break

if __name__ == '__main__':
    main()



