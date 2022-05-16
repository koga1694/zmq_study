import sys
import time
import zmq

'''
특징
- PUSH socket은 연결이 존재하지 않을 때 send()하게 되면 연결될 때까지 블록(block)된다.
- 전달된 메세지는 연결된 socket에 round robin 된다.
- Worker는 ventilator에 PULL로 연결(connect)되어 있고, sink와는 PUSH로 연결(Connect) 되어 있다. 이것은 Worker 는 임의로 추가 할 수 있다는 것을 의미한다.
만약 worker 가 바인딩(bind) 되어 있다면 worker 가 추가 될 때마다 매번 ventilator와 sink에 더 많은 소켓이 필요하다. 이 구조에서 ventilator와 sink 는 stable part, worker는 dynamic part 라 부른다.
- ventilator의 PUSH 소켓은 균등하게 Worker에 작업을 분배한다. (load-balancing)
- Sink의 PULL 소켓은 균등하게 Worker로 부터 결과를 수집한다. (fair-queuing)

PUSH, PULL의 bind, connect 는 상황에 따라 유용한 패턴이 있다.
- PUSH - bind, PULL - connect 의 경우는 동시 처리를 위한 Producer-Consumer 패턴에 적합
- PUSH - connect, PULL - bind 의 경우 처리 데이터를 한곳으로 집중 시켜 모을 때
'''

# sink

context = zmq.Context()

# 소켓에서 메세지를 받음
receiver = context.socket(zmq.PULL)
receiver.bind('tcp://127.0.0.1:10103')

s = receiver.recv()

tstart = time.time()

total_msec = 0
for task_nbr in range(100):
    s = receiver.recv()
    if task_nbr % 10 == 0:
        sys.stdout.write(':')
    else:
        sys.stdout.write('.')
    sys.stdout.flush()

tend = time.time()
print('Total elapsed time: %d msec' % ((tend-tstart)*1000))