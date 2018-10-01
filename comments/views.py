from django.shortcuts import render, redirect

from .models import Comment
from .forms import CommentForm


def index(request):
	comments = Comment.objects.all()

	context = {'comments': comments}

	return render(request, 'comments/index.html', context)


def submit(request):
	if request.method == 'POST':
		form = CommentForm(request.POST)

		if form.is_valid():
			new_submit = Comment.objects.create(title=request.POST['title'], body=request.POST['body'])
			return redirect('index')

	else:
		form = CommentForm()

	context = {'form': form}
	return render(request, 'comments/submit.html', context)
