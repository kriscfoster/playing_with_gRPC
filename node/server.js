const grpc = require('grpc');

const messages = require('./generated/helloworld_pb');
const services = require('./generated/helloworld_grpc_pb');

const PORT = 1996;

function sayHello(call, callback) {
  var reply = new messages.HelloReply();
  reply.setMessage(`Hello From Node.js, ${call.request.getName()}!`);
  callback(null, reply);
}

const server = new grpc.Server();

server.addService(services.GreeterService, { sayHello });
server.bind(`localhost:${PORT}`, grpc.ServerCredentials.createInsecure());
server.start();

console.log(`Node gRPC Server Listening on ${PORT}!`);
