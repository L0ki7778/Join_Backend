from django.urls import path
from rest_framework import routers
from .views import TicketViewSet,UserViewSet

router = routers.SimpleRouter()
router.register(r'tickets', TicketViewSet)
router.register(r'user', UserViewSet)

urlpatterns = router.urls
