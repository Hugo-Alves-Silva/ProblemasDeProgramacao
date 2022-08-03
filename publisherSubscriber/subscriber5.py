import zmq
#HOST = '192.168.40.189'
HOST = '127.0.0.1'
PORT = '9999'
context = zmq.Context()
s = context.socket(zmq.SUB) # create a subscriber socket
p = 'tcp://'+ HOST +':'+ PORT # how and where to communicate
s.connect(p) # connect to the server
s.setsockopt_string(zmq.SUBSCRIBE, 'IDADES') # subscribe to TIME messages

while True: # Five iterations
    info = s.recv() # receive a message
    dados = info.decode().split('*')  
    idade = int(dados[1])
    if idade >= 5 and idade <= 7:
        print('infantil A')
    elif idade >= 8 and idade <= 10: 
        print('infantil B')
    elif idade >= 11 and idade <= 13:
        print('juvenil A')
    elif idade >= 14 and idade <= 17:
        print('juvenil B')
    elif idade >= 18:
        print('adulto')
