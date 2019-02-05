from django.conf.urls import url
from views import UserDetail, new_user

urlpatterns = [
    url(r'^detail/(?P<pk>\w+)/$', UserDetail.as_view(), name='user_detail'),
    url(r'^new/$', new_user, name="new_user"),
]
