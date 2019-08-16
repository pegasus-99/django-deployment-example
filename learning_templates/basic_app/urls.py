from django.urls import path
from basic_app import views

app_name = 'basicapp'

urlpatterns = [

    path('relative/',views.relative_url_templates,name='relative'),
    path('other/',views.other,name='other')

]
