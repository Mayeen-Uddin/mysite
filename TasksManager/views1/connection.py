# - * - Coding: utf -8 - * -
from django.shortcuts import render
from django.utils import timezone

# View for connection page.

def page(request):
	return render(request, "en/public/connection.html",)
