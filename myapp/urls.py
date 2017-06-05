from django.conf.urls import url
from myapp import views
urlpatterns = [
    
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^contact/$',views.MyContactPage.as_view()),
    url(r'^education/$',views.MyEducationDetails.as_view()),
    url(r'^courses/$',views.MyCoursesDetails.as_view()),
    url(r'^news/$',views.MyNewsAll.as_view()),
    url(r'^project/$',views.MyProjectDetails.as_view()),
    
    
]
