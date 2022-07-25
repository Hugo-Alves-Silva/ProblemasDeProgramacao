import socket
import argparse
import threading 

parser = argparse.ArgumentParser(description = "Servidor multithreading")
parser.add_argument('--host', metavar = 'host', type = str, nargs = '?', default = "127.0.0.1")
parser.add_argument('--port', metavar = 'port', type = int, nargs = '?', default = 9998)
args = parser.parse_args()

pessoas = {
    'João da Silva': ['operador', 2000.0], 
    'Mario da Costa': ['programador', 3000.0],
    'Pedro Silva Rodrigues': ['programador', 5500.50],
    'Maria de Souza': ['médica', 10000.0],
    'Ana Paula Faria': ['operadora', 3500.0]
}

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
    msg = client.recv(1024)
    dados = msg.decode()
    informacoes = pessoas.get(dados) 
    if(informacoes == None):
        reply = 'Pessoa não encontrada no banco de dados'
    else:
        reply = informacoes[0] + "*" + str(informacoes[1])
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
