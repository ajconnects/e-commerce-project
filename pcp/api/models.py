from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    is_programmer = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField()
    categories = models.ManyToManyField(Category, related_name='programmers', blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

class ProgrammerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='programmer_profile')
    skills = models.TextField()
    experience = models.IntegerField()  # Number of years
    bio = models.TextField()
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    portfolio = models.URLField(blank=True, null=True)
    certifications = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_profile')
    categories = models.ManyToManyField(Category, related_name='client_profiles')
    company_name = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class Booking(models.Model):
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)
    programmer = models.ForeignKey(ProgrammerProfile, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='pending')
    project_description = models.TextField()
    attachments = models.FileField(upload_to='attachments/', blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.client.user.username} booking with {self.programmer.user.username}"

class Review(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1 to 5 rating
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.booking.programmer.user.username} by {self.booking.client.user.username}"

class Payment(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')], default='pending')
    payment_method = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=100)

    def __str__(self):
        return f"Payment for {self.booking.id} - {self.status}"

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.sender.username} to {self.receiver.username}"

class AvailabilitySlot(models.Model):
    programmer = models.ForeignKey(ProgrammerProfile, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_booked = models.BooleanField(default=False)
    timezone = models.CharField(max_length=50)

    def __str__(self):
        return f"Slot for {self.programmer.user.username} from {self.start_time} to {self.end_time}"

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username} - {self.message[:20]}"

class Project(models.Model):
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Project: {self.title} by {self.client.user.username}"

class Application(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    programmer = models.ForeignKey(ProgrammerProfile, on_delete=models.CASCADE)
    cover_letter = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('submitted', 'Submitted'), ('reviewed', 'Reviewed'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='submitted')

    def __str__(self):
        return f"Application by {self.programmer.user.username} for {self.project.title}"

class Technology(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ProgrammerTechnology(models.Model):
    programmer = models.ForeignKey(ProgrammerProfile, on_delete=models.CASCADE)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.programmer.user.username} - {self.technology.name}"

class ProjectTechnology(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.project.title} - {self.technology.name}"

class CalendarIntegration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    provider = models.CharField(max_length=50)
    access_token = models.CharField(max_length=255)
    refresh_token = models.CharField(max_length=255, blank=True, null=True)
    token_expires = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} - {self.provider}"