from django.contrib import admin

# Register your models here.
from Todo.models import TodoModel

admin.site.register(TodoModel)