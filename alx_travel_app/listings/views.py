from .serializers import ListingSerializer, BookingSerializer
from .models import Listing, Booking
from rest_framework.viewsets import ModelViewSet

class ListingViewSet(ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer    
    