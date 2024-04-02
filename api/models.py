from django.db import models
from django.core.validators import FileExtensionValidator


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
 
class Visitors(models.Model):
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    anonymous_uuid = models.UUIDField(null=True, blank=True, unique=True)