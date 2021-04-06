from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns=[
    url(r'^$',views.index,name='index'),
    # url(r'^picture/(\d+)',views.image,name ='image'),
    # url(r'^image/(?P<category_name>\w+)/(?P<image_id>\d+)',views.single,name = 'single'),
    # url(r'^location/(?P<image_location>\d+)', views.location_filter, name='location_filter'),
    # url(r'^search/', views.search_image, name='search_image'),
    # url(r'^locations/', views.search_results, name='search_results'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
