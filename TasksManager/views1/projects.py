# - * - Coding: utf -8 - * -
from TasksManager.models import Project, Task, Supervisor, Developer
from django.shortcuts import render
from django.utils import timezone


# View for projects page.
def page(request):
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