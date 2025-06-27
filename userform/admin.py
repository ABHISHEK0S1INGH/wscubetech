from django.contrib import admin

from userform.models import UserForm

class UserFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')

admin.site.register(UserForm, UserFormAdmin)

# Register your models here.
