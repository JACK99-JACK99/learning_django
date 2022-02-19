from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class Testview(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'student1': {'name': 'jitndra',
                         'age': 69,
                         'college': ',mbgpg',
                         'roll_no': 2001320251,
                         'college_id': 1947347
                         },

            'student2': {'name': 'jitndra',
                         'age': 69,
                         'college': ',mbgpg',
                         'roll_no': 2001320251,
                         'college_id': 1947347
                         }
        }
        return Response(data)


# def test_veiw(request):
#     data = {
#         'name':'jitndra',
#         'age':69
#     }
#     return JsonResponse(data)
    # return render(request, "index.html", {'name': 'krishan'})
    # return HttpResponse('Hello world')
