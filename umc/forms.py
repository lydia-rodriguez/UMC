from django import forms
from .models import User_Request

class User_Request_Form(forms.ModelForm):

    class Meta:
        model = User_Request
        fields = ('requestor_emp_id', 'user_emp_id', 'client_name',)