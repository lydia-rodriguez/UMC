from django.db import models
from django.utils import timezone

# Create your models here.
class User_Request(models.Model):
	requestor_emp_id = models.CharField(max_length=50)
	user_emp_id = models.CharField(max_length=50)
	client_name = models.CharField(max_length=50)
	created_date = models.DateTimeField(default=timezone.now)

def __str__(self):
        return self.user_emp_id