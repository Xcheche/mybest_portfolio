from django.contrib import admin
from .models import About, Education, Experience, Service
# Register your models here.

admin.site.register(About)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Service)