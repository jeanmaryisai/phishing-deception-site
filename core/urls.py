from django.urls import path
from. import views  # Import the views module from the cor app.

urlpatterns = [
    path('', views.home, name='home'),
    # path('konesans',views.konesans, name='konesans'),
    # path('konesans/create', views.create, name='create'),
    # path('konesans/results', views.results, name='results')
    path('create-answers/', views.create_answers, name='create_answers'),
    path('reponn/<slug>', views.reponn, name='reponn'),
    
]