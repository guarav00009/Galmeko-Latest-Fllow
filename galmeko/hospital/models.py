from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.

class Hospital(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    hospital_name = models.CharField(max_length=100,blank=False,null=False)
    phone = models.CharField(max_length=15, blank=True, null=True)
    registration_no = models.CharField(max_length=30, unique=True)
    address = models.CharField(max_length=150,blank=False,null=False)
    STATUS_CHOICES = (
        (0, 'Pending'),
        (1, 'Active'),
        (2, 'Rejected'),
        (3, 'Deleted'),
    )
    status = models.IntegerField(
        _('status'), choices=STATUS_CHOICES, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Hospital'
        verbose_name_plural = 'Hospital'

    def __str__(self):
        return self.hospital_name