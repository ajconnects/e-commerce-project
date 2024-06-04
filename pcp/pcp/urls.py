"""
URL configuration for pcp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import *


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'programmer_profiles', ProgrammerProfileViewSet)
router.register(r'client_profiles', ClientProfileViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'availability_slots', AvailabilitySlotViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'applications', ApplicationViewSet)
router.register(r'technologies', TechnologyViewSet)
router.register(r'programmer_technologies', ProgrammerTechnologyViewSet)
router.register(r'project_technologies', ProjectTechnologyViewSet)
router.register(r'calendar_integrations', CalendarIntegrationViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
