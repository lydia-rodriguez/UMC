from django.shortcuts import redirect, render
from django.utils import timezone
from .models import User_Request
from django.shortcuts import render, get_object_or_404
from .forms import User_Request_Form

# Create your views here.
def user_request_list(request):
	user_requests = User_Request.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
	return render(request, 'umc/user_request_list.html', {'user_requests':user_requests})

def user_request_detail(request, pk):
	user_request = get_object_or_404(User_Request, pk=pk)
	return render(request, 'umc/user_request_detail.html', {'user_request': user_request})
	
def user_request_new(request):
	if request.method == "POST":
		form = User_Request_Form(request.POST)
		if form.is_valid():
			user_request = form.save(commit=False)
			user_request.requestor_emp_id = request.POST['requestor_emp_id']
			user_request.user_emp_id = request.POST['user_emp_id']
			user_request.client_name = request.POST['client_name']
			user_request.save()
			return redirect('umc.views.user_request_detail', pk=user_request.id)
	else:
		form = User_Request_Form()
	return render(request, 'umc/user_request_new.html', {'form': form})
	
def user_request_edit(request, pk):
	user_request = get_object_or_404(User_Request, pk=pk)
	if request.method == "POST":
		form = User_Request_Form(request.POST, instance=user_request)
		if form.is_valid():
			user_request = form.save(commit=False)
			user_request.requestor_emp_id = request.POST['requestor_emp_id']
			user_request.user_emp_id = request.POST['user_emp_id']
			user_request.client_name = request.POST['client_name']
			user_request.save()
			return redirect('umc.views.user_request_detail', pk=user_request.id)
	else:
		form = User_Request_Form(instance=user_request)
	return render(request, 'umc/user_request_edit.html', {'form': form})
	
def user_request_remove(request, pk):
    user_request = get_object_or_404(User_Request, pk=pk)
    user_request.delete()
    return redirect('umc.views.user_request_list')
