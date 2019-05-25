from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from potato.models import Post,Comment,Profile,Event
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.views.generic import ListView,UpdateView,DetailView
from potato.forms import PostForm,EventForm,UserForm,ProfileForm

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the potato index.")

def about_view(request):
    return render(request, 'potato/about_us.html')

def help_view(request):
    return render(request, 'potato/help.html')

def policy(request):
    return render(request, 'potato/policy.html')

def home_view(request):
    post_list = Event.objects.all()
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

class UserUpdateView(UpdateView):
    model = Profile
    fields = '__all__'
    template_name='potato/user-update.html'

    '''def get_context_data(self,*args,**kwargs):
        context=super(UserUpdateView,self).get_context_data(*args,**kwargs)
        user = self.request.GET['profile']
        print(user.info)
        context['User']= User.objects.get(username=user)
        return context'''


def lk(request):
    #author = User.objects.get(username=author)
    if request.user.is_authenticated():
        author = request.user      
        profile = Profile.objects.get(user=author.id)
        
        
        if request.POST:
            print('create')
            print(request.POST)
            '''form = UserForm(request.POST)
            print(form)
            if form.is_valid():   
                user = form.save(commit='false')      
                user.save()'''
            author.first_name = request.POST['first_name']
            author.last_name = request.POST['last_name']
            author.email = request.POST['email']
            author.save()

            profile.age = request.POST['age']
            profile.info = request.POST['info']
            profile.save()
            
        form = UserForm(instance=author)
        form1 = ProfileForm(instance=profile)
        context = {'author':author,'form':form,'form1':form1}
        response = render(request,'potato/lk.html',context=context)
  
    return response

def post_user(request,author='g'):
    author = User.objects.get(username=author)
    post_list = Event.objects.filter(author=author.id)    # получаем все ивенты которые создал челик
    profile = Profile.objects.get(user=author.id)
    event_list = Event.objects.filter(participant=author.id) # получаем все ивенты на которые идет челик


    context = {'author':author,'post_list':post_list,'profile':profile,'event_list':event_list}
    response = render(request,'potato/userpost.html',context=context)

    return response


def get_post(request,pk='1'):
        event = Event.objects.get(pk=pk)     
        if request.POST:
            print(request.POST)
            if 'comment' in request.POST:
                print("комментарий")
                text = request.POST['comment']
                author = User.objects.get(username = request.user)
                comment = Comment.objects.create(author=author,text=text,event=event)
                comment.save()
        list_comment = Comment.objects.filter(event=pk)
        context = {'list_comment':list_comment,'post':event,'kol':event.participant.count()}
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
        age = request.POST['age']
        info = request.POST['info']

        user = User.objects.create_user(username = username,email = email,password=  password)
        user.first_name = first_name
        user.save()

        profile= Profile()
        profile.user=user
        profile.age = age
        profile.info = info
        profile.save()
        response = HttpResponseRedirect('/')
    return response

def post_create(request):
    context={}
    form = EventForm()
    context['form'] = form
    response = render(request,'potato/post-create.html',context)
    if request.POST:
        print('create')
        form = EventForm(request.POST)
        if form.is_valid():
            print(form)
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
        
        event = Event.objects.get(pk=request.POST['id'])       
        author = User.objects.get(username = request.user)
        if author in event.participant.all():
            print("dislike")
            event.save()
            event.participant.remove(author)
            event.thumbnumber = event.participant.count()
            event.save()

        else:
        #like1 = Like.objects.create(thumbnumber=post.likedone.thumbnumber+1)
        #like1.save()
        #like1.likedone.add(author)
        #post.likedone = like1
            print("like")
        
            event.save()
            event.participant.add(author)
            event.thumbnumber = event.participant.count()
            event.save()

        ls.append({'thumbnumber':event.participant.count()})
        return JsonResponse(ls,safe=False)
   
      
    #date= json.dumps(ls)
    return JsonResponse(ls,safe=False)


    


def exit(request):

    logout(request)
    response = HttpResponseRedirect('/')
    return response