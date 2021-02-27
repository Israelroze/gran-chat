# Chat Server 

* [Running the chat server](#running-the-service-locally)
* [Running the chat client](# Running the Chat Client)

## Running the Chat Server
1. build the docker image from the following docker file:
gran-chat -> server -> Dockerfile
2. run the docker image
3. the server publishes 2 API's:
    | URL        | Method           | Request Body  | Description
    | ------------- |:-------------:| -----:| -----:|
    |*IP*:*Port*/chat      | POST | {'username':"Israel",'message':"Hi!"} | Send new message to chat
    |*IP*:*Port*/chat      | GET  |  None | Get all messages

## Running the Chat Client
To run the client, please execute the run.py under the client image with the following arguments:

"--username" your user name

"--target" the IP address of the server (OPTIONAL, default is 127.0.0.1)

"--port" the listening port of the server (OPTIONAL, default is 5000) 

The client will print all the message in the chat, to add a message press ctrl+c on the keyboard
