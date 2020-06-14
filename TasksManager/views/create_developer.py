# - * - Coding: utf -8 - * -
from TasksManager.models import Project, Task, Supervisor, Developer
from django.shortcuts import render
from django.http import HttpResponse
from django import forms

# View for create_developer page.
# def page(request):
# 	error = False
# 	# If form has posted
# 	if request.POST:
# 		# This line checks if the data was sent in POST. If so, this means that the form has been submitted and we should treat it.
# 		if 'name' in request.POST:
# 		# This line checks whether a given data named name exists in the POST variables.
# 			name = request.POST.get('name', '')
# 			# This line is used to retrieve the value in the POST dictionary. Normally, we perform filters to recover the data to avoid false data, but it would have required many lines of code.
# 		else:
# 			error=True
# 		if 'login' in request.POST:
# 			login = request.POST.get('login', '')
# 		else:
# 			error=True
# 		if 'password' in request.POST:
# 			password = request.POST.get('password', '')
# 		else:
# 			error=True
# 		if 'supervisor' in request.POST:
# 			supervisor_id = request.POST.get('supervisor', '')
# 		else:
# 			error=True
# 		if not error:
# 			# We must get the supervisor
# 			supervisor = Supervisor.objects.get(id = supervisor_id)
# 			new_dev = Developer(name=name, login=login, password=password, supervisors=supervisor)
# 			new_dev.save()
# 			return HttpResponse("Developer added")
# 		else:
# 			return HttpResponse("An error has occured")
# 	else:
# 		supervisors_list = Supervisor.objects.all()
# 	return render(request, 'en/public/create_developer.html', {'supervisors_list':supervisors_list})
# This line imports the Django forms package
class Form_inscription(forms.Form):
	# This line creates the form with four fields. It is an object that inherits from forms.Form. It contains
	# attributes that define the form fields.
	name = forms.CharField(label="Name", max_length=30)
	login = forms.CharField(label="Login", max_length=30)
	password = forms.CharField(label="Password", widget=forms.PasswordInput)
	supervisor = forms.ModelChoiceField(label="Supervisor", queryset=Supervisor.objects.all())
# View for create_developer
def page(request):
	if request.POST:
		form = Form_inscription(request.POST)
		# If the form has been posted, we create the variable that will contain our form filled with data sent by POST
		# form.
		if form.is_valid():
		# This line checks that the data sent by the user is consistent with the field that has been defined in the
		# form.
			name = form.cleaned_data['name']
		# This line is used to retrieve the value sent by the client. The collected data is filtered by
		# the clean() method that we will see later. This way to recover data provides secure data.
			login = form.cleaned_data['login']
			password = form.cleaned_data['password']
			supervisor = form.cleaned_data['supervisor']
		# In this line, the supervisor variable is of the Supervisor type, that is to say that the returned data
		# by the cleaned_data dictionary will directly be a model.
			new_developer = Developer(name=name, login=login, password=password, email="", supervisors=supervisor)
			new_developer.save()
			return HttpResponse("Developer added")
		else:
			return render(request, 'en/public/create_developer.html', {'form' : form})
		# To send forms to the template, just send it like any other variable. We send it in case the form
		# is not valid in order to display user errors:
	else:
		form = Form_inscription()
	# In this case, the user does not yet display the form, it instantiates with no data inside.
		return render(request, 'en/public/create_developer.html', {'form': form})