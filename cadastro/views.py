from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from cadastro.models import Artista, Musica, Album

def index(request):

# Contando o número de livros e exemplares:
    num_artistas = Artista.objects.all().count()
    num_musicas = Musica.objects.all().count()
    num_albuns = Album.objects.all().count()

    contexto = {
        'num_artistas': num_artistas,
        'num_musicas': num_musicas,
        'num_albuns': num_albuns,
    }

    # Renderizando o template index.html com os dados da variável contexto:
    return render(request, 'index.html', context=contexto)

class ArtistaListView(generic.ListView):
    model = Artista

class ArtistaDetailView(generic.DetailView):
    model = Artista

class ArtistaCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ''
    model = Artista
    fields = '__all__'

class ArtistaUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ''
    model = Artista
    fields = ['nome', 'categoria', 'data_nascimento']

class ArtistaDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ''
    model = Artista
    success_url = '/'



class MusicaListView(generic.ListView):
    model = Musica

class MusicaDetailView(generic.DetailView):
    model = Musica

class MusicaCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ''
    model = Musica
    fields = '__all__'

class MusicaUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ''
    model = Musica
    fields = ['nome','data_lancamento', 'nota']

class MusicaDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ''
    model = Musica
    success_url = '/'



class AlbumListView(generic.ListView):
    model = Album

class AlbumDetailView(generic.DetailView):
    model = Album

class AlbumCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ''
    model = Album
    fields = '__all__'

class AlbumUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ''
    model = Album
    fields = ['nome', 'data_lancamento', 'nota']

class AlbumDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ''
    model = Album
    success_url = '/'
