from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

from django.shortcuts import render
def login(request):
	c= {}
	c.update(csrf(request))
	return render_to_response('mysite/login.html', c)

def auth_view(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user = auth.authenticate(username=username,password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
	return render_to_response('mysite/loggedin.html',
		{'full_name':request.user.username})

def invalid_login(request):
	return render_to_response('mysite/invalid_login.html')

def logout(request):
	auth.logout(request)
	return render_to_response('mysite/logout.html')

def register_employer(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.groups.add(Group.objects.get(name='employer'))
            return HttpResponseRedirect("/accounts/register_employer_success")
    else:
        form = UserCreationForm()
    return render(request, "mysite/register.html", {
        'form': form,
    })
def register_user(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            
            return HttpResponseRedirect("/accounts/register_success")
    else:
        form = UserCreationForm()
    return render(request, "mysite/register.html", {
        'form': form,
    })
'''
	if request.method == 'POST':

		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/register_success')

	args = {}
	args.update(csrf(request))
	args['form'] = UserCreationForm()
	print args
	return render_to_response('mysite/register.html',args)

def register_user(request):
    args = {}
    args.update(csrf(request))

    if request.method == 'POST':
    	x = 1/0
        form = UserCreationForm(request.POST)
        args['form'] = form
        #if form.is_valid():           
        form.save()
        x = 1/0
        return HttpResponseRedirect('/accounts/register_success')
            
    else:
    	
        args['form'] = UserCreationForm()   

    return render_to_response('mysite/register.html', args)#, context_instance=RequestContext(request))
'''
def register_success(request):
	return render_to_response('mysite/register_success.html')

