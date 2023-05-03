from django.urls import path, re_path
from . import views

app_name = 'instagram'

urlpatterns = [
    path('', views.post_list),
    path('<int:pk>/',views.post_detail),
    # re_path(r'(?P<pk>\d+)/$', views.post_detail), ( 정규 표현식, 위와 같은 경로 )
    path('archives/<int:year>/', views.archives_year),
    re_path(r'archives/(?P<year>20\d{2})/$', views.archives_year), # 20xx년도를 주소에 기입했을때만 반응하도록
]
