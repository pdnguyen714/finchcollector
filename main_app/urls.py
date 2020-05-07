from django.urls import path
from . import views

urlpatterns = [
    path('',                       views.home,                 name='home'),
    path('about/',                 views.about,                name='about'),
    path('games/',                 views.games_index,          name='index'),
    path('games/<int:game_id>',    views.games_detail,         name='games_detail'),
    path('games/create/',          views.GameCreate.as_view(), name='games_create'),
    path('games/<int:pk>/update/', views.GameUpdate.as_view(), name='games_update'),
    path('games/<int:pk>/delete/', views.GameDelete.as_view(), name='games_delete'),
    path('games/<int:game_id>/add_supporting/', views.add_supporting, name='add_supporting'),
    path('games/<int:game_id>/assoc_award/<int:award_id>/', views.assoc_award, name='assoc_award'),
    path('awards/', views.AwardList.as_view(), name='awards_index'),
    path('awards/<int:pk>/', views.AwardDetail.as_view(), name='awards_detail'),
    path('awards/create/', views.AwardCreate.as_view(), name='awards_create'),
    path('awards/<int:pk>/update/', views.AwardUpdate.as_view(), name='awards_update'),
    path('awards/<int:pk>/delete/', views.AwardDelete.as_view(), name='awards_delete'),
]