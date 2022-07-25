import socket
import argparse
import threading 

parser = argparse.ArgumentParser(description = "Servidor multithreading")
parser.add_argument('--host', metavar = 'host', type = str, nargs = '?', default = "127.0.0.1")
parser.add_argument('--port', metavar = 'port', type = int, nargs = '?', default = 9999)
parser.add_argument('--hostBD', metavar = 'hostBD', type = str, nargs = '?', default = "127.0.0.1")
parser.add_argument('--portBD', metavar = 'portBD', type = int, nargs = '?', default = 9998)
args = parser.parse_args()

print(f"Rodando o servidor no host: {args.host} e na porta: {args.port}")
print(f"Digite Ctrl + c para sair")
sck = socket.socket()
sck.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try: 
    sck.bind((args.host, args.port))
    sck.listen(5)
except Exception as e:
    raise SystemExit(f"Não conseguimos ligar o servidor no host: {args.host} na porta: {args.port}, porque: {e}")


def on_new_client(client, connection):
    ip = connection[0]
    port = connection[1]
    print(f"A nova conexão foi feita do IP: {ip}, e da porta: {port}!")
    while True:
        msg = client.recv(1024)
        if msg.decode() == 'sair':
            break
        dados = msg.decode()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sckBD:
            try:
                sckBD.connect((args.hostBD, args.portBD))
            except Exception as e:
                raise SystemExit(f" Falhamos em conectar com o host: {args.hostBD} na porta: {args.portBD}, porque: {e}")
        
            sckBD.sendall(dados.encode('utf-8'))
            msg2 = sckBD.recv(1024)
            sckBD.close()
        
        dados2 = msg2.decode().split("*")
        if len(dados2) == 1:
            reply = dados2[0]
        else:
            salarioAux = dados2[1].split(".")
            salario = int(salarioAux[0])
            if len(salarioAux) > 1:
                salario += (int(salarioAux[1]) / 100)
        
        
            if dados2[0].lower() == 'operador' or dados2[0].lower() == 'operadora':
                salario += (salario * (20/100))
            elif dados2[0].lower() == 'programador' or dados2[0].lower() == 'programadora':
                salario += (salario* (18/100))
  
            reply = f"{dados} com salário de: {salario}"
        
        client.sendall(reply.encode('utf-8'))
        
    print(f"O cliente do ip: {ip}, e da porta: {port}, foi desconectado!")
    client.close()

while True:
    try: 
        client, ip = sck.accept()
        threading._start_new_thread(on_new_client,(client, ip))
    except KeyboardInterrupt:
        print(f"\nFechando o servidor!")
        break
    except Exception as e:
        print(f"Nós não antecipamos isto: {e}")

sck.close()
