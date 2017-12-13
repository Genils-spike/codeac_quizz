from django.conf.urls import url 

urlpatterns = [
   url(r'^/$', TemplateView.as_view(template_name='front/index.html')),
]