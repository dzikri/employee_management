from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView
from .views import UserProfileView

urlpatterns = patterns('',
   url(r'^$', TemplateView.as_view(template_name='base.html')),
   url(r'^(?P<slug>\w+)/$',
       UserProfileView.as_view(),
       name="profile"),
   url(r'^accounts/', include("registration.backends.simple.urls"))
)
