from django.urls import path
from dinner import views

urlpatterns = [
	path('', views.index, name='index'),
	path('chits/', views.ChitListView.as_view(), name='chits'),
	path('delete_chit/<int:id>', views.delete_chit, name='delete_chit'),
]