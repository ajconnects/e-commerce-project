from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_programmer', 'is_client', 'phone_number', 'profile_picture', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        #fields =  '__all__'

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class ProgrammerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = ProgrammerProfile
        fields = ['user', 'skills', 'experience', 'bio', 'hourly_rate', 'availability', 'portfolio', 'certifications']

class ClientProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    categories = CategorySerializer(many=True, read_only=True)
    category_ids = serializers.PrimaryKeyRelatedField(
        many=True, write_only=True, queryset=Category.objects.all(), source='categories'
    )

    class Meta:
        model = ClientProfile
        fields = ['user', 'company_name', 'bio', 'website', 'categories', 'category_ids']
        #fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        category_ids = validated_data.pop('categories', [])

        user = User.objects.create(**user_data)
        client_profile = ClientProfile.objects.create(user=user, **validated_data)
        client_profile.categories.set(category_ids)

        return client_profile

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        category_ids = validated_data.pop('categories', [])

        user = instance.user
        for attr, value in user_data.items():
            setattr(user, attr, value)
        user.save()

        instance.categories.set(category_ids)
        return super().update(instance, validated_data)

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'client', 'programmer', 'start_time', 'end_time', 'status', 'project_description', 'attachments', 'notes']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'booking', 'rating', 'comment', 'timestamp']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'booking', 'amount', 'timestamp', 'status', 'payment_method', 'transaction_id']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'subject', 'content', 'timestamp', 'read']

class AvailabilitySlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailabilitySlot
        fields = ['id', 'programmer', 'start_time', 'end_time', 'is_booked', 'timezone']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'user', 'message', 'created_at', 'read']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'client', 'title', 'description', 'budget', 'deadline', 'created_at']

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'project', 'programmer', 'cover_letter', 'submitted_at', 'status']

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ['id', 'name']

class ProgrammerTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammerTechnology
        fields = ['id', 'programmer', 'technology']

class ProjectTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTechnology
        fields = ['id', 'project', 'technology']

class CalendarIntegrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalendarIntegration
        fields = ['id', 'user', 'provider', 'access_token', 'refresh_token', 'token_expires']