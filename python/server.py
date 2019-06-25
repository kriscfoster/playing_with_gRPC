from concurrent import futures
import time
import grpc

import helloworld_pb2
import helloworld_pb2_grpc

DAY_IN_SECONDS = 60 * 60 * 24
PORT = 1997;


class Greeter(helloworld_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        return helloworld_pb2.HelloReply(message='Hello From Python, %s!' % request.name)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:%s' % PORT)
    server.start()
    print 'Python gRPC server listening on: %s!' % PORT
    time.sleep(DAY_IN_SECONDS)

if __name__ == '__main__':
    serve()
