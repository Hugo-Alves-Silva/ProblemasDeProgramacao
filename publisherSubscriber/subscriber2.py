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
    nome = dados[1]
    idade = int(dados[3])
    sexo  = dados[2].lower() 
    if sexo == 'masculino' and idade >= 18:
        print(f"{nome} é maior de idade.")    
    elif sexo == 'masculino' and idade < 18:
        print(f"{nome} não é maior de idade.")
    elif sexo == 'feminino' and idade >= 21:
        print(f"{nome} é maior de idade.")    
    elif sexo == 'feminino' and idade < 21: 
        print(f"{nome} não é maior de idade.")
    
