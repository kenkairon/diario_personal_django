from django.shortcuts import render, get_object_or_404, redirect
from .models import Entry
from .forms import EntryForm

# Create your views here.
def entry_list(request):
    entries = Entry.objects.order_by("created")
    return render(request, 'diary/entry_list.html', {'entries': entries})

def entry_detail(request, id):
    entry = get_object_or_404(Entry, id=id)
    return render(request,  'diary/entry_detail.html', {'entry': entry})

def entry_create(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('entry-list')
    else:
        form = EntryForm()
    return render(request, 'diary/entry_create.html', {'form': form})