from django.urls import path
from cadastro import views

urlpatterns = [
    path('', views.index, name='index'),
    path('artistas/', views.ArtistaListView.as_view(), name='artistas'),
    path('artista/<int:pk>', views.ArtistaDetailView.as_view(), name='artista-detalhes'),
    path('artista/create/', views.ArtistaCreateView.as_view(), name='artista-create'),
    path('autor/<int:pk>/update/', views.ArtistaUpdateView.as_view(), name='artista-update'),
    path('autor/<int:pk>/delete/', views.ArtistaDeleteView.as_view(), name='artista-delete'),

    path('musicas/', views.MusicaListView.as_view(), name='musicas'),
    path('musica/<int:pk>', views.MusicaDetailView.as_view(), name='musica-detalhes'),
    path('musica/create/', views.MusicaCreateView.as_view(), name='musica-create'),
    path('autor1/<int:pk>/update/', views.MusicaUpdateView.as_view(), name='musica-update'),
    path('autor1/<int:pk>/delete/', views.MusicaDeleteView.as_view(), name='musica-delete'),

    path('albuns/', views.AlbumListView.as_view(), name='albuns'),
    path('album/<int:pk>', views.AlbumDetailView.as_view(), name='album-detalhes'),
    path('album/create/', views.AlbumCreateView.as_view(), name='album-create'),
    path('autor2/<int:pk>/update/', views.AlbumUpdateView.as_view(), name='album-update'),
    path('autor2/<int:pk>/delete/', views.AlbumDeleteView.as_view(), name='album-delete'),
]
