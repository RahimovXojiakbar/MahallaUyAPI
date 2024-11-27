from django.urls import path
from .import views 
urlpatterns = [
    path('neighborhood/', views.NeighborhoodView.as_view(), name='neighborhood_url'),
    path('house/', views.HouseView.as_view(), name="house_url"),
    path('neighborhood_detail/<int:id>/', views.NeighborhoodDetaillView.as_view(), name='neighborhood_detail_url'),
    path('house_detail/<int:id>/', views.HouseDetailView.as_view(), name='house_detail_url' ),
]
