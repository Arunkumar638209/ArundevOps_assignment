# library/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Ebook
from .forms import EbookForm

def ebook_list(request):
    ebooks = Ebook.objects.all()
    return render(request, 'library/ebook_list.html', {'ebooks': ebooks})

def ebook_detail(request, ebook_id):
    ebook = get_object_or_404(Ebook, id=ebook_id)
    return render(request, 'library/ebook_detail.html', {'ebook': ebook})

def upload_ebook(request):
    if request.method == 'POST':
        form = EbookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ebook_list')
    else:
        form = EbookForm()
    return render(request, 'library/upload_ebook.html', {'form': form})
