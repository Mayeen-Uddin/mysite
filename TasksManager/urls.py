from django.urls import path, re_path
from TasksManager.views import TasksManager

urlpatterns = [
	re_path(r'^$', TasksManager.page, name='home')
#	path('', views.TasksManager)
]