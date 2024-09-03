from django.urls import path, include
from . import views
from rest_framework import routers
from myapp_drf.views import StudentViewSet

router = routers.DefaultRouter()
router.register(r'student', StudentViewSet)


urlpatterns = [
    # path('student/', views.home, name='home'),
    # path('student/<int:pk>', views.student_detail, name='student_detail'),
    path('', include(router.urls))
    
]