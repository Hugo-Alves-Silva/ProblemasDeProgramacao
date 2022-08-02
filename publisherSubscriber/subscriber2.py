import zmq
#HOST = '192.168.40.189'
HOST = '127.0.0.1'
PORT = '9999'
context = zmq.Context()
s = context.socket(zmq.SUB) # create a subscriber socket
p = 'tcp://'+ HOST +':'+ PORT # how and where to communicate
s.connect(p) # connect to the server
s.setsockopt_string(zmq.SUBSCRIBE, 'MAIORIDADE') # subscribe to TIME messages

while True: # Five iterations
    info = s.recv() # receive a message
    dados = info.decode().split('*')  
    maior = False
    idade = int(dados[3])
    if dados[2].lower() == 'masculino':
        if  
    elif dados[2].lower() == 'feminino':
        salario += salario * (18.0/100.0) 
       
    if()
    print(f"Nome: {dados[1]}")
    
    print(f"Salário: {salario:.2f}")
    print("")