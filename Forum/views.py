from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied
from .form import commentform,postform,UserProfileForm
from .models import PostModel,Comments,UserProfile




def index(request):
    template_name = "index.html"
    posts = Post.PostManager.all()
    return render(request, template_name, {"post": posts})
    
def createpost(request):
    new_post = None
    template_name = "createpost.html"
    if request.method == "POST": 
        new_post = postform(data=request.data)
        if new_post.is_valid():
            new_post.save(commit=True)
            
            return redirect("/")

    return render(request, template_name)        
        

def detail_post(request, pk):
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

@login_required #required login before taking any actions
def editUserdetails(request, pk):
    user = User.objects.get(pk=pk)
    userform = UserProfileForm(instance=user)

    ProfileInlineFormset = inlineformset_factory(User, UserProfile, fields=("bio", "phone", "department", "faculty"))
    formset = ProfileInlineFormset(instance=user)

    if request.user.is_authenticated() and request.user.id == user.id:
        if request.method == "POST":
            userform = UserProfileForm(request.POST, request.FILES, instance=user)
            formset = ProfileinlIneFormset(request.POST, request.FILES, instance=user)
            if userform.is_valid():
                created_user = userform.save(commit=False)
                formset = ProfileinlIneFormset(request.POST, request.FILES, instance=created_user)
                if formset.is_valid():
                    created_user.save()
                    formset.save()
                    return HttpResponseRedirect('account/profile')

        return render(request, "account/accountUpdate.html", {"userPk": pk
        , "user_form": userform,
        "formset": formset
        })

    else:
        raise PermissionDenied       

                
