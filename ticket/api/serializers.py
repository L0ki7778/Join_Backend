from rest_framework import serializers
from ..models import User, Ticket

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = '__all__'
            
        
class TicketSerializer(serializers.ModelSerializer):
    
    
    assignees = serializers.SerializerMethodField()
    
    class Meta:
        model=Ticket
        fields = '__all__'
        
    def get_assignees(self,obj):
        users = User.objects.filter(id__in=obj.assignees.all())
        return [user.name for user in users]
        