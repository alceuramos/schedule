from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Activity
from .forms import ActivityForm
# Create your views here.

def index(request):
    activities_list = Activity.objects.order_by('create_date')
    context = {
        'activities_list':activities_list,
    }
    return render(request, 'activities/index.html', context)

def detail(request,activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    return render(request,'activities/detail.html',{'activity': activity})

def exclude(request,activity_id):
    # activity = get_object_or_404(Activity, pk=activity_id)
    activity = Activity.objects.get(pk=activity_id)
    activity.delete()
    activities_list = Activity.objects.order_by('create_date')
    return render(request,'activities/index.html',{'activities_list':activities_list,})
def add_activity(request):
    form = ActivityForm()
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/detail/{{}}')
        else:
            print(form.errors)
    return render(request, 'rango/add_category.html', {'form': form})