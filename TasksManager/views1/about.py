# - * - Coding: utf -8 - * -
from django.shortcuts import render
from django.utils import timezone
from TasksManager.views import *

# View for about page.
def page(request):
	return render(request, "en/public/about.html",)
