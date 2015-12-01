from django import forms
from .models import User_Request

class User_Request_Form(forms.ModelForm):

    class Meta:
        model = User_Request
        fields = ('requestor_emp_id', 'requestor_first_name', 'requestor_last_name', 'requestor_email', 'user_emp_id', 'user_first_name', 'user_last_name', 'user_email', 'user_password', 'user_groups', 'client_name',
		)