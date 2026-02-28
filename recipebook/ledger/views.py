from .models import Recipe
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes_list.html'


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe.html'
