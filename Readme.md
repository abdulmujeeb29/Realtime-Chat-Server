Realtime Chat Server using Django Rest Framework
================================================

This project implements a Realtime Chat Server utilizing Django Rest Framework (DRF). It offers functionalities for user authentication (login, signup, forgot password) and session management. The chat features include one-to-one and group chat capabilities with real-time communication enabled through WebSocket integration with Django Channels.

Table of Contents
-----------------

*   Installation
    
*   Usage
    
*   Endpoints
    
*   Authentication
    
*   Chat Functionality
    
*   WebSocket Integration
    
*   Frontend Testing
    
*   Contributing
    
*   License
    

Installation
------------

To set up the project locally, follow these steps:

1.  Bashgit clone https://github.com/topics/real-time-chat-appUse codeÂ [with caution.](https://gemini.google.com/faq#coding)content\_copy
    
2.  Bashpip install -r requirements.txtUse codeÂ [with caution.](https://gemini.google.com/faq#coding)content\_copy
    
3.  Bashpython manage.py migrateUse codeÂ [with caution.](https://gemini.google.com/faq#coding)content\_copy
    
4.  Bashpython manage.py runserverUse codeÂ [with caution.](https://gemini.google.com/faq#coding)content\_copy
    

Usage
-----

After starting the server, you can interact with the API endpoints using tools like cURL, Postman, or any HTTP client. Additionally, you can test the frontend functionality by opening the provided HTML/JS templates in your browser.

Endpoints
---------

The following endpoints are available in the API:

### Authentication

*   POST /api/register/: Register a new user.
    
*   POST /api/login/: Authenticate and obtain access and refresh tokens.
    
*   POST /api/token/refresh/: Refresh an expired access token.
    
*   POST /api/forgot-password/: Send instructions for resetting the password.
    
*   GET /api/check-session/: Check the status of the user's session.
    

### Chat

*   GET /api/messages//:Â Retrieve messages between the authenticated user and the specified recipient.
    
*   POST /api/messages/: Send a new message to a recipient.
    
*   GET /api/group-chats/: Retrieve all group chat rooms available in the system.
    
*   GET /api/group-chat-participants/: Retrieve all participants in group chat rooms.
    

Authentication
--------------

The authentication process involves user registration, login to obtain tokens (access & refresh), refreshing the access token upon expiration, and handling forgot password requests. The /api/check-session/ endpoint allows verifying the user's session status.

Chat Functionality
------------------

The chat functionality offers one-to-one and group chat options. One-to-one chat enables users to exchange messages in real-time with another user. Additionally, group chat functionality is available.

WebSocket Integration
---------------------

Real-time communication is achieved through WebSocket integration with Django Channels. WebSocket consumers manage WebSocket connections, message reception, and message broadcasting to other users in real-time.

Frontend Testing
----------------

A basic frontend setup is provided for testing purposes. Users can interact with the API using simple HTML/JS templates, focusing on functionality rather than user interface design.

