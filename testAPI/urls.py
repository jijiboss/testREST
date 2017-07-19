from django.conf.urls import url
from django.contrib import admin
#make the URL compatible for API
from rest_framework.urlpatterns import format_suffix_patterns
from testAPP import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^products/$', views.ProductList.as_view()),
]

#http://www.django-rest-framework.org/api-guide/format-suffixes/
#urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns = format_suffix_patterns(urlpatterns, allowed = ['json', 'html', 'xml'])
