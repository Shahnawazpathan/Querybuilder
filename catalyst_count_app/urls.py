from django.urls import path
from . import views


urlpatterns = [
  path('login/',views.user_login,name="user_login"),
  path('logout/',views.user_logout,name="user_logout"),
  path('' , views.csv_upload , name = "uploaddata"),
  path('Querybuilder/' , views.querybuilder , name = 'querybuilder'),
  path('userdata/' ,views.userdata , name = 'userdata'),
  path('useradd/', views.useradd , name = 'useradd' ),
  path('delete/', views.deletedata , name = 'delete' ),

]
    
