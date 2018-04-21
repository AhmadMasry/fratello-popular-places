from django.http import HttpResponse
from django.shortcuts import render
import populartimes
from populartimes.crawler import PopulartimesException


def index(request):
    return HttpResponse("Hello World")


def detail(request):
    place_id = request.POST.get('place_id',False)

    if place_id:
        try:
            place_detail = populartimes.get_id(api_key='AIzaSyAgC34k4v02u41pDEbljVkrn9WgiqUiJ5M',
                                               place_id=place_id)
            return render(request, 'check_popular_places/detail.html', place_detail)
        except PopulartimesException as e:
            return render(request, 'check_popular_places/detail.html', {
                'error_message': e.message + " Please Enter a Place ID.",
            })

    else:
        return render(request, 'check_popular_places/detail.html', {
            'error_message': "Please Enter a Place ID.",
        })

