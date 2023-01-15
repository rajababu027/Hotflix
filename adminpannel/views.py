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

from rest_framework import generics

from .models import VideosDetails, UserDetails
from .serializers import VideoDetailsSerializer, UserDetailsSerializer




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





def signupDetail(request):
    if request.method == 'POST':
        userDetails = UserDetails()
        userDetails.name = request.POST.get('name')
        userDetails.phone = request.POST.get('Phone_Number')
        userDetails.email = request.POST.get('email')
        userDetails.password = request.POST.get('pass')
        print("--------------------------------------------")
        print(request.POST.get('name'), request.POST.get('Phone_Number'),request.POST.get('email'),request.POST.get('pass'))
        userDetails.save()
        print("--------------------------------------------")

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
        member.title = title
        member.year = int(year)
        member.description = description
        member.type = Type
        member.genre = genre
        # member.image = image
        member.save()
        return redirect('/videoList')
    return HttpResponseRedirect(reverse('videoList'))

def videoDetailsUpload(request):
    if request.method == 'POST':
        videoData = VideosDetails()
        videoData.titleImage = request.FILES.get('titleImage')
        videoData.thumbnailImage = request.FILES.get('thumbnailImage')
        videoData.title = request.POST.get('title')
        videoData.description = request.POST.get('description')
        videoData.year = request.POST.get('year')
        videoData.genre = request.POST.get('genre')
        videoData.type = request.POST.get('type')
        videoData.trailer = request.FILES.get('trailer')
        videoData.video = request.FILES.get('video')
        videoData.save()
        return HttpResponse("Your Video Details has Successfully Uploaded <br><br><a href='/videoUpload' class='btn btn-success'>Go to Back</a>")
    return render(request,'video_upload.html')




# API Views 

class VideoDetailsList(generics.ListCreateAPIView):
    queryset = VideosDetails.objects.all()
    serializer_class = VideoDetailsSerializer


class VideoDetailsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VideosDetails.objects.all()
    serializer_class = VideoDetailsSerializer


class UserDetailsList(generics.ListCreateAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsSerializer


class UserDetailsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsSerializer
