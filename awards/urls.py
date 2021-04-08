from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^profile',views.profile,name = 'profile'),
    url(r'^project/(\d+)', views.project, name='project'),
    url(r'^$', views.review_list, name='review_list'),
    url(r'^review/(?P<review_id>[0-9]+)/$',
        views.review_detail, name='review_detail'),
    url(r'^new/project$', views.new_project, name='new-project'),
    url(r'^search/', views.search_projects, name='search_projects'),
    url(r'^edit_profile',views.edit_profile,name = 'edit-profile'),
    url(r'^new_profile/$',views.new_profile,name = 'new_profile'),
    url(r'^api/awmerch/$', views.MerchList.as_view()),
    url(r'^api/awproject/$', views.ProjectList.as_view()),
    url(r'api/merch/merch-id/(?P<pk>[0-9]+)/$',views.MerchDescription.as_view()),
    url(r'api/prod/prod-id/(?P<pk>[0-9]+)/$',views.ProductDescription.as_view()),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
