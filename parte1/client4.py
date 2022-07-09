import socket 
import argparse

parser = argparse.ArgumentParser(description = "Cliente para o servidor")
parser.add_argument('--host', metavar = 'host', type = str, nargs = '?', default = "127.0.0.1")
parser.add_argument('--port', metavar = 'port', type = int, nargs = '?', default = 9999)
args = parser.parse_args()

print(f"Conectando com o servidor: {args.host} na porta: {args.port}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sck:
    try:
        sck.connect((args.host, args.port))
    except Exception as e:
        raise SystemExit(f" Falhamos em conectar com o host: {args.host} na porta: {args.port}, porque: {e}")

    while True:
        teste = input("Deseja fazer consulta ou sair? (digite 'sim' para continuar e 'sair' para sair ) : ")
        if teste == 'sair':
            print("Fechando o cliente!")
            sck.sendall(teste.encode('utf-8'))
            break
        
        altura = input("Digite a altura: ")
        sexo = input("Digite o sexo: ")

        msg = altura +"*" + sexo
        sck.sendall(msg.encode('utf-8'))

        data = sck.recv(1024)
        print(f"O servidor respondeu: {data.decode()}")
