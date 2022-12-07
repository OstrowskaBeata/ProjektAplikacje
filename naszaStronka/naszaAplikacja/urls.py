from django.urls import path, include
from . import views

urlpatterns = [
    path('kierowca/', views.kierowca_list),
    path('kierowca/<int:pk>/', views.kierowca_detail),
    path('kierowca/<imie>/', views.kierowca_imie),
    path('kierowca/update/<int:pk>/', views.kierowca_update_delete),
    path('kierowca/delete/<int:pk>/', views.kierowca_update_delete),
    path('kierowca/kierowcy_add', views.kierowca_add),
    path('ciezarowki/', views.ciezarowki_list),
    path('ciezarowki/<int:pk>/', views.ciezarowki_detail),
    path('ciezarowki/ciezarowki_add', views.ciezarowki_add),
    path('ciezarowki/update/<int:pk>/', views.ciezarowki_update_delete),
    path('ciezarowki/delete/<int:pk>/', views.ciezarowki_update_delete),
    path('zlecenia/', views.zlecenia_list),
    path('zlecenia/<int:pk>/', views.zlecenia_detail),
    path('zlecenia/update/<int:pk>/', views.zlecenia_update_delete),
    path('zlecenia/delete/<int:pk>/', views.zlecenia_update_delete),
    path('zlecenia/kierowcy_add', views.zlecenia_add),
    path('api-auth/', include('rest_framework.urls')),
]