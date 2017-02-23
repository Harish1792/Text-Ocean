from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.homeIndex,name='homeIndex'),
    url(r'^PasteText/',views.PasteText,name='PasteText'),
    url(r'^AboutUs/',views.AboutUs,name='AboutUs'),
    url(r'^Contact/',views.Contact,name='Contact'),
    url(r'^analyze/',views.upload_file,name='getText')

]
