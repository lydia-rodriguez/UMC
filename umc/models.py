from django.db import models
from django.utils import timezone



class User_Request(models.Model):
	Administrators = 'Administrators'
	Developers = 'Developers'
	DevelopersNew = 'DevelopersNew'
	Users = 'Users'
	USER_GROUP_CHOICES = ((Administrators, 'Administrators'),
						(Developers, 'Developers'),
						(DevelopersNew, 'DevelopersNew'),
						(Users, 'Users'))
	
	requestor_emp_id = models.CharField(max_length=50)
	requestor_first_name = models.CharField(max_length=50)
	requestor_last_name = models.CharField(max_length=50)	
	requestor_email = models.CharField(max_length=50)
	user_emp_id = models.CharField(max_length=50)
	user_first_name = models.CharField(max_length=50)
	user_last_name = models.CharField(max_length=50)
	user_email = models.EmailField(max_length=50)
	user_password = models.CharField(max_length=50)
	user_groups = models.CharField(max_length=20, choices=USER_GROUP_CHOICES)
	client_name = models.CharField(max_length=50)
	created_date = models.DateTimeField(default=timezone.now)

def __str__(self):
        return self.user_emp_id