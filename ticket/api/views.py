from rest_framework.viewsets import *
from ..models import Ticket, User

class TicketViewSet(ModelViewSet):
    serializer_class = ""
    queryset = Ticket.objects.all()
    pass

class UserViewSet(ModelViewSet):
    serializer_class=""
    queryset = User.objects.all()