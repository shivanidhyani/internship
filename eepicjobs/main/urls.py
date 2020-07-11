from django.urls import path,include
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
				path('', views.index, name='index'),
                path('login/', views.login, name='login'),
                path('register/', views.register, name='register'),
                
                path('logout/', views.logout, name='logout'),
                path('home/', views.home, name='home'),
                ########### CURRENT URLS ##########################
                path('sendmsg/', views.addmsg, name='sendmsg'),
                path('jobpost/', views.jobpost_create, name='jobpost'),
                path('home/jobpost/', views.jobpost_create, name='jobpost'),
                path('viewmsg/', views.viewmsg, name='viewmsg'),
                path('search/', views.searchjob, name='search'),
                path('searchJob/', views.searchjobb, name='searchJob'),
                path('automotive/', views.automotive, name='automotive'),
                path('health/', views.health, name='health'),
                path('food/', views.food, name='food'),
                path('educationIndustry/', views.educationIndustry, name='educationIndustry'),
                path('designer/', views.designer, name='designer'),
                path('cutomerService/', views.cutomerService, name='cutomerService'),
                path('createresume/', views.createresume, name='createresume'),
                path('project/', views.project, name='project'),
                path('education/', views.education, name='education'),
                path('change_password/', views.change_password, name='change_password'),
                path('show/', views.show, name='show'),
                path('applyjob/<jid>', views.applyjob, name='applyjob'),
                path('applyjobb/<jid>', views.applyjobb, name='applyjobb'),
                path('showmyjobs/', views.showmyjobs, name='showmyjobs'),
                 path('empview/', views.empview, name='empview'),
                  path('employerview/', views.employerview, name='employerview'),
                path('dashboard/', views.dashboard, name='dashboard'),
                path('updateEmp/<str:pk>/', views.updateEmp, name='updateEmp'),
                path('dashboard/employer/', views.employerin, name='employerin'),
                path('dashboard/employer/Profile/update', views.employerup, name='employerup'),
                path('updateresume/<str:pk>/', views.updateresume, name='updateresume'),
                path('dashboard/employee/', views.employeein, name='employeein'),
                path('dashboard/employee/Profile/update', views.employeeup, name='employeeup'),
                path('dashboard/employee/Profile/view', views.employeev, name='employeev'),
                path('dashboard/employee/alerts', views.employeeal, name='employeeal'),
                path('dashboard/employee/Jobs/applied', views.employeeapp, name='employeeapp'),
                path('dashboard/employee/order', views.employeeor, name='employeeor'),
                path('dashboard/employee/package', views.employeepack, name='employeepack'),
                path('dashboard/employee/Jobs/saved', views.employeesa, name='employeesa'),
                path('dashboard/employee/Resume', views.employeeresume, name='employeeresume'),
                path('dashboard/employerdetails/', views.employerdetails, name='employerdetails'),
                path('checksubscription/',views.check_status,name='check_status'),
                 path('rr/', views.rr, name='rr'),
                  path('savedresume', views.saved_resume, name='saved_resume'),
                  path('subsform/',views.sub,name='sub'),
                  path('showapplicants/<str:jid>/', views.showapplicants, name='showapplicants'),
                 path('sendemail/', views.sendemail, name='sendemail'), 
                 path('sending/<str:apid>/', views.sending, name='sending'), 
                 path('seeing/<str:apid>/', views.seeing, name='seeing'), 
]