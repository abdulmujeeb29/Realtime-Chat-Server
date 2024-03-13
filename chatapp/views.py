from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics , status
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import UserSerializer , GroupChatSerializer, GroupChatParticipantSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import  *
from .serializers import MessageSerializer
from rest_framework.permissions import IsAuthenticated
from django.views.generic import TemplateView
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import send_mail
from django.urls import reverse

# Create your views here.
class LandingPageView(TemplateView):
    template_name = 'landing.html'

class OneToOneChatPageView(TemplateView):
    template_name = 'one_to_one_chat.html'

class GroupChatPageView(TemplateView):
    template_name = 'group_chat.html'

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RegisterUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CheckSessionView(generics.GenericAPIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request, *args, **kwargs):
        # Retrieve the user associated with the request
        user = request.user

        # Check if the user is authenticated
        if user.is_authenticated:
            # User is authenticated, session is valid
            return Response({"message": "Session is valid"}, status=status.HTTP_200_OK)
        else:
            # User is not authenticated, session is invalid
            return Response({"message": "Session is invalid"}, status=status.HTTP_401_UNAUTHORIZED)
        


class ForgotPasswordView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')

        # Check if the email exists in the database
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"message": "User with this email does not exist"}, status=status.HTTP_404_NOT_FOUND)

        # Generate a password reset token
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)

        # Construct the password reset link
        reset_url = reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})

        # Send password reset email to the user
        send_mail(
            'Password Reset',
            f'Click the following link to reset your password: {reset_url}',
            'from@example.com',
            [user.email],
            fail_silently=False,
        )

        return Response({"message": "Password reset instructions sent to your email"}, status=status.HTTP_200_OK)


#one to one chat functionality     

class MessageListView(generics.ListAPIView):
    queryset = Message.objects.all()  # Retrieve all messages from the database
    serializer_class = MessageSerializer  # Use MessageSerializer to serialize message objects
    permission_classes = [IsAuthenticated]  # Only allow authenticated users to access this endpoint

    def get_queryset(self):
        recipient_id = self.kwargs.get('recipient_id')  # Get the recipient ID from URL parameters
        # Retrieve messages between the authenticated user (sender) and the specified recipient
        return Message.objects.filter(recipient=self.request.user, sender_id=recipient_id)
    

class SendMessageView(generics.CreateAPIView):
    serializer_class = MessageSerializer  # Use MessageSerializer to deserialize incoming message data
    permission_classes = [IsAuthenticated]  # Only allow authenticated users to send messages

    def perform_create(self, serializer):
        # Automatically set the sender of the message to the authenticated user
        serializer.save(sender=self.request.user)


class GroupChatListView(generics.ListAPIView):
    queryset = GroupChat.objects.all()  # Retrieve all group chats from the database
    serializer_class = GroupChatSerializer  # Use GroupChatSerializer to serialize group chat objects
    permission_classes = [IsAuthenticated]  # Only allow authenticated users to access this endpoint

class GroupChatParticipantListView(generics.ListAPIView):
    queryset = GroupChatParticipant.objects.all()  # Retrieve all group chat participants from the database
    serializer_class = GroupChatParticipantSerializer  # Use GroupChatParticipantSerializer to serialize group chat participant objects
    permission_classes = [IsAuthenticated]  # Only allow authenticated users to access this endpoint


