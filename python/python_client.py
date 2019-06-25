from __future__ import print_function
import sys
import grpc

import helloworld_pb2
import helloworld_pb2_grpc

def run(port, name):
    with grpc.insecure_channel('localhost: %s' % port) as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name=name))
    print(response.message)

if __name__ == '__main__':
	port = sys.argv[1]
	name = sys.argv[2]
	run(port, name)
