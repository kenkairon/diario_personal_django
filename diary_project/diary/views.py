from django.shortcuts import render
from .models import Entry

# Create your views here.
def entry_list(request):
    entries = Entry.objects.order_by("created")
    return render(request, 'diary/entry_list.html', {'entries': entries})
