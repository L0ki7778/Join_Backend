from rest_framework.viewsets import *
from ..models import Ticket, User
from .serializers import TicketSerializer,UserSerializer

class TicketViewSet(ModelViewSet):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()
    

class UserViewSet(ModelViewSet):
    serializer_class=UserSerializer
    queryset = User.objects.all()
    