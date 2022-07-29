from django.contrib import admin
from django.urls import path
from stackersapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('party/', views.partyhome, name='partyhome'), 
     path('partydetail/<int:party_id>', views.partydetail, name='partydetail'),      

    
    path('develop/', views.home, name='home'), 
    path('detail/<int:develop_id>', views.detail, name='detail'),  # 아이디어 디벨롭/세부 페이지 
    path('modelformcreate/', views.modelformcreate, name='modelformcreate'), # 새로운 아이디어 추가
] 
# media 파일에 접근할 수 있는 url도 추가해주어야 함.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)