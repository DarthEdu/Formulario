from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import VenueForm


def inicio(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/inicio?submitted=True")
        else:
            form = VenueForm
            if 'submitted' in request.GET:
                submitted = True

    form = VenueForm
    return render(request, 'paginas/inicio.html', {'form': form, 'submitted': submitted})


def nosotros(request):
    return render(request, 'paginas/nosotros.html')
