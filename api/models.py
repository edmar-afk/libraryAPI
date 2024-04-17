from django.db import models
from django.core.validators import FileExtensionValidator
import uuid
from django.utils import timezone
now = timezone.now()
currentDate = now.date()


class Librarian(models.Model):
    SITE_CHOICES = (
        ('Main', 'Main'),
        ('Canuto', 'Canuto'),
        ('Dumingag', 'Dumingag'),
        ('Pagadian', 'Pagadian'),
        
    )
    
    is_librarian_head = models.BooleanField(default=False)
    user_image = models.FileField(upload_to='media/', validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])],)
    name = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    facebook_link = models.CharField(max_length=1000)
    site = models.CharField(max_length=100, choices=SITE_CHOICES)
    
    def __str__(self):
        return f'Librarian - {self.name}'
 
class Visit(models.Model):
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=False)
    anonymous_uuid = models.UUIDField(null=True, blank=True, unique=True)

    @classmethod
    def create(cls, ip_address, user_agent, timestamp):
        anonymous_uuid = uuid.uuid4()
        return cls(ip_address=ip_address, user_agent=user_agent, anonymous_uuid=anonymous_uuid, timestamp=timestamp)
    
class Booking(models.Model):
    event = models.CharField(max_length=250)
    month = models.DateField()
    startDatetime = models.TimeField()
    endDatetime = models.TimeField()