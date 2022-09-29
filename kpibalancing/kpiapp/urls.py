from django.urls import path
from . import views
from django.views.generic import RedirectView


urlpatterns = [
    path("", views.AddCardView, name='add_kpi'),
    path('test/', views.cards_update, name='test'),
    path("pivot/", views.FilteredPeopleListView.as_view(), name='pivot'),
    path('<int:pk>/update/', views.CardUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.CardDeleteView.as_view(), name='delete'),
    path("formset/", views.CardAddView.as_view(), name='add_formset'),

]

