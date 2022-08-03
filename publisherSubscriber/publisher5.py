import zmq, time
#HOST = '192.168.40.189'
HOST = '127.0.0.1'
PORT = '9999'
context = zmq.Context()
s = context.socket(zmq.PUB) # create a publisher socket
p = 'tcp://'+ HOST +':'+ PORT # how and where to communicate
s.bind(p) # bind socket to the address
idades = [5, 7, 9, 11, 12, 14, 15, 19, 22, 23, 34]

while True:
    for i in idades:
        time.sleep(5) # wait every 5 seconds
        #s.send_string("TIME" + time.asctime()) # publish the current time
        s.send_string("IDADES*" + str(i))
       
