from mysite_app.models import *

def myinfo(request):
    myinfo = MyInfo.objects.first()
    return {'myinfo': myinfo }

def about(request):
    about = About.objects.first()
    return {'about': about }

def education_details(request):
     education_details = EducationDetail.objects.all()
     return {'education_details': education_details }

def exprience_details(request):
     exprience_details = ExprienceDetail.objects.all()
     return {'exprience_details': exprience_details }

def service_list(request):

    service_list = Services.objects.all()

    return {'service_list': service_list }

def blog_list(request):
    blog_list = Blog.objects.all().order_by('-id')

    return {'blog_list': blog_list }

