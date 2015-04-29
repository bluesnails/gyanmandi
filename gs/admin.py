from django.contrib import admin
from .models import Question, Choice, Answer, Author

# Register your models here.

class questionform(admin.ModelAdmin):
	pass

class AuthorForm(admin.ModelAdmin):
	pass

admin.site.register(Author, AuthorForm)
admin.site.register(Question, questionform)
