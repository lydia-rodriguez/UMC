from django.shortcuts import redirect, render
from django.utils import timezone
from .models import User_Request
from django.shortcuts import render, get_object_or_404
from .forms import User_Request_Form
from django.contrib.auth.decorators import login_required

import requests
import json

@login_required
def user_request_list(request):
	user_requests = User_Request.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
	return render(request, 'umc/user_request_list.html', {'user_requests':user_requests})

@login_required
def user_request_detail(request, pk):
	user_request = get_object_or_404(User_Request, pk=pk)
	return render(request, 'umc/user_request_detail.html', {'user_request': user_request})
	
def request_engine(user_request):
	user_info_dict = {
		'full_name': user_request.user_first_name + " " + user_request.user_last_name, 
		'user_email': user_request.user_email,
		'password': user_request.user_password,
		'groups': [user_request.user_groups], # list of groups user belongs to
		'username': user_request.user_last_name + user_request.user_first_name[0]
	}

	#base_url = 'http://10.1.177.27:8099' # url where request engine is located
	url = 'http://10.1.177.27:8099/vzw99999/ems/user/addUser/'# % (base_url)
	settings_origin_url = 'http://10.1.176.115' # Lydia laptop, temporary

	payload = {'callMethod': True,
			   'methodArgs': user_info_dict}

	headers = {'content-type': 'application/json',
				# 'origin': settings_origin_url, # settings_origin_url, where django project is located
				# 'referer': url, # request engine url, above
				'accept': 'application/json'}

	res = requests.post(url, verify=False, headers=headers, data=json.dumps(payload))

@login_required
def user_request_new(request):
	if request.method == "POST":
		form = User_Request_Form(request.POST)
		if form.is_valid():
			user_request = form.save(commit=False)
			user_request.requestor_emp_id = request.POST['requestor_emp_id']
			user_request.requestor_first_name = request.POST['requestor_first_name']
			user_request.requestor_last_name = request.POST['requestor_last_name']
			user_request.requestor_email = request.POST['requestor_email']
			user_request.user_emp_id = request.POST['user_emp_id']
			user_request.user_first_name = request.POST['user_first_name']
			user_request.user_last_name = request.POST['user_last_name']
			user_request.user_email = request.POST['user_email']
			user_request.user_password = request.POST['user_password']
			user_request.user_groups = request.POST['user_groups']
			user_request.client_name = request.POST['client_name']
			user_request.save()
			request_engine(user_request)
			return redirect('umc.views.user_request_detail', pk=user_request.id)
	else:
		form = User_Request_Form()
	return render(request, 'umc/user_request_new.html', {'form': form})


				
@login_required
def user_request_edit(request, pk):
	user_request = get_object_or_404(User_Request, pk=pk)
	if request.method == "POST":
		form = User_Request_Form(request.POST, instance=user_request)
		if form.is_valid():
			user_request.requestor_emp_id = request.POST['requestor_emp_id']
			user_request.requestor_first_name = request.POST['requestor_first_name']
			user_request.requestor_last_name = request.POST['requestor_last_name']
			user_request.requestor_email = request.POST['requestor_email']
			user_request.user_emp_id = request.POST['user_emp_id']
			user_request.user_first_name = request.POST['user_first_name']
			user_request.user_last_name = request.POST['user_last_name']
			user_request.user_email = request.POST['user_email']
			user_request.user_password = request.POST['user_password']
			user_request.user_groups = request.POST['user_groups']
			user_request.client_name = request.POST['client_name']
			user_request.save()
			return redirect('umc.views.user_request_detail', pk=user_request.id)
	else:
		form = User_Request_Form(instance=user_request)
	return render(request, 'umc/user_request_edit.html', {'form': form})

@login_required
def user_request_remove(request, pk):
    user_request = get_object_or_404(User_Request, pk=pk)
    user_request.delete()
    return redirect('umc.views.user_request_list')

