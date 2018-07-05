from django.contrib import admin
from .models import Sections, Topics, Posts
# Register your models here.

admin.site.register(Sections)
admin.site.register(Topics)
admin.site.register(Posts)