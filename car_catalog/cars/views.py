from rest_framework.views import APIView
from .serializers import MyModelSerializer
from .models import Car
from rest_framework.response import Response

class MyModelAPIView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Car.objects.all()
        serializer = MyModelSerializer(queryset, many=True)
        return Response(serializer.data)


class SearchView(APIView):
    def get(self, request):
        query = request.query_params.get('q')
        articles = Car.objects.filter(title__icontains=query)
        serializer = MyModelSerializer(articles, many=True)
        return Response(serializer.data)