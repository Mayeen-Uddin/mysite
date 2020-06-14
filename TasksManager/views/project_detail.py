# - * - Coding: utf -8 - * -
from django.shortcuts import render

# View for project_details page.
def page(request, pk):
	project = Project.objects.get(id=pk)
	return render(request, 'en/public/project_detail.html', {'project' : project})