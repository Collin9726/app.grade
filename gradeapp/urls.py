from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url(r'^$',views.index,name = 'index'),
    # url(r'^home/(\d+)',views.home,name = 'home'),
    url(r'^sendemail/$',views.send_email,name = 'send-email'),
    url(r'^createprofile/$',views.create_profile,name = 'create-profile'),
    url(r'^myprofile/$',views.my_profile,name = 'my-profile'),
    # url(r'^uploadimage/$',views.upload_image,name = 'upload-image'),
    # url(r'^deleteimage/(\d+)',views.delete_image,name = 'delete-image'),
    # url(r'^updatecaption/(\d+)',views.update_caption,name = 'update-caption'),
    # url(r'^changeprofilephoto/$',views.change_profile_photo,name = 'change-profile-photo'),
    # url(r'^deleteprofile/$',views.delete_profile,name = 'delete-profile'),
    # url(r'^search/$',views.search_profile,name = 'search-profile'),
    # url(r'^userprofile/(\d+)',views.user_profile,name = 'user-profile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)