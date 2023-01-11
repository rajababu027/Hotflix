from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from adminpannel.form import UserDetailsForm, Video_form
from .models import UserDetails, VideosDetails
from django.contrib.auth.decorators import login_required
import os



def videoDetailsUpload(request):
    # all_video=VideosDetails.objects.all()
    if request.method == "POST":    
        form=Video_form(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Your Video Details has Successfully Uploaded <br><br><a href='/videoUpload' class='btn btn-success'>Go to Back</a>")
    else:
        form=Video_form()
    return render(request,'video_upload.html', {'form':form})
                # return HttpResponse("Your Video Details has Successfully Uploaded <br><br><a href='/home' class='btn btn-success'>Go to Home</a>")
       



def loginDetail(request):
    if request.method == 'POST':
        Email_Phone = request.POST.get('eamil_Phone')
        password = request.POST.get('password')
        if UserDetailsForm is not None:
            for userlogin in UserDetails.objects.all():
                if userlogin.email == Email_Phone and userlogin.password == password:
                    print(userlogin.name)
                    print(userlogin.email)
                    print(userlogin.phone)
                    return redirect('/home')
            return HttpResponse("Your eamil or password is incorrect........<br><br><a href='/' class='btn btn-success'>Go to Login</a>")
    return render(request,'login.html')



            # else:
            #     return HttpResponse("Your eamil or password is incorrect")
            
                # return render(request,'home.html',)
                # if user is not None:
            #         # login(request,user)
            #     return redirect('/home')
            # #     # return HttpResponse("Your eamil or password is incorrect")
            # return HttpResponse("Your eamil or password is incorrect")
        # user = authenticate(request, username=email_data, password=password_data)
        # if user is not None:
        #     login(request,user)
        #     return redirect('/home')
        # return HttpResponse("Your eamil or password is incorrect")
    # return render(request,'login.html',)



def signupDetail(request):
    if request.method == 'POST':
        Name = request.POST.get('name')
        Phone_Number = request.POST.get('Phone_Number')
        Email = request.POST.get('email')
        Pass = request.POST.get('pass')
        My_signupDetails = UserDetails(Name,Name,Phone_Number,Email,Pass)
        My_signupDetails.save()
        # return HttpResponse("You have ")
        return redirect('/')
    return render(request,'signup.html',)
    


def AdminsignupDetail(request):
    if request.method == 'POST':
        # Name = request.POST.get('name')
        Phone_Number = request.POST.get('Phone_Number')
        Email = request.POST.get('email')
        Pass = request.POST.get('pass')
        print("-------------------------------")
        print(Phone_Number,Email,Pass)
        print("-------------------------------")
        My_signupDetails = User.objects.create_user(Phone_Number,Email,Pass)
        My_signupDetails.save()
        # return HttpResponse("You have ")
        return redirect('/')
    return render(request,'signup.html',)



def AdminloginDetail(request):
    if request.method == 'POST':
        Eamil_Phone = request.POST.get('eamil_Phone')
        password = request.POST.get('password')
        user = authenticate(request, username=Eamil_Phone, password=password)
        print("-------------------------------")
        print(Eamil_Phone,password)
        print(user)
        print("-------------------------------")
        if user is not None:
            login(request,user)
            return redirect('/home')
        return HttpResponse("Your eamil or password is incorrect")
    return render(request,'login.html',)

    

@login_required(login_url='/')
def home(request):
    all_videos_data = VideosDetails.objects.all()
    return render(request,'home.html',{'all':all_videos_data})  



def Logoutpage(request):
    logout(request)
    return redirect('/')


def Dashboard(request):
    return render(request,'dashboard.html')

def videoList(request):
    all_videos_data = VideosDetails.objects.all()
    return render(request,'videolist.html',{'all':all_videos_data}) 


def delete(request, id):
  VideoDelete = VideosDetails.objects.get(id=id)
  VideoDelete.delete()
  return HttpResponseRedirect(reverse('videoList'))


def update(request, id):
  mymember = VideosDetails.objects.get(id=id)
  template = loader.get_template('videoUpdate.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
   

def updaterecord(request, id):
    member = VideosDetails.objects.get(id=id)
    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(member.video) > 0:
                os.remove(member.video.path)
                member.video = request.FILES['video']
                
            elif len(member.trailer) > 0:
                os.remove(member.trailer.path)
                member.trailer = request.FILES['trailer']
                
       
        title = request.POST['title']
        year = request.POST['year']
        description = request.POST['description']
        genre = request.POST['genre']
        Type = request.POST['type']
        # image = request.POST['image']
        # video = request.POST['video']
        # member = VideosDetails.objects.get(id=id)
        member.title = title
        member.year = int(year)
        member.description = description
        member.type = Type
        member.genre = genre
        # member.image = image
        member.save()
        # message.success(request, "Your Video has Successfully updated")
        return redirect('/videoList')
    return HttpResponseRedirect(reverse('videoList'))

def videoDetailsUpload(request):

    if request.method == 'POST':
        videoData = VideosDetails()
        videoData.image = request.FILES.get('image')
        videoData.titleImage = request.FILES.get('titleImage')
        videoData.thumbnailImage = request.FILES.get('thumbnailImage')
        videoData.title = request.POST.get('title')
        videoData.description = request.POST.get('description')
        videoData.year = request.POST.get('year')
        videoData.genre = request.POST.get('genre')
        videoData.type = request.POST.get('type')
        videoData.trailer = request.FILES.get('trailer')
        videoData.video = request.FILES.get('video')

        # My_signupDetails = VideosDetails(image,image,title_image,thumbnail_image,title,description,Year,Genre,type,trailer,video)
        videoData.save()
        # return HttpResponse("You have ")
        return HttpResponse("Your Video Details has Successfully Uploaded <br><br><a href='/videoUpload' class='btn btn-success'>Go to Back</a>")
    return render(request,'video_upload.html')






     # return render(request,'video_upload.html')



        
        #     return HttpResponse("<h1> Upload success</h1>")
        # else:
    #     #     video_form = VideosDetailsForm()
    # return render(request,'dashboard.html')






















# class PostList(generic.ListView):
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = 'blog/index.html'  # a list of all posts will be displayed on index.html


# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'blog/post_detail.html'  # detail about each blog post will be on post_detail.html


# def contact_form(request):
#     form = ContactForm()
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = f'Message from {form.cleaned_data["name"]}'
#             message = form.cleaned_data["message"]
#             sender = form.cleaned_data["email"]
#             recipients = ['thekodechamp@gmail.com']
#             try:
#                 send_mail(subject, message, sender, recipients, fail_silently=True)
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found')
#             return HttpResponse('Success...Your email has been sent')
#     return render(request, 'blog/contact.html', {'form': form})


# def signup(request):
#     if request.method == 'POST':
#         form = UserCreateForm(request.POST)
#         if form.is_valid():
#             new_user = form.save()
#             new_user = authenticate(
#                 username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password1']
#             )
#             login(request, new_user)
#             return redirect('home')
#     else:
#         form = UserCreateForm()
#     return render(request, 'registration/signup.html', {'form': form})
