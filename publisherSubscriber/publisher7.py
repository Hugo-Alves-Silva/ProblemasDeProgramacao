import zmq, time
#HOST = '192.168.40.189'
HOST = '127.0.0.1'
PORT = '9999'
context = zmq.Context()
s = context.socket(zmq.PUB) # create a publisher socket
p = 'tcp://'+ HOST +':'+ PORT # how and where to communicate
s.bind(p) # bind socket to the address
dados = [
    [23, 'masculino', 2],
    [65, 'masculino', 30],
    [45, 'masculino', 22],
    [20, 'feminino', 3],
    [25, 'feminino', 1],
    [60, 'feminino', 25]
]

while True:
    for i in dados:
        time.sleep(5) # wait every 5 seconds
        #s.send_string("TIME" + time.asctime()) # publish the current time
        s.send_string("APOSENTADORIA*" + str(i[0])+"*"+i[1]+"*"+str(i[2]))
       
