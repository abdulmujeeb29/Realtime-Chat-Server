# Realtime Chat Server using Django Rest Framework

This project implements a Realtime Chat Server using Django Rest Framework (DRF). It provides authentication functionalities such as login, signup, forgot password, and session management. The chat options include one-to-one chat and group chat, with real-time communication capabilities using WebSocket integration with Django Channels.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Authentication](#authentication)
- [Chat Functionality](#chat-functionality)
- [WebSocket Integration](#websocket-integration)
- [Frontend Testing](#frontend-testing)
- [Contributing](#contributing)
- [License](#license)

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/abdulmujeeb29/Realtime-Chat-Server.git
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Apply database migrations:

bash
Copy code
python manage.py migrate
Start the Django development server:

bash
Copy code
python manage.py runserver
Usage
After starting the server, you can access the API endpoints using tools like cURL, Postman, or any HTTP client. Additionally, you can test the frontend functionality by opening the provided HTML/JS templates in your browser.

Endpoints
The following endpoints are available in the API:

Authentication
POST /api/register/: Register a new user.
POST /api/login/: Authenticate and obtain access and refresh tokens.
POST /api/token/refresh/: Refresh an expired access token.
POST /api/forgot-password/: Send instructions for resetting the password.
GET /api/check-session/: Check the status of the user's session.
Chat
GET /api/messages/<recipient_id>/: Retrieve messages between authenticated user and the specified recipient.
POST /api/messages/: Send a new message to a recipient.
GET /api/group-chats/: Retrieve all group chat rooms available in the system.
GET /api/group-chat-participants/: Retrieve all participants in group chat rooms.
Authentication
The authentication process involves registering a new user, logging in to obtain access and refresh tokens, refreshing the access token when it expires, and handling forgot password requests. The /api/check-session/ endpoint allows users to verify their session status.

Chat Functionality
The chat functionality includes options for one-to-one and group chat. One-to-one chat allows users to exchange messages in real-time with another user, while group chat functionality is also available.

WebSocket Integration
Real-time communication is enabled using WebSocket integration with Django Channels. WebSocket consumers handle WebSocket connections, message reception, and message broadcasting to other users in real-time.

Frontend Testing
A very minimal frontend setup is provided for testing purposes. Users can interact with the API using simple HTML/JS templates, focusing on functionality rather than UI design.