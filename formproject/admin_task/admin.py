from django.contrib import admin

# Register your models here.
from .models import emp


class emp_admin(admin.ModelAdmin):
    list_display = ['e_name','e_id','email','pas']

admin.site.register(emp,emp_admin)