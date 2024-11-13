from rest_framework.serializers import ModelSerializer
from .models import Menu

class MenuItemSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = ['Title', 'Price', 'Inventory']