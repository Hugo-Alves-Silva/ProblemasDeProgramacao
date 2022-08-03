import zmq
#HOST = '192.168.40.189'
HOST = '127.0.0.1'
PORT = '9999'
context = zmq.Context()
s = context.socket(zmq.SUB) # create a subscriber socket
p = 'tcp://'+ HOST +':'+ PORT # how and where to communicate
s.connect(p) # connect to the server
s.setsockopt_string(zmq.SUBSCRIBE, 'NOTAS') # subscribe to TIME messages

while True: # Five iterations
    info = s.recv() # receive a message
    dados = info.decode().split('*')  
    print()
    n1 = float(dados[1])
    n2 = float(dados[2])
    n3 = float(dados[3])
    
    m = ((n1+n2)/2)
    if m >= 7.0:
        print("Aprovado")
    elif m >3 and m < 7:
        if (m + n3)/2 >= 5:
            print("Aprovado")
        else:
            print("Reprovado")
    else:
        print("Reprovado")
   
