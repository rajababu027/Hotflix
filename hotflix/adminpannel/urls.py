from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.loginDetail, name='Login'),
    path('signup', views.signupDetail, name='Signup'),
    # path('<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
    # path('contact/', views.contact_form, name='contact'),
    # path('signup/', views.signup, name='signup')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)