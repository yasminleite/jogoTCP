import socket
import random

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8000))
    server_socket.listen(2)

    print("Aguardando conexão de dois jogadores...")

    while True:
        (jogador1, address1) = server_socket.accept()
        print("Jogador 1 conectado de ", address1)

        (jogador2, address2) = server_socket.accept()
        print("Jogador 2 conectado de ", address2)

        jogadores(jogador1, jogador2)

def jogadores(jogador1, jogador2):
    numero = random.randint(1, 20)
    print("O número a ser adivinhado é: ", numero)

    for i in range(10):
        palpite1 = jogador1.recv(1024)
        palpite1 = int(palpite1.decode('utf-8'))

        palpite2 = jogador2.recv(1024)
        palpite2 = int(palpite2.decode('utf-8'))

        print(f"Jogador 1: {palpite1} | Jogador 2: {palpite2}")

        if palpite1 == numero and palpite2 == numero:
            jogador1.send(b'Empate')
            jogador2.send(b'Empate')
            return
        elif palpite1 == numero:
            jogador1.send(b'Ganhou')
            jogador2.send(b'Perdeu')
            return
        elif palpite2 == numero:
            jogador1.send(b'Perdeu')
            jogador2.send(b'Ganhou')
            return
        else:
            if palpite1 < numero and palpite2 < numero:
                jogador1.send(b'Maior')
                jogador2.send(b'Maior')
            elif palpite1 > numero and palpite2 > numero:
                jogador1.send(b'Menor')
                jogador2.send(b'Menor')
            if palpite1 > numero and palpite2 < numero:
                jogador1.send(b'Menor')
                jogador2.send(b'Maior')
            elif palpite1 < numero and palpite2 > numero:
                jogador1.send(b'Maior')
                jogador2.send(b'Menor')
        
    print("Acabaram as tentativas dos 2 clientes")
    return

    jogador1.send(b'Perdeu')
    jogador2.send(b'Perdeu')


if __name__ == '__main__':
    main()