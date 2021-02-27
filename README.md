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

    TBD
