from django.contrib import admin
from .models import FoodStall
from .models import Comment

#enables the admin (Food Swarm Team) to see the FoodStall records and Comment history
admin.site.register(FoodStall)
admin.site.register(Comment)

# Register your models here.
