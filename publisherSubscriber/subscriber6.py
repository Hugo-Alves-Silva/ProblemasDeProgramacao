import zmq
#HOST = '192.168.40.189'
HOST = '127.0.0.1'
PORT = '9999'
context = zmq.Context()
s = context.socket(zmq.SUB) # create a subscriber socket
p = 'tcp://'+ HOST +':'+ PORT # how and where to communicate
s.connect(p) # connect to the server
s.setsockopt_string(zmq.SUBSCRIBE, 'FUNCIONARIOS') # subscribe to TIME messages

while True: # Five iterations
    info = s.recv() # receive a message
    dados = info.decode().split('*')  
    nome  = dados[1]
    nivel = dados[2]
    salarioBruto = float(dados[3])
    numeroDependentes = int(dados[4])   
    salarioLiquido = salarioBruto
    
    if nivel == 'A':
        if numeroDependentes > 0:
            salarioLiquido -=  (salarioBruto * (8/100))
        else:
             salarioLiquido -=  (salarioBruto * (3/100))
    elif nivel == 'B': 
        if numeroDependentes > 0:
             salarioLiquido -=  (salarioBruto * (10/100))
        else:
             salarioLiquido -=  (salarioBruto * (5/100))
    elif nivel == 'C':
        if numeroDependentes > 0:
             salarioLiquido -=  (salarioBruto * (15/100))
        else:
             salarioLiquido -=  (salarioBruto * (8/100))
    elif nivel == 'D':
        if numeroDependentes > 0:
             salarioLiquido -=  (salarioBruto * (17/100))
        else:
             salarioLiquido -=  (salarioBruto * (10/100))
    
    print(f"Nome: {nome}\nNível: {nivel}\nSalário líquido: {salarioLiquido:.2f}\n")
