# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)
    
class AboutPageView(TemplateView):
    template_name = "about.html"
    
class MyContactPage(TemplateView):
    template_name="contact.html"
    
class MyEducationDetails(TemplateView):
    template_name="education.html"

class MyCoursesDetails(TemplateView):
    template_name="courses.html"
    
class MyNewsAll(TemplateView):
    template_name="news.html"
    
class MyProjectDetails(TemplateView):
    template_name="project.html"
    
class MainPage(TemplateView):
    template_name="index1.html"
    
