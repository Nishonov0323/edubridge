from django.shortcuts import get_object_or_404, render

from .models import Module


def home(request):
    modules = Module.objects.all()
    return render(request, 'handbook/home.html', {'modules': modules})


def module_detail(request, number):
    modules = Module.objects.all()
    module = get_object_or_404(Module, number=number)
    exercises = module.exercises.all()
    has_answers = any(exercise.answer for exercise in exercises)
    template_name = f'handbook/module_{number}.html'
    return render(
        request,
        template_name,
        {
            'module': module,
            'modules': modules,
            'exercises': exercises,
            'has_answers': has_answers,
        },
    )


def integration(request):
    modules = Module.objects.all()
    return render(request, 'handbook/integration.html', {'modules': modules})
