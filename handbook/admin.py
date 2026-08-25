from django.contrib import admin

from .models import Exercise, Module


class ExerciseInline(admin.TabularInline):
    model = Exercise
    extra = 1
    fields = ('order', 'group_label', 'prompt', 'answer')


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'accent', 'order')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ExerciseInline]


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('module', 'order', 'group_label', 'prompt')
    list_filter = ('module',)
