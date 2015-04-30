from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


from .models import Post
from .models import Question, Choice, Author, Answer
from .forms import QuestionForm
#from .forms import allPosts

# Create your views here.

def index(request):
	return render(request, 'index.html')

def about(request):
	return render(request, 'about.html')

def login_page(request):
	return render(request, 'Registration/login.html')

def aspirant_login(request):
	if request.method=='POST':
		username = request.POST['username']


def get_blog_posts(request):	
	return render(request, 'blogs.html', {'posts':posts})


@login_required(login_url='/admin/')
def add_ques(request):
	
	if request.method=='POST':
		form = QuestionForm(request.POST)
		print "here here"

		if form.is_valid():
			print "we came here"
			ques_text = form.cleaned_data['ques_text']
			ques_type = form.cleaned_data['ques_type']
			ques_dscore = form.cleaned_data['ques_dscore']
			ques_bloom = form.cleaned_data['ques_bloom']
			ques_sub  = form.cleaned_data['ques_sub']
			ques_ans = form.cleaned_data['ques_ans']
			
			ch1 = form.cleaned_data['ques_ch1']
			ch2 = form.cleaned_data['ques_ch2']
			ch3 = form.cleaned_data['ques_ch3']
			ch4 = form.cleaned_data['ques_ch4']
		
			print ques_text
			print ques_dscore
			print ques_bloom
			print ques_ans
			print ques_sub
			print ques_type

	
			ques_sol = form.cleaned_data['ques_sol']

			ques_tags = form.cleaned_data['ques_tags'].split(',')
			
			Q = question(ques_text=ques_text, 
			            ques_type=ques_type, 
			            ques_dscore=ques_dscore, 
			            ques_bloom=ques_bloom, 
			            ques_subject=ques_sub,
				    ques_author=author(user=request.user)
			     )
			Q.save()
			            
			choice1 = choice(choice_text=ch1, choice_ques=Q)
			choice1.save()
			choice2 = choice(choice_text=ch2, choice_ques=Q)
			choice2.save()
			choice3 = choice(choice_text=ch3, choice_ques=Q)
			choice3.save()
			choice4 = choice(choice_text=ch4, choice_ques=Q)
			choice4.save()		

			ch_ans = form.cleaned_data['ques_ans']
		        ans_choice_dict = {'ch1': choice1, 'ch2': choice2, 'ch3': choice3, 'ch4':choice4}
			ans = answer(answer_text=ques_sol, answer_ques=Q, answer_choice=ans_choice_dict[ch_ans])
			ans.save()
			
			for tag in ques_tags:
				tag = tag.strip()
				t = tags(tags_text=tag)
				t.save()
				tcon = tagcon(tagcon_tags=t, tagcon_ques=Q)
				tcon.save()
		
			print "we finally got here"	
			return HttpResponseRedirect(reverse('.views.index'))

		else:
			print "form not valid"
			print form.errors
	else:
		print "we shouldnt be here"
		form = QuestionForm()

	return render(request, 'addques.html', {'form':form})
