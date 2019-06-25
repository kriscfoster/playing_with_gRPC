# playing_with_gRPC

## Help with node.js

### Set up
```
$ cd node
$ npm install
```

### Running Server
`$ node server.js`
### Running Client
`$ node client.js <SERVER-PORT> <YOUR-NAME>`

## Help with python

### Set up
```
$ cd python
$ python -m pip install --upgrade pip
$ python -m pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ python -m pip install --upgrade pip
$ python -m pip install grpcio
$ python -m pip install grpcio-tools
```

### Running Server
`$ python server.py`
### Running Client
`$ python client.py <SERVER-PORT> <YOUR-NAME>`
