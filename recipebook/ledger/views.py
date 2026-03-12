from .models import Recipe, RecipeImage
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from .forms import RecipeForm, RecipeImageForm
from django.urls import reverse_lazy


class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes_list.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = RecipeImage.objects.filter(recipe=self.object)
        return context


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_form.html'


class RecipeImageUploadView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    form_class = RecipeImageForm
    template_name = 'recipe_image_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context

    def get_success_url(self):
        return reverse_lazy('ledger:recipe_detail', kwargs={'pk': self.kwargs['pk']})

    def post(self, request, *args, **kwargs):
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.recipe_id = self.kwargs['pk']
            form.save()
        return redirect(self.get_success_url())
