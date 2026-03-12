from .models import Recipe, RecipeImage
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RecipeForm, RecipeImageForm


class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes_list.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe.html'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_form.html'


class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    form_class = RecipeImageForm
    template_name = 'recipe_image_form.html'
