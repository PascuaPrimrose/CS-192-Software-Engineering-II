from django.shortcuts import render
from .models import FoodStall

# Create your views here.
#defines the views available in the application; what is displayed/where it goes
def home(request):
	foodstalls = {
		'foodstalls': FoodStall.objects.all()
	}
	return render(request, 'FoodSwarm/home.html', foodstalls)

def comments(request):
	comments = {
		'comments': Comment.objects.all()
	}
	return render(request, 'FoodSwarm/home.html', comments)


def about(request):
	return render(request, 'FoodSwarm/about.html', {'title': 'About'})