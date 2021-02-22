from django.shortcuts import render,get_object_or_404
from .form import commentform,postform
from .models import Post,Comments
# Create your views here.
def PostList(request):
    template_name = "index.html"
    posts = Post.PostManager.all()
    return render(request, template_name, {"post": posts})
    
def CreatePost(request):
    new_post = None
    if request.method == "POST":
        new_post = postform(data=request.data)
        if new_post.is_valid():
            new_post.save(commit=True)
            
        

def Detail_Post(request, pk):
    template_name = "postdetail.html"
    post = get_object_or_404(Post, pk=pk)
    comments = post.comment.filter(active=True)
    new_comment = None

    #creating comment
    if request.method == 'POST':
        comment_form = commentform(data=request.POST)
        if comment_form.is_valid():
            #create comment but dont save in the database yet
            new_comment = comment_form.save(commit=False)
            #assign the post to the comment in the database
            new_comment.post = post
             #now go ahead and save
            new_comment.save()
    else:
        comment_form = commentform()
    return render(request, template_name, {'post': post,
    'comments': comments,
     new_comment: "new_comment",
    comment_form :"comment_form" })             
