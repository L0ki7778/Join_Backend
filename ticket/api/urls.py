from django.urls import path
from rest_framework import routers
from .views import TicketViewSet

router = routers.SimpleRouter()
router.register(r'tickets', TicketViewSet)

urlpatterns = router.urls
