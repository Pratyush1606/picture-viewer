from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import redirect

from pic_app.models import Image
from pic_app.serializers import ImageSerializer
from pic_app.pagination import CustomPagination, MyPaginationMixin


class imageList(APIView, MyPaginationMixin):

    pagination_class = CustomPagination
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        query = request.GET.get("query", None)
        if(not query):
            images = Image.objects.all()
            page = self.paginate_queryset(images)
            if page is not None:
                serializers = ImageSerializer(page, many=True)
                image_response = self.get_paginated_response(serializers.data)
            
            return Response(image_response.data, template_name="image_list.html", status=status.HTTP_200_OK)
        
        # Sending a list of images whose name match with the query
        images = Image.objects.filter(ImgName=query)
        serializers = ImageSerializer(images, many=True)
        data = {
            "results": serializers.data,
            "query": query
        }
        return Response(data, template_name="image_list.html", status=status.HTTP_200_OK)
        
    def post(self, request):
        data = {
            "ImgName": request.data.get("ImgName"),
            "ImgURL": request.data.get("ImgURL"),
            "ImgDetails": request.data.get("ImgDetails")
        }
        serializer = ImageSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
        return redirect("pic_app:imageList")
    
class imageDetail(APIView):

    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, id):
        try:
            image = Image.objects.get(id=id)
        except Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ImageSerializer(image)
        return Response({"image": serializer.data}, template_name="image_detail.html", status=status.HTTP_200_OK)

class imageDelete(APIView):

    def delete(self, request, id):
        try:
            image = Image.objects.get(id=id)
        except Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        image.delete()
        return JsonResponse({"status": "Success"})

class imageAdd(APIView):

    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        return Response(template_name="image_add.html", status=status.HTTP_200_OK)

class imageEdit(APIView):

    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, id):
        try:
            image = Image.objects.get(id=id)
        except Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ImageSerializer(image)
        return Response({"image": serializer.data}, template_name="image_edit.html", status=status.HTTP_200_OK)
    
    def put(self, request, id):
        try:
            image = Image.objects.get(id=id)
        except Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data = {
            "ImgName": request.data.get("ImgName"),
            "ImgURL": request.data.get("ImgURL"),
            "ImgDetails": request.data.get("ImgDetails")
        }
        serializer = ImageSerializer(image, data, partial=True)
        if(serializer.is_valid()):
            serializer.save()
        return JsonResponse({"status": "passed"})
        

