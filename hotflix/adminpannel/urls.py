from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import VideoDetailsList, VideoDetailsDetail,UserDetailsList, UserDetailsDetail

urlpatterns = [
    path('', views.loginDetail, name='Login'),
    path('signup', views.signupDetail, name='Signup'),
    path('home', views.home, name='Home'),
    path('logout', views.Logoutpage, name='logout'),
    path('dashboard', views.Dashboard, name='dashboard'),
    path('videoUpload', views.videoDetailsUpload, name='videoDetailsUpload'),
    path('videoList', views.videoList, name='videoList'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('video/', VideoDetailsList.as_view()),
    path('video/<int:pk>/', VideoDetailsDetail.as_view()),
    path('user/', UserDetailsList.as_view()),
    path('user/<int:pk>/', UserDetailsDetail.as_view()),
    # path('<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
    # path('contact/', views.contact_form, name='contact'),
    # path('signup/', views.signup, name='signup')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)