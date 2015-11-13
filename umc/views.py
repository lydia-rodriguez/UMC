from django.shortcuts import render
from django.utils import timezone
from .models import User_Request

# Create your views here.
def user_request_list(request):
	user_requests = User_Request.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
	return render(request, 'umc/user_request_list.html', {'user_requests':user_requests})

