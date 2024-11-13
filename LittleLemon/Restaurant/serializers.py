from rest_framework.serializers import ModelSerializer
from .models import Menu, Booking

class MenuItemSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = ['Title', 'Price', 'Inventory']

class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = ['Name', 'No_of_guests', 'BookingDate']