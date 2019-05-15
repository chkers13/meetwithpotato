from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from potato.models import Post,Comment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.views.generic import ListView,UpdateView,DetailView
from potato.forms import PostForm,EventForm

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the potato index.")

def home_view(request):
    post_list = Post.objects.all()
    user = request.user

    context = {'post_list':post_list,'user':user}

    response = render(request,'home.html',context=context)
    return response

class PostDetailView(DetailView):
    model = Post
    def get_comment(**kwargs):
       list_comment=Comment.objects.filter(post=3)
       context={'list_comment':list_comment}
       return context
  
    
def post_user(request,author='g'):
    author = User.objects.get(username=author)
    post_list = Post.objects.filter(author=author.id)    
    

    context = {'author':author,'post_list':post_list}
    response = render(request,'potato/userpost.html',context=context)
    return response

    
def get_post(request,pk='1'):
        post = Post.objects.get(pk=pk)       
        if request.POST:
            print(request.POST)
            if 'comment' in request.POST:
                print("комментарий")
                text = request.POST['comment']
                author = User.objects.get(username = request.user)
                comment=Comment.objects.create(author=author,text=text,post=post)
                comment.save()
        list_comment=Comment.objects.filter(post=pk)
        context={'list_comment':list_comment,'post':post}
        response = render(request,'potato/post-detail.html',context)
        return response
    
def login_view(request):

    
    response = render(request,'potato/login.html')
    if 'username' in  request.POST and 'password' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        #context = {'username':username,'password':password}
        #response = render(request,'potato/login.html',context)  
        
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
            # Redirect to a success page.
            else:
            # Return a 'disabled account' error message
                ...
        else:
            pass
        response = HttpResponseRedirect('/')
    return response

def registration(request):
    response = render(request,'potato/registration.html')
    if 'username' in  request.POST and 'password' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        user = User.objects.create_user(username = username,email = email,password=  password)
        user.first_name = first_name
        user.save()
        response = HttpResponseRedirect('/')
    return response

def post_create(request):
    context={}
    form = EventForm()
    context['form'] = form
    response = render(request,'potato/post-create.html',context)
    if request.POST:
        form = PostForm(request.POST)
        if form.is_valid():
           
            event = form.save(commit='false')
            author = User.objects.get(username = request.user)
            event.author = author
            event.save()
            response = HttpResponseRedirect('/')
      
    return response

def like_json(request):
    print("json")
    ls = []
    if request.POST:
        
        post = Post.objects.get(pk=request.POST['id'])       
        author = User.objects.get(username = request.user)
        if author in post.likedone.all():
            print("dislike")
            post.thumbnumber=post.likedone.count()-1
            post.save()
            post.likedone.remove(author)

        else:
        #like1 = Like.objects.create(thumbnumber=post.likedone.thumbnumber+1)
        #like1.save()
        #like1.likedone.add(author)
        #post.likedone = like1
            print("like")
            post.thumbnumber=post.likedone.count()+1
            post.save()
            post.likedone.add(author)
        ls.append({'thumbnumber':post.thumbnumber})
        return JsonResponse(ls,safe=False)
   
      
    #date= json.dumps(ls)
    return JsonResponse(ls,safe=False)


    


def exit(request):

    logout(request)
    response = HttpResponseRedirect('/')
    return response