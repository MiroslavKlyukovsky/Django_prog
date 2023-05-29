from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Club, Abonement, Day, User

admin.site.register(Club)
admin.site.register(Abonement)
admin.site.register(Day)
admin.site.register(User, UserAdmin)