from django.shortcuts import render
from django.views.generic import CreateView
from django.http import HttpResponse, HttpResponseRedirect
from .models import Comment
from .form import CommentForm
from django.urls import reverse_lazy

class AddComment(CreateView):
    latest_comment_list = Comment.objects.order_by('-id')[:10]# новый
    model = Comment
    form_class = CommentForm
    template_name = 'index.html'
    success_url = reverse_lazy('index')

# Create your views here.
def index(request):
    counter = len(Comment.objects.all())
    latest_comment_list = Comment.objects.order_by('-id')[:10]
    return render(request, 'index.html', {'latest_comment_list': latest_comment_list, 'counter': counter})
    
def leave_comment(request):
    c = Comment(comment_text = request.POST['comment_text'], author_name = request.POST['author_name'], photo = request.FILES['photo'])
    c.save()
    return HttpResponseRedirect(reverse_lazy('index'))
    