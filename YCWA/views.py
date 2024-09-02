from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .forms import EntryForm
from .models import Entry


def create_entire(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('create_entire')
            except Exception as e:
                form.add_error(None, str(e))
        else:
            form.add_error(None, "Invalid form data")
    else:
        form = EntryForm()

    entries = Entry.objects.all().order_by('-created_at')
    paginator = Paginator(entries, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'YCWA/main-page.html', context={'form': form, 'entries': entries, 'page_obj': page_obj})


def get_new_entries(request: HttpRequest) -> JsonResponse:
    last_id = request.GET.get('last_id', 0)
    new_entries = Entry.objects.filter(id__gt=last_id).order_by('-created_at')

    entries_data = []
    for entry in new_entries:
        entries_data.append({
            'id': entry.id,
            'content': entry.content,
            'created_at': entry.created_at.isoformat(),
        })

    return JsonResponse({'entries': entries_data})


@user_passes_test(lambda u: u.is_superuser)
def delete_all_entries(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        Entry.objects.all().delete()
        return redirect('create_entire')
    return render(request, 'YCWA/delete_all.html')
