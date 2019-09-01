from django.conf.urls import url,include
from . import views

urlpatterns = [
    # url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^$', views.index, name="home"),
     url(r'^signup/$', views.signup, name='signup'),
    url(r'^accounts/profile/',  views.profile, name="myProfile"),
    url(r'^user/(\d+)', views.user_profile, name='userProfile'),
    url(r'^image/(\d+)', views.single_post, name='singleImage'),
    url(r'^single_image/likes/(\d+)', views.single_image_like, name="singleImageLike"),
    
      # url(r'^login/$', views.login, name='login'),
    # url(r'^logout/$', views.logout, name='logout'),
]