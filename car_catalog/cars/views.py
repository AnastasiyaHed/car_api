# # # from rest_framework.views import APIView
# # # from .serializers import MyModelSerializer
# # # from .models import Car
# # # from rest_framework.response import Response
# # # from rest_framework import status
# # # from rest_framework.parsers import MultiPartParser, FormParser
# # #
# # #
# # #
# # # class MyModelAPIView(APIView):
# # #     def get(self, request, *args, **kwargs):
# # #         queryset = Car.objects.all()
# # #         serializer = MyModelSerializer(queryset, many=True)
# # #         return Response(serializer.data)
# # #
# # #
# # #     def post(self, request, *args, **kwargs):
# # #         serializer = MyModelSerializer(data=request.data)
# # #         if serializer.is_valid():
# # #             serializer.save()
# # #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# # #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# # #
# # #
# # #     def put(self, request, pk, *args, **kwargs):
# # #         car = self.get_object(pk)
# # #         serializer = MyModelSerializer(car, data=request.data)
# # #         if serializer.is_valid():
# # #             serializer.save()
# # #             return Response(serializer.data)
# # #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# # #     def delete(self, request, pk, *args, **kwargs):
# # #         car = self.get_object(pk)
# # #         car.delete()
# # #         return Response(status=status.HTTP_204_NO_CONTENT)
# # #
# # #
# # # class SearchView(APIView):
# # #     def get(self, request):
# # #         query = request.query_params.get('q')
# # #         articles = Car.objects.filter(title__icontains=query)
# # #         serializer = MyModelSerializer(articles, many=True)
# # #         return Response(serializer.data)
# # #
# # #
# # from rest_framework.views import APIView
# # from .serializers import MyModelSerializer
# # from .models import Car
# # from rest_framework.response import Response
# # from rest_framework import status
# # from rest_framework.parsers import MultiPartParser, FormParser
# #
# # class MyModelAPIView(APIView):
# #     parser_classes = [MultiPartParser, FormParser]
# #
# #     def get_object(self, pk):
# #         try:
# #             return Car.objects.get(pk=pk)
# #         except Car.DoesNotExist:
# #             raise Http404
# #
# #     def get(self, request, *args, **kwargs):
# #         queryset = Car.objects.all()
# #         serializer = MyModelSerializer(queryset, many=True)
# #         return Response(serializer.data)
# #
# #     def post(self, request, *args, **kwargs):
# #         serializer = MyModelSerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# #
# #     def put(self, request, pk, *args, **kwargs):
# #         car = self.get_object(pk)
# #         serializer = MyModelSerializer(car, data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# #
# #     def delete(self, request, pk, *args, **kwargs):
# #         car = self.get_object(pk)
# #         car.delete()
# #         return Response(status=status.HTTP_204_NO_CONTENT)
# #
# # class SearchView(APIView):
# #     def get(self, request):
# #         query = request.query_params.get('q')
# #         cars = Car.objects.filter(make__icontains=query) | Car.objects.filter(model__icontains=query)
# #         serializer = MyModelSerializer(cars, many=True)
# #         return Response(serializer.data)
# #
# #
#
# from rest_framework.views import APIView
# from .serializers import MyModelSerializer
# from .models import Car
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.parsers import MultiPartParser, FormParser
#
# class MyModelAPIView(APIView):
#     parser_classes = [MultiPartParser, FormParser]
#
#     def get_object(self, pk):
#         try:
#             return Car.objects.get(pk=pk)
#         except Car.DoesNotExist:
#             raise Http404
#
#     def get(self, request, *args, **kwargs):
#         queryset = Car.objects.all()
#         serializer = MyModelSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, *args, **kwargs):
#         serializer = MyModelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, pk, *args, **kwargs):
#         car = self.get_object(pk)
#         serializer = MyModelSerializer(car, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, *args, **kwargs):
#         car = self.get_object(pk)
#         car.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
# class SearchView(APIView):
#     def get(self, request):
#         query = request.query_params.get('q')
#         cars = Car.objects.filter(make__icontains=query) | Car.objects.filter(model__icontains=query)
#         serializer = MyModelSerializer(cars, many=True)
#         return Response(serializer.data)

from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import MyModelSerializer
from .models import Car
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import HttpResponse
from django.views.generic import View
import pandas as pd

class MyModelAPIView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get_object(self, pk):
        try:
            return Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            raise Http404

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

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            car = self.get_object(pk)
            car.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class SearchView(APIView):
    def get(self, request):
        query = request.query_params.get('q')
        cars = Car.objects.filter(make__icontains=query) | Car.objects.filter(model__icontains=query)
        serializer = MyModelSerializer(cars, many=True)
        return Response(serializer.data)

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = MyModelSerializer


class ExportExcelView(View):
    def get(self, request, *args, **kwargs):
        # Получаем данные из базы данных
        queryset = Car.objects.all()

        # Преобразуем данные в DataFrame
        data = {
            'Make': [car.make for car in queryset],
            'Model': [car.model for car in queryset],
            'Year': [car.year for car in queryset],
            'Price': [car.price for car in queryset],
        }
        df = pd.DataFrame(data)

        # Создаем response и записываем DataFrame в Excel
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=cars.xlsx'
        df.to_excel(response, index=False, engine='openpyxl')

        return response