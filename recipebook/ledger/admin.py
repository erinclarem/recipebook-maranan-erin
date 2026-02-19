from django.contrib import admin
from .models import Recipe, RecipeIngredient
# Register your models here.

class TaskInline(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [TaskInline,]

admin.site.register(Recipe, RecipeAdmin)
