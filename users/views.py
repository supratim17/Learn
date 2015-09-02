from django.shortcuts import render
from forms import RegistrationForm
from django.views import generic

class RegisterView(generic.DetailView):
	template_name = 'users/register.html'
	model = 'User'

	def register(request):
	    if request.method == "GET":
	        return render(request, 'users/register.html')
	    if request.method == "POST":
	        form = RegistrationForm(data = request.POST)
	        if form.is_valid():
	            user = form.save(False)
	            user.set_password(user.password)
	            user.save()
	            user = authenticate(username=user.username, password=request.POST['password1'])
	            login(request, user)
	            return redirect('/')