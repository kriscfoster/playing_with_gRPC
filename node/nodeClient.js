const grpc = require('grpc');

const messages = require('./generated/helloworld_pb');
const services = require('./generated/helloworld_grpc_pb');

const PORT = process.argv[2];
const NAME = process.argv[3];

const client = new services.GreeterClient(`localhost:${PORT}`,
	grpc.credentials.createInsecure());

const request = new messages.HelloRequest();
request.setName(NAME);

client.sayHello(request, function(err, response) {
  console.log(response.getMessage());
});
