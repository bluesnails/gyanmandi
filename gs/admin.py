from django.contrib import admin
from .models import Question, Choice, Answer, Author, Post

# Register your models here.

class ChoiceForm(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionForm(admin.ModelAdmin):
	inlines = [
		ChoiceForm,
	]

class AuthorForm(admin.ModelAdmin):
	pass
	
class PostForm(admin.ModelAdmin):
	pass

admin.site.register(Author, AuthorForm)
admin.site.register(Question, QuestionForm)
admin.site.register(Post, PostForm)
