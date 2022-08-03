import zmq
#HOST = '192.168.40.189'
HOST = '127.0.0.1'
PORT = '9999'
context = zmq.Context()
s = context.socket(zmq.SUB) # create a subscriber socket
p = 'tcp://'+ HOST +':'+ PORT # how and where to communicate
s.connect(p) # connect to the server
s.setsockopt_string(zmq.SUBSCRIBE, 'APOSENTADORIA') # subscribe to TIME messages

while True: # Five iterations
    info = s.recv() # receive a message
    dados = info.decode().split('*')  
    idade = int(dados[1])
    sexo = dados[2]
    tempo = int(dados[3])
    flag = False 
    if sexo == 'masculino':
        if idade >= 65 and tempo >= 30 :
            flag = True 
    else:
        if idade >= 60 and tempo >= 25: 
            flag = True
            
    if flag:
        print("O funcionário pode se aposentar.\n")
    else:    
        print("O funcionário ainda não pode se aposentar.\n")
