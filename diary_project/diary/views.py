from django.shortcuts import render, get_object_or_404
from .models import Entry


# Create your views here.
def entry_list(request):
    entries = Entry.objects.order_by("created")
    return render(request, 'diary/entry_list.html', {'entries': entries})

def entry_detail(request, id):
    entry = get_object_or_404(Entry, id=id)
    return render(request,  'diary/entry_detail.html', {'entry': entry})