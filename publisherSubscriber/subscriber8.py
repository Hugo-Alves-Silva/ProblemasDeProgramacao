import zmq
#HOST = '192.168.40.189'
HOST = '127.0.0.1'
PORT = '9999'
context = zmq.Context()
s = context.socket(zmq.SUB) # create a subscriber socket
p = 'tcp://'+ HOST +':'+ PORT # how and where to communicate
s.connect(p) # connect to the server
s.setsockopt_string(zmq.SUBSCRIBE, 'SALDOS') # subscribe to TIME messages

while True: # Five iterations
    info = s.recv() # receive a message
    dados = info.decode().split("*")  
    saldoMedio = float(dados[1])
    credito = 0.0
        
    if saldoMedio >= 201 and saldoMedio <= 400:   
        credito +=  0.2 * saldoMedio
    elif saldoMedio >= 401 and saldoMedio <= 600:   
        credito +=  0.3 * saldoMedio
    elif saldoMedio >= 601:
        credito +=  0.4 * saldoMedio
    
    print(f"Saldo Médio: {saldoMedio:.2f}.")         
            
    if credito == 0:
        print(f"Nenhum crédito disponível.\n")
    else:    
        print(f"Crédito: {credito:.2f}\n")
