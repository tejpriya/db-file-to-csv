from django.urls import path,include
from con1 import views
urlpatterns = [
    path('create',views.create),
    path('insert',views.insert),
    path('index/',views.index),
    path('export/',views.export_users_csv),
]
