import zmq, time
#HOST = '192.168.40.189'
HOST = '127.0.0.1'
PORT = '9999'
context = zmq.Context()
s = context.socket(zmq.PUB) # create a publisher socket
p = 'tcp://'+ HOST +':'+ PORT # how and where to communicate
s.bind(p) # bind socket to the address
funcionarios = [
    ['Pedro Alves Silva', 'A', 21000.5, 0],
    ['Pedro Pereira Rodrigues', 'B', 2000.2, 0],
    ['João Rodrigues de Oliveira', 'C', 5555.5, 0],
    ['Luana Machado Silva', 'D', 6666.6, 0],
    ['Luara Cortes', 'A', 20000.7, 2],
    ['Laura Silva Alves', 'B', 50000.0, 1],
    ['Eliara Pereira', 'C', 3000.0, 1],
    ['Agusto Costa', 'D', 10000.0, 1]
]

while True:
    for i in funcionarios:
        time.sleep(5) # wait every 5 seconds
        #s.send_string("TIME" + time.asctime()) # publish the current time
        s.send_string("FUNCIONARIOS*" + i[0]+"*"+i[1]+"*"+str(i[2])+"*"+str(i[3]))
       
