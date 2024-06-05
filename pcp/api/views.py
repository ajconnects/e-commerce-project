from typing import Any
from rest_framework import viewsets
from django.views.generic import TemplateView, CreateView
from .models import *
from .serializer import *
from .forms import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProgrammerProfileViewSet(viewsets.ModelViewSet):
    queryset = ProgrammerProfile.objects.all()
    serializer_class = ProgrammerProfileSerializer

class ClientProfileViewSet(viewsets.ModelViewSet):
    queryset = ClientProfile.objects.all()
    serializer_class = ClientProfileSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class AvailabilitySlotViewSet(viewsets.ModelViewSet):
    queryset = AvailabilitySlot.objects.all()
    serializer_class = AvailabilitySlotSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class TechnologyViewSet(viewsets.ModelViewSet):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer

class ProgrammerTechnologyViewSet(viewsets.ModelViewSet):
    queryset = ProgrammerTechnology.objects.all()
    serializer_class = ProgrammerTechnologySerializer

class ProjectTechnologyViewSet(viewsets.ModelViewSet):
    queryset = ProjectTechnology.objects.all()
    serializer_class = ProjectTechnologySerializer

class CalendarIntegrationViewSet(viewsets.ModelViewSet):
    queryset = CalendarIntegration.objects.all()
    serializer_class = CalendarIntegrationSerializer

class HomePageView(TemplateView):
    template_name = 'api/index.html'

    def get_context_data(self, **kwargs):
        content = super().get_context_data(**kwargs)
        return content

class AddProgrammerProfile(CreateView):
    model = ProgrammerProfile
    form_class = ProgrammerProfileForm
    template_name = 'api/programmer_form.html'

class AddClientProfile(CreateView):
    model = ClientProfile
    form_class = ClientProfileForm
    template_name = 'api/client_form.html'
