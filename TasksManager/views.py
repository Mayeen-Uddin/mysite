from TasksManager.models import Project, Task, Supervisor, Developer
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.db.models import Q
#from django.http import HttpResponse
# Create your views here.
#def TasksManager(request):
#	return HttpResponse("Hello World")

def TasksManager(request):
	my_variable = "View from variable!"
	years_old = 15
	array_city_capitale = [ "Dhaka", "Chottogram", "Rajshahi" ]
	my_hellow = "Hello World!"
	var1 = "variable view 1"
	var2 = "variable view 2"
	var3 = "variable view 3"
	var4 = "variable view 4"
	var5 = "variable view 5"
	return render(request, "en/public/home.html", {"my_var":my_variable, "years":years_old, "array_city":array_city_capitale, "my_hello":my_hellow, "variable1":var1, "variable2":var2, "variable3":var3, "variable4":var4, "variable5":var5, },)

def projects(request):
#	new_project1 = Project(title="System support", description="All system and peripherials.", client_name="UFL Employee")
#	new_project1.save()
#	new_project2 = Project(title="Network support", description="Network connectivity troubleshoot.", client_name="UFL Employee")
#	new_project2.save()
#	all_projects = Project.objects.all()
	action = 'Save relationship'
#	projects_to_me = Project.objects.filter(client_name="UFL", title="Network support")
#	first_record = Project.objects.get(id="8")
	queryset_project = Project.objects.filter(client_name="UFL").order_by("id")
#	first_item_queryset = queryset_project[:1]
#	project = first_item_queryset.get()
	project = Project.objects.filter(client_name="UFL").order_by("id")[:1].get().title
#	get_all_object = Task._meta.model.objects.all()  ## get all instance
#	new_supervisor = Supervisor(name="Mayeen Uddin", login="muddin2543", password="pass123", last_connection=timezone.now(), email="muddin2543@ulc.com", specialisation="Python")
#	new_supervisor.save()
#	new_developer = Developer(name="Rubel Mia", login="rmia", password="pass123", last_connection=timezone.now(), email="rmia@ulc.com", supervisors=new_supervisor)
#	new_developer.save()
#	project_to_link = Project.objects.get(id = 8)
#	new_task = Task(title="Adding relation", description="Example of adding relation and save it", time_elapsed=2, importance=0, project=project_to_link, developer=new_developer)
#	new_task.save()
#	return render(request, "en/public/projects.html", {"action":"Save datas of model", "all_projects": all_projects,})
	return render(request, "en/public/projects.html", locals())

def about(request):
	return render(request, "en/public/about.html",)

def connection(request):
	return render(request, "en/public/connection.html",)

def project_detail(request, pk):
	project = Project.objects.get(id=pk)
	return render(request, 'en/public/project_detail.html', {'project' : project})

def create_developer(request):
	error = False
	# If form has posted
	if request.POST:
		# This line checks if the data was sent in POST. If so, this means that the form has been submitted and we should treat it.
		if 'name' in request.POST:
		# This line checks whether a given data named name exists in the POST variables.
			name = request.POST.get('name', '')
			# This line is used to retrieve the value in the POST dictionary. Normally, we perform filters to recover the data to avoid false data, but it would have required many lines of code.
		else:
			error=True
		if 'login' in request.POST:
			login = request.POST.get('login', '')
		else:
			error=True
		if 'password' in request.POST:
			password = request.POST.get('password', '')
		else:
			error=True
		if 'supervisor' in request.POST:
			supervisor_id = request.POST.get('supervisor', '')
		else:
			error=True
		if not error:
			# We must get the supervisor
			supervisor = Supervisor.objects.get(id = supervisor_id)
			new_dev = Developer(name=name, login=login, password=password, supervisor=supervisor)
			new_dev.save()
			return HttpResponse("Developer added")
		else:
			return HttpResponse("An error has occured")
	else:
		supervisors_list = Supervisor.objects.all()
	return render(request, 'en/public/create_developer.html', {'supervisors_list':supervisors_list})