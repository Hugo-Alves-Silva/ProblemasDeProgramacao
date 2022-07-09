import socket
import argparse
import threading 

parser = argparse.ArgumentParser(description = "Este é o servidor")
parser.add_argument('--host', metavar = 'host', type = str, nargs = '?', default = "127.0.0.1")
parser.add_argument('--port', metavar = 'port', type = int, nargs = '?', default = 9999)
args = parser.parse_args()


print(f"Rodando o servidor no host: {args.host} e na porta: {args.port}")
print(f"Digite Ctrl + c para sair")
sck = socket.socket()
sck.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try: 
    sck.bind((args.host, args.port))
    sck.listen(5)
except Exception as e:
    raise SystemExit(f"Não conseguimos ligar o servidor no host : {args.host} na porta: {args.port}, porque: {e}")


def on_new_client(client, connection):
    ip = connection[0]
    port = connection[1]
    print(f"A nova conexão foi feita do IP: {ip}, e da porta: {port}!")
    while True:
        msg = client.recv(1024)
        if msg.decode() == 'sair':
            break
        dados = msg.decode().split("*")
        salarioAux = dados[2].split(",")
        salario = int(salarioAux[0])
        if len(salarioAux) > 1:
            salario += (int(salarioAux[1]) / 100)
        
        
        if dados[1].lower() == 'operador':
            salario += (salario * (20/100))
        elif dados[1].lower() == 'programador':
            salario += (salario* (18/100))
  
        reply = f"{dados[0]} com salário de: {salario}"
        client.sendall(reply.encode('utf-8'))

    print(f"O cliente do ip: {ip}, e da porta: {port}, foi desconectado!")
    client.close()

while True:
    try: 
        client, ip = sck.accept()
        on_new_client(client, ip)
    except KeyboardInterrupt:
        print(f"\nFechando o servidor!")
        break
    except Exception as e:
        print(f"Nós não antecipamos isso: {e}")
sck.close()
