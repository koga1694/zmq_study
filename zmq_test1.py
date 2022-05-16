from socket import socket
from matplotlib.style import context
import zmq

# 버전 확인
print(zmq.pyzmq_version())

# zmq 라이브러리 기능 사용하기 전에 먼저 생성 되어야 한다.
context = zmq.Context()
print(type(context))

# zmq 소켓은 context를 통해 생성할 수 있다.
sockets = context.socket(zmq.REP)
print(type(sockets))