import zmq
#HOST = '192.168.40.189'
HOST = '127.0.0.1'
PORT = '9999'
context = zmq.Context()
s = context.socket(zmq.SUB) # create a subscriber socket
p = 'tcp://'+ HOST +':'+ PORT # how and where to communicate
s.connect(p) # connect to the server
s.setsockopt_string(zmq.SUBSCRIBE, 'PESO') # subscribe to TIME messages

while True: # Five iterations
    info = s.recv() # receive a message
    dados = info.decode().split('*')  
    altura = float(dados[1])
    sexo = dados[2]
    
    if sexo == 'masculino':
        peso = (72.7 * altura) - 58
    else:
        peso = (62.1 * altura) - 44.7
    
    print(f'Peso ideal: {peso:.2f}')
