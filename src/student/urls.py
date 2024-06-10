from django.urls import path
from django.views.generic.base import RedirectView
from .views import *

urlpatterns = [
    path('', StudentListView.as_view() , name='students_list'),
    path('signup/', StudentSignUp.as_view(), name='student_sign_up'),
    path('signin/', StudentSignIn.as_view(), name='student_sign_in'),
    path('<int:pk>/', AcademicInfo.as_view(), name='academic_info'),
    path('<int:pk>/change/', ChangeStudentProfile.as_view(), name='change_student_profile'),
    path('<int:pk>/studentprofile/', RedirectView.as_view(url='../#student-profile'), name='student_profile'),
    path('semesterreportcard/<int:pk>/change/', ChangeSemesterReportCard.as_view(), name='change_semester_report_card'),
]