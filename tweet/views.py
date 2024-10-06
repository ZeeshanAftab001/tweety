from django.shortcuts import render,redirect,get_object_or_404
from .models import User,Profile,Tweet
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.utils.functional import SimpleLazyObject

# Create your views here.

@login_required 
def home(request):

    tweets = Tweet.objects.filter(user__profile__in=request.user.profile.follows.all())
    return render(request,'home.html',{"tweets":tweets})


def create_tweet(request):

    if request.method == "POST":

        title=request.POST.get("title")
        body=request.POST.get("body")

        tweet=Tweet(user=request.user)
        if title:
            tweet.title=title
        if body:
            tweet.title=title
        
        tweet.body=body

        tweet.save()
        return redirect("home")
    return render(request,"create_tweet.html",{})

def edit_tweet(request,id):
    tweet=get_object_or_404(Tweet,id=id)
    print(tweet.title)
    if request.method == "POST":
        body=request.POST.get("body")
        title=request.POST.get("title")
        print(body)

        tweet.title=title
        tweet.body=body

        tweet.save()
        messages.success(request,"Tweet Updated")
        return redirect('home')
    else:
        messages.error(request,"Error Occured")
    
    return render(request,'home.html',{})

def edit_tweet_page(request,id):

    tweet=get_object_or_404(Tweet,id=id)
    return render(request,"edit_tweet.html",{"tweet":tweet})

def delete_tweet(request,id):

    tweet=get_object_or_404(Tweet,id=id)
    tweet.delete()
    return redirect("home")
    

def signup(request):

    if request.method == "POST":

        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")

        user=User()
        user.username=username
        user.email=email
        user.set_password(password)

        user.save()
        login(request=request,user=user)
        return redirect("home") 

    return render(request,'signup.html',{})

    
def login_user(request):
        
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request=request,user=user)
            # Redirect to a success page.
            return redirect("home")
            
        else:
            messages.error(request, "Wrong Credentials. Please Try Again!")
    
    return render(request, 'login.html', {})

@login_required 
def logout_user(request):
    logout(request=request)
    return redirect("login")

@login_required 
def settings(request):
    return render(request,'settings.html',{})


@login_required 
def search(request):
    
    if request.method == "POST":
        item = request.POST.get("search")

        # Correctly traverse the relationship from Profile to User to filter by username
        profiles = Profile.objects.filter(user__username__icontains=item)
        tweets = Tweet.objects.filter( Q(body__icontains=item) | Q(title__icontains=item))
        if profiles or tweets:

            return render(request, 'profiles_list.html', {"profiles": profiles,"tweets":tweets})
        else:
            messages.error(request,"User  or Tweet Not Found")
            return render(request,"home.html")

    return render(request, "home.html", {})

@login_required 
def update_profile(request):

    if request.method == "POST" and request.FILES.get('image'):

        image = request.FILES.get('image')  # Get the uploaded image file
        username = request.POST.get('Username')  # Get the uploaded image file
        bio = request.POST.get('bio')  # Get the uploaded image file
        user = request.user
        if isinstance(user, SimpleLazyObject):
            user = user._wrapped  # This unwraps the actual user object

        # Assuming a Profile object is created for each user
        profile, created = Profile.objects.get_or_create(user=user)
        profile.picture = image
        profile.bio = bio
        profile.save()

        return redirect("settings")
    else:
        return render(request,'update_my_profile.html',{})
@login_required 
def update_credentails(request):
    if request.method == "POST":
        # Assuming you're getting username and email from a form
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Update the user instance
        user = request.user  # Get the logged-in user
        user.username = username
        user.password= password
        user.save()  # Save the updated user

        messages.success(request, "Your credentials have been updated successfully.")
        return redirect('settings')  # Redirect to a success page

    return render(request, "update_credentials.html", {})
    
@login_required
def my_profile(request):
    user=request.user
    profile=get_object_or_404(Profile,user=user)
    return render(request,"myprofile.html",{"profile":profile})

def user_profile(request, id):
    user = request.user
    profile = get_object_or_404(Profile, user__id=id)

    # Initialize current_profile before the if-else block
    current_profile = request.user.profile

    if request.method == 'POST':
        action = request.POST.get('UnFollow')

        if action == 'UnFollow':
            current_profile.follows.remove(profile)
        else:
            current_profile.follows.add(profile)
        
        current_profile.save()

    return render(request, 'end_user_profile.html', {"profile": profile})


def unfollow_user(request,id):
    user = request.user
    profile = get_object_or_404(Profile, user__id=id)

    current_profile = request.user.profile
    if request.method == 'POST':
        action = request.POST.get('UnFollow')

        if action == 'UnFollow':
            current_profile.follows.remove(profile)
        current_profile.save()
        return redirect("home")
    return redirect("home")
