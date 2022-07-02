from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views import generic

from backend.models import Switch


class IndexView(generic.ListView):
    template_name = 'frontend/index.html'
    context_object_name = 'switch_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Switch.objects.all()