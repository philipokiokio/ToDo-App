from django.contrib import admin
from .models import Category,TodoItems
from django.contrib.auth.admin import UserAdmin

# from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.


admin.site.register(Category)



class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'body','completed']



admin.site.register(TodoItems,TodoAdmin)