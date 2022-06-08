from django.shortcuts import render
from .forms import EquationForm
from .solution import solution


def index(request):
    if request.method == 'POST':
        form = EquationForm(request.POST)
        submitbutton = request.POST.get("OK")
        print(form.is_valid())
        if form.is_valid():
            parameter_a = form.cleaned_data["parameter_a"]
            parameter_b = form.cleaned_data["parameter_b"]
            parameter_c = form.cleaned_data["parameter_c"]
            result = solution(parameter_a, parameter_b, parameter_c)
            context = {'form': form, 'parameter_a': parameter_a,
                       'parameter_b': parameter_b, 'submitbutton': submitbutton,
                       'parameter_c': parameter_c, 'result': result}
            return render(request, 'equation/new.html', context)
    else:
        form = EquationForm()
    return render(request, 'equation/new.html', {'form':form})