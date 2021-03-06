"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView
# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

#from TasksManager.views import TasksManager
from TasksManager.views import connection
from TasksManager.views import project_detail
from TasksManager.views import projects
from TasksManager.views import create_developer
from TasksManager.views import about


#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('TaskManager/', include('TaskManager.urls')),
#    path('', RedirectView.as_view(url='TaskManager/')),
#] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



urlpatterns = [
	path('admin/', admin.site.urls),
#	path('', views.index, name='index'),
	re_path(r'^about/?', about.page, name="about"),
	re_path(r'^connection-TasksManager$', connection.page, name="public_connection"),
	re_path(r'^projects-TasksManager$', projects.page, name="view_projects"),
	re_path(r'^project-detail-(?P<pk>\d+)$', project_detail.page, name="project_detail"),
	re_path(r'^create-developer$', create_developer.page, name="create_developer"),
]

urlpatterns += [
    path('TasksManager/', include('TasksManager.urls')),
]


urlpatterns += [
    path('', RedirectView.as_view(url='TasksManager/', permanent=True)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
