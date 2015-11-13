from django.shortcuts import render
from django.utils import timezone
from .models import User_Request
from django.shortcuts import render, get_object_or_404

# Create your views here.
def user_request_list(request):
	user_requests = User_Request.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
	return render(request, 'umc/user_request_list.html', {'user_requests':user_requests})

def user_request_detail(request, pk):
	user_request = get_object_or_404(User_Request, pk=pk)
	return render(request, 'umc/user_request_detail.html', {'user_request': user_request})