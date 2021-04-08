from django.conf.urls import url
from .views import UserRegisterView

urlpatterns=[
  url(r'registration/', UserRegisterView.as_view(), name='registration')
]


