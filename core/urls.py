from django.urls import path
from . import views

urlpatterns = [
    path('', views.WineListView.as_view(), name='wine_list'),
    path('wine/<int:pk>/', views.WineDetailView.as_view(), name='wine_detail'),
    path('wine/<int:pk>/vota/', views.vota_wine, name='vota_wine'),
    path('import/', views.import_wines, name='import_wines'),
    path('top/', views.TopWineView.as_view(), name='top_wines'),
]
