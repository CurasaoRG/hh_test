from django.shortcuts import render
from .forms import GuessForm
from .guess import GuessColor


def index(request):
    g = GuessColor()
    if request.method == 'POST':
        form = GuessForm(request.POST)
        submitbutton = request.POST.get("OK")
        print(form.is_valid())
        if form.is_valid():
            parameter_n = form.cleaned_data["parameter_n"]
            result = g.check(parameter_n)
            context = {'form': form, 'parameter_n': parameter_n,
                       'submitbutton': submitbutton, 'result': result[1], 'guess': result[0]}
            return render(request, 'guess/index.html', context)
    else:
        form = GuessForm()
    return render(request, 'guess/index.html', {'form': form})
