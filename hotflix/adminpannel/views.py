from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from adminpannel.form import UserDetailsForm
from .models import UserDetails
from django.contrib.auth.decorators import login_required


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
            return HttpResponse("Your eamil or password is incorrect/<br><br><a href='/' class='btn btn-success'>Go to Login</a>")
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
    


def signupDetail(request):
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
    return render(request,'home.html')



def Logoutpage(request):
    logout(request)
    return redirect('/')


def dashboard(request):
    return render(request,'dashboard.html')





















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
