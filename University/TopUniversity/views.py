from django.http import JsonResponse, HttpRequest
import requests

def get_data(city):
    url = f"https://jsonmock.hackerrank.com/api/universities?city={city}"
    response_data = requests.get(url)
    data = response_data.json()
    return data

def higheststudent(city):
    maxi = 0
    maxstu = None

    # Iterate through universities in the city data
    for university in city['data']:
        international_students = int(university['international_students'].replace(',', ''))
        if international_students > maxi:
            maxi = international_students
            maxstu = university
    return maxstu

def my_view(request, firstcity, seccity):
    findone = get_data(firstcity)
    findtwo = get_data(seccity)

    firstcityuni = higheststudent(findone)
    seccityuni = higheststudent(findtwo)

    if firstcityuni['international_students'] > seccityuni['international_students']:
        return JsonResponse({'university_with_high_no_of_internationaltu': firstcityuni['international_students']})
    else:
        return JsonResponse(seccityuni)






