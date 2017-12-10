from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import LocationForm
from .models import Location

def index(request):
  context = {}
  context['location_form'] = LocationForm()
  context['locations'] = Location.objects.order_by('-time_updated')
  return render(request, 'locator/index.html', context)

def update_location(request):
  if request.method == 'POST':
    form = LocationForm(request.POST)
    if form.is_valid():
      Location.objects.update_or_create(user=request.user,
        defaults={'location': form.cleaned_data['location']})
  return HttpResponseRedirect(reverse('locator:index'))
