import zmq, time
#HOST = '192.168.40.189'
HOST = '127.0.0.1'
PORT = '9999'
context = zmq.Context()
s = context.socket(zmq.PUB) # create a publisher socket
p = 'tcp://'+ HOST +':'+ PORT # how and where to communicate
s.bind(p) # bind socket to the address
pessoas = [
    ['João da Silva','operador', 2000.0], 
    ['Mario da Costa','programador', 3000.0],
    ['Pedro Silva Rodrigues', 'programador', 5500.50],
    ['Maria de Souza','médica', 10000.0],
    ['Ana Paula Faria','operadora', 3500.0]
]
while True:
    for i in pessoas:
        time.sleep(5) # wait every 5 seconds
        #s.send_string("TIME" + time.asctime()) # publish the current time
        s.send_string("REAJUSTE*" + i[0]+ "*"+ i[1] +"*"+str(i[2]))
       