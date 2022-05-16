import zmq
import time

# REQ/REP
'''
REQ socket은 많은 서버에 연결(connect) 할 수 있다.
REQ의 send()는 응답이 올 때까지 block된다.
REP의 recv()는 요청이 수신될 때 가지 block 된다.
'''

# REQ
context = zmq.Context()
sockets = context.socket(zmq.REQ)
sockets.connect('tcp://127.0.0.1:10101')

for i in range(10):
    print(f'{i}번째 시도')
    sockets.send_string('hello')
    print('recv : ' + sockets.recv_string())
    time.sleep(3)