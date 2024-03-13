from .views import * 
from django.urls import path 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    
)
from . import views

urlpatterns = [
    
    path('api/register/', RegisterUser.as_view(), name='register'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/check-session/', CheckSessionView.as_view(), name='check_session'),
    path('api/messages/<int:recipient_id>/', MessageListView.as_view(), name='messages'),
    path('api/messages/', SendMessageView.as_view(), name='send_message'),
    path('', LandingPageView.as_view(), name='landing_page'),
    path('one-to-one-chat/', OneToOneChatPageView.as_view(), name='one_to_one_chat_page'),
    path('group-chat/', GroupChatPageView.as_view(), name='group_chat_page'), 
    path('api/group-chats/', GroupChatListView.as_view(), name='group_chats_list'),
    path('api/group-chat-participants/', GroupChatParticipantListView.as_view(), name='group_chat_participants_list'),
    path('api/forgot-password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('api/users/', UserListView.as_view(), name='user_list'),

]
