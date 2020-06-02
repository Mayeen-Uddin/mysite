# - * - Coding: utf -8 - * -
from django.shortcuts import render
from django.utils import timezone
#from django.http import HttpResponse
# Create your views here.
#def TasksManager(request):
#	return HttpResponse("Hello World")

# View for TasksManager(Home) page.
def page(request):
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