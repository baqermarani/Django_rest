# Register your models here.
from django.contrib import admin

from .models import Person, Question, Answer

admin.site.register(Question)
admin.site.register(Answer)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email')
