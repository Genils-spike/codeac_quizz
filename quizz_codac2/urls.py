from django.conf.urls import url, include
from backoffice import views
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', views.index.as_view()),
	url(r'^logout/$', views.LogoutView.as_view()),
	url(r'^backoffice/$', login_required(TemplateView.as_view(template_name='backoffice/index.html'))),
]