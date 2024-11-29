from django.shortcuts import render
from django.http import Http404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import CarModel


def index(request):
    return render(request, 'cars/index.html', {})


def gallery(request):
    cars = CarModel.objects.all().order_by("id")
    page_number = request.GET.get("page", 1)
    paginator = Paginator(cars, per_page=15)

    page_obj = None
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    context = {
        "page": {
            "has_previous": page_obj.has_previous(),
            "current": page_obj.number,
            "has_next": page_obj.has_next(),
        },
        "cars": page_obj.object_list,
        "page_obj": page_obj,
    }
    return render(request, 'cars/gallery.html', context)


def car_detail_view(request, car_id):
    try:
        context = {
            'car': CarModel.objects.get(id=car_id)
        }
    except CarModel.DoesNotExist:
        raise Http404("Details Not Found")
    return render(request, 'cars/car_detail.html', context)
