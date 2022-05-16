import zmq
import time

# Pub/Sub

'''
특징
- Pub socket의 경우 연결된 SUB가 없는 경우 메세지는 버려진다.
- Sub의 경우 반드시 setsocket()를 사용하여 subscroption을 설정해야 한다.
- Sub 소켓을 먼저 바인드(bind)하고 나중에 Sub 소켓을 연결(connect)하면 Sub 소켓은 오래된 메세지를 받을 수 없게 된다.
  그러므로 가능하면 Pub은 바인드(bind), Sub는 연결(connect) 하는 것이 가장 좋다.

Pub가 바인딩 후 즉시 메세지를 전송하면, Sub는 데이터를 수신 못할 가능성이 있다.
이를 위해서 Sub가 연결하고 준비되기까지 데이터를 발송하지 않도록 동기화 하는 방법을 제공한다.

ZMQ의 PUB-SUB Pattern 특징
- 하나의 Sub는 한 개 이상의 Pub에 연결할 수 있다.
- Sub가 없다면 모든 Pub의 메세지는 유실된다.
- Sub에서만 메세지 필터링이 가능하다.
'''

# Pub
context = zmq.Context()
sockets = context.socket(zmq.SUB)
sockets.connect('tcp://127.0.0.1:10100')
sockets.setsockopt_string(zmq.SUBSCRIBE, '') # 모든 메세지를 받는다.

for i in range(10):
    print(f'{i}번째 시도')
    print(sockets.recv_string())