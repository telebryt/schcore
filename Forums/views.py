from django.shortcuts import render, get_object_or_404,HttpResponse, HttpResponseRedirect,redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt 
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied
from .form import commentform,postform,UserProfileForm
from .models import PostModel,Comments,UserProfile



#home page
def index(request):
    template_name = "index.html"
    posts = PostModel.PostManager.all()  #for all post that has been published
    draftpost = PostModel.DraftManager.all()#for post that has been drafted
    return render(request, template_name, {"post": posts, "draft": draftpost})
    

#create post
def createpost(request):
    new_post = None
    template_name = "createpost.html"
    if request.method == "POST": 
        new_post = postform(data=request.data)
        if new_post.is_valid():
            new_post.save()
            return redirect("/")

    return render(request, template_name)        
        
#detail post
def detail_post(request, pk):
    template_name = "detail.html"
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
def edituserdetails(request, pk):
    user = User.objects.get(pk=pk)
    userform = UserProfileForm(instance=user)
    #create profile and also editting and validating every field sent
    profileinlineformset = inlineformset_factory(User, UserProfile, fields=("bio", "phone", "department", "faculty"))
    formset = profileinlineformset(instance=user)
    if request.user.is_authenticated() and request.user.id == user.id:
        if request.method == "POST":
            userform = UserProfileForm(request.POST, request.FILES, instance=user)
            formset = profileinlineformset(request.POST, request.FILES, instance=user)
            if userform.is_valid():
                created_user = userform.save(commit=False)
                formset = profileinlineformset(request.POST, request.FILES, instance=created_user)
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

                

#user registrations
@csrf_exempt
def registration(request, *args, **kwargs):
    template_name = "form/register.html"
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        username = request.POST["username"]

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already taken")
                return render(request, template_name)
                
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already taken")
                return render(request, template_name)
            else:
                User.objects.create_user(username=username, first_name=first_name,
                last_name=last_name, email=email, password=password1)
                return redirect("login")

        else:
            messages.info(request, "Password do not match")
            return render(request, template_name)

    else:
        return render(request, template_name)


#user login 
@csrf_exempt
def login(request, *args, **kwargs):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request.user)
            return redirect('home')
        else:
            messages.info(request, "Invalid Credentials")
            return render("login")
    else:
        return render(request,"form/login.html")                
        