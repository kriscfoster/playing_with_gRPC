# playing_with_gRPC

## Node.js Helper

### Set up
```
$ cd node
$ npm install
```

### Running Server
`$ node server.js`
### Running Client
`$ node client.js <SERVER-PORT> <YOUR-NAME>`

## Python Helper

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

### Running
`$ python server.py`
`$ python client.py <SERVER-PORT> <YOUR-NAME>`
