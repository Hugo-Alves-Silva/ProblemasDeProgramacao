import socket
import argparse
import threading 

parser = argparse.ArgumentParser(description = "Servidor multithreading")
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
    raise SystemExit(f"Não conseguimos ligar o servidor no host: {args.host} na porta: {args.port}, porque: {e}")


def on_new_client(client, connection):
    ip = connection[0]
    port = connection[1]
    print(f"A nova conexão foi feita do IP: {ip}, e da porta: {port}!")
    while True:
        msg = client.recv(1024)
        if msg.decode() == 'sair':
            break
        dados = msg.decode().split("*")
        n1Aux = dados[0].split(",")
        n2Aux = dados[1].split(",")
        n3Aux = dados[2].split(",")
        
        n1 = float(n1Aux[0])
        n2 = float(n2Aux[0])
        n3 = float(n3Aux[0])
        
        if len(n1Aux) > 1:
            n1 += (float(n1Aux[1]) /100)  
        if len(n2Aux) > 1:
            n2 += (float(n2Aux[1])/100)
        if len(n3Aux) > 1: 
            n2 += (float(n3Aux[1])/100)
        
        media = (n1 + n2)/2

        reply = ""
        if media >= 7: 
            reply = "Aluno aprovado" 
        elif media < 7 and media >= 3:
                if ((media + n3)/2) >= 5:
                      reply = "Aluno aprovado" 
                else:
                     reply = "Aluno reprovado" 
        else:
           reply = "Aluno reprovado" 
        
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
