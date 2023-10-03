from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import MatchingPost
from .forms import MatchingPostForm
from django.http import HttpResponseNotAllowed


# Create your views here.
def index(request):
    matching_posts = MatchingPost.objects.order_by('-create_date')
    context = {'matching_posts': matching_posts}
    return render(request, 'matching/matching_posts.html', context)

def detail(request, post_id):
    matching_post = get_object_or_404(MatchingPost, pk=post_id)
    context = {'matching_post': matching_post}
    return render(request, 'matching/matching_posts.html', context)

def post_create(request):
    if request.method == 'POST':
        form = MatchingPostForm(request.POST)
        if form.is_valid():
            matching_post = form.save(commit=False)
            matching_post.create_date = timezone.now()
            matching_post.save()
            return redirect('matching:index')
    else:
        form = MatchingPostForm()
    context = {'form': form}
    return render(request, 'matching/matching_postform.html', context)