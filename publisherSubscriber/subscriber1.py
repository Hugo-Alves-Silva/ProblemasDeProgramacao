import zmq
#HOST = '192.168.40.189'
HOST = '127.0.0.1'
PORT = '9999'
context = zmq.Context()
s = context.socket(zmq.SUB) # create a subscriber socket
p = 'tcp://'+ HOST +':'+ PORT # how and where to communicate
s.connect(p) # connect to the server
s.setsockopt_string(zmq.SUBSCRIBE, 'REAJUSTE') # subscribe to TIME messages

while True: # Five iterations
    info = s.recv() # receive a message
    dados = info.decode().split('*')  
    #print(dadosAux[0])
    salarioAux = dados[3].split('.')
    salario = float(salarioAux[0])
    if len(salarioAux) > 1:
        salario += float(salarioAux[1])/100.0
        
    if dados[2].lower() == 'operador' or dados[2].lower() == 'operadora':
        salario += salario * (20.0/100.0) 
    elif dados[2].lower() == 'programador'or dados[2].lower() == 'programadora':
        salario += salario * (18.0/100.0) 
       
    print(f"Nome: {dados[1]}")
    print(f"Salário: {salario:.2f}")
    print("")