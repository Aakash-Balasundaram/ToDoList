from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User, ChatMessage
from .serializers import UserSerializer, ChatMessageSerializer

class UserListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = User.objects.exclude(id=request.user.id)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class ChatHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, username):
        other_user = User.objects.get(username=username)
        messages = ChatMessage.objects.filter(
            (Q(sender=request.user) & Q(receiver=other_user)) |
            (Q(sender=other_user) & Q(receiver=request.user))
        )
        serializer = ChatMessageSerializer(messages, many=True)
        return Response(serializer.data)