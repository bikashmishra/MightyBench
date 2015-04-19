from django.http import Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from models import User
# Create your views here.

def index(request):
	if request.method == "POST":
		hclass = request.POST['hclass']
		return HttpResponseRedirect(reverse('startusup:results', kwargs = {'hclass_id':hclass}))
	return render(request, 'startusupapp/index.html')

def results(request, hclass_id):
	try:
		user = get_list_or_404(User, hclass=hclass_id)
		results = {'results': user}
		return render(request, 'startusupapp/index.html', results)
	except:
		return render(request, 'startusupapp/index.html')

def signup(request):
	if request.method == "POST":
		firstname = request.POST['firstname']
		lastname = request.POST['lastname']
		skills = request.POST['skills']
		hclass = request.POST['hclass']
		email = request.POST['email']
		githublink	= request.POST['githublink']
		linkedinlink = request.POST['linkedinlink']
		dribblelink = request.POST['dribblelink']
		user_object = User(firstname= firstname, lastname=lastname, hclass=hclass, skills=skills,
			email=email, githublink=githublink, linkedinlink=linkedinlink, dribblelink=dribblelink)
		user_object.save()
		return HttpResponseRedirect(reverse('startusup:index'))


	return render(request, 'startusupapp/signup.html')