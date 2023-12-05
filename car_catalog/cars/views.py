from rest_framework.views import APIView
from .serializers import MyModelSerializer
from .models import Car
from rest_framework.response import Response
from rest_framework import status


class MyModelAPIView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Car.objects.all()
        serializer = MyModelSerializer(queryset, many=True)
        return Response(serializer.data)


    def post(self, request, *args, **kwargs):
        serializer = MyModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk, *args, **kwargs):
        car = self.get_object(pk)
        serializer = MyModelSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, *args, **kwargs):
        car = self.get_object(pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SearchView(APIView):
    def get(self, request):
        query = request.query_params.get('q')
        articles = Car.objects.filter(title__icontains=query)
        serializer = MyModelSerializer(articles, many=True)
        return Response(serializer.data)


