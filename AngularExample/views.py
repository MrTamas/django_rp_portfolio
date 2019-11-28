from django.shortcuts import render

# Create your views here.
def angular_index(request):
	#angular = AngularExample.objects.all()
	#context = {
	#	'AngularExample': angular
	#}
	return render(request, 'angular_index.html') #context
