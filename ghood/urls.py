from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('profile/<username>/edit/', views.edit_profile, name='edit-profile'),
#     path('profile/<username>', views.profile, name='profile'),
#     path('all-hoods/',views.neighbourhoods,name='hood'),
#     path('new-hood/', views.create_neighbourhood, name='new-hood'),
#     path('join_hood/<id>', views.join_neighbourhood, name='join-hood'),
#     path('leave_hood/<id>', views.leave_neighbourhood, name='leave-hood'),
#     path('single_hood/<hood_id>', views.single_neighbourhood, name='single-hood'),
#     path('<hood_id>/new-post', views.create_post, name='post'),
    
# ]


# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)