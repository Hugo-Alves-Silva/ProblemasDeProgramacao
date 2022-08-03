import zmq, time
#HOST = '192.168.40.189'
HOST = '127.0.0.1'
PORT = '9999'
context = zmq.Context()
s = context.socket(zmq.PUB) # create a publisher socket
p = 'tcp://'+ HOST +':'+ PORT # how and where to communicate
s.bind(p) # bind socket to the address
pessoas = [
    ['João da Silva', 'masculino', 15], 
    ['Mario da Costa', 'masculino', 30],
    ['Pedro Silva Rodrigues', 'masculino', 5],
    ['Maria de Souza', 'feminino', 10],
    ['Ana Paula Faria', 'feminino', 35],
    ['Ana Luiza de Melo', 'feminino', 21],
    ['Victor Hugo Souza Silva', 'masculino', 18],
    ['Pedro Rodrigues Silva', 'masculino', 22]
]
while True:
    for i in pessoas:
        time.sleep(5) # wait every 5 seconds
        #s.send_string("TIME" + time.asctime()) # publish the current time
        s.send_string("MAIORIDADE*" + i[0]+ "*"+ i[1] +"*"+str(i[2]))
       
