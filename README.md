# AiDa
AiDa an open source intelligent chatbot

# Phase [1] Completed... 
We now have an endpoint for web users and developers... 


### Terminal commands

    To run test: make tests

    To run application: make run

### Viewing the endpoints ###

    Open the following url on your browser to view swagger documentation
    http://127.0.0.1:5000/aida/ping for checksum 
    http://127.0.0.1:5000/aida/verify for verify end poin
    http://127.0.0.1:5000/aida/webhook for webhook


# TODO
- Make Chatbot Conversation.

# How to use AiDa API

1. Get your data ready in Json format. The require key needed is object and message. "object" takes the value "web" for a website or web platform... "message" takes the any string value.
# Example of the data 
{"object":"web", "message":message}
2. Send a request to this url https://maya-2019.herokuapp.com/ along with your json
3. Recieve response in json format.
Response should look like this
{"response":response, "user":"AiDa"}


# P.S: Currently we have put an hold to Social Media Intergrations until futher notice.

We are working to make it better......
