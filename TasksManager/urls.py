from django.urls import path, re_path
from TasksManager import views

urlpatterns = [
	re_path(r'^$', views.TasksManager, name='home')
#	path('', views.TasksManager)
]