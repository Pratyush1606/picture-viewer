from rest_framework import serializers
from pic_app.models import Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'ImgName', 'ImgURL', 'ImgDetails')
