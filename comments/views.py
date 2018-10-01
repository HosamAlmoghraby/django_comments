from django.shortcuts import render, redirect

from .models import Comment
# from .forms import CommentForm


def index(request):
  comments = Comment.objects.all()
  context = {
    'comments': comments
  }
  return render(request, 'comments/index.html', context)


# def submitForm(request):
#   if request.method == 'POST':
#     form = FormName(request.POST)
    
#     if form.is_valid():
#       new_submit = Comment.objects.create(title=request.POST['title'], body=request.POST['body'])
#       return redirect('index')
      
#     else:
#       form = FormName()
  
#   context = {'form': form}
#   return render(request, 'appName/submit.html', context)