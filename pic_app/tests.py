import json
from django.urls import reverse
from rest_framework.test import APITestCase

from pic_app.serializers import *

class ImageModelViewTest(APITestCase):
    def setUp(self):
        data = {
            "ImgName": "Picture 1",
            "ImgURL": "https://images.pexels.com/photos/3573382/pexels-photo-3573382.jpeg",
            "ImgDetails": "An evening Pic!"
        }
        img = Image.objects.create(**data)
    
    def testGetImageList(self):
        response = self.client.get(reverse("pic_app:imageList"))
        self.assertEqual(response.status_code, 200)

        data = response.data
        # There should be 1 image in the list
        self.assertEqual(len(data["results"]), 1)
        # Checking the data of that image
        self.assertEqual(data["results"][0]["id"], 1)
        self.assertEqual(data["results"][0]["ImgName"], "Picture 1")
        self.assertEqual(data["results"][0]["ImgURL"], "https://images.pexels.com/photos/3573382/pexels-photo-3573382.jpeg")
        self.assertEqual(data["results"][0]["ImgDetails"], "An evening Pic!")
        
    def testPagination(self):
        # First Populating Database with more than one image
        for i in range(2, 11):
            data = {
                "ImgName": "Picture {}".format(i),
                "ImgURL": "https://images.pexels.com/photos/3573382/pexels-photo-3573382.jpeg",
                "ImgDetails": "An evening Pic!"
            }
            img = Image.objects.create(**data)
        
        # Checking all the entries
        self.assertEqual(Image.objects.count(), 10)

        # Making a request
        response = self.client.get(reverse("pic_app:imageList"))
        self.assertEqual(response.status_code, 200)

        data = response.data
        # There should be 9 images in the list (page size is 9)
        self.assertEqual(len(data["results"]), 9)
    
    def testImageSearch(self):
        # Searching with an existing image name in database
        parameter = {
            "query": "Picture 1"
        }
        response = self.client.get(reverse("pic_app:imageList"), parameter)
        self.assertEqual(response.status_code, 200)

        data = response.data
        # There should be 1 image in the list
        self.assertEqual(len(data["results"]), 1)
        # Checking the data of that image
        self.assertEqual(data["results"][0]["id"], 1)
        self.assertEqual(data["results"][0]["ImgName"], "Picture 1")
        self.assertEqual(data["results"][0]["ImgURL"], "https://images.pexels.com/photos/3573382/pexels-photo-3573382.jpeg")
        self.assertEqual(data["results"][0]["ImgDetails"], "An evening Pic!")
   
    def testPostImage(self):
        # Checking that there should be only 1 entry in db
        self.assertEqual(Image.objects.count(), 1)
        # Posting an Image
        data = {
            "ImgName": "Picture 2",
            "ImgURL": "https://images.pexels.com/photos/3573382/pexels-photo-3573382.jpeg",
            "ImgDetails": "An evening Pic!"
        }
        response = self.client.post(reverse("pic_app:imageList"), json.dumps(data), content_type="application/json")
        # There should be 2 entries in db
        self.assertEqual(Image.objects.count(), 2)

    def testPutImage(self):
        # Checking before updating
        data = ImageSerializer(Image.objects.get(id=1)).data
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["ImgName"], "Picture 1")
        self.assertEqual(data["ImgURL"], "https://images.pexels.com/photos/3573382/pexels-photo-3573382.jpeg")
        self.assertEqual(data["ImgDetails"], "An evening Pic!")

        # Updating this Image
        data = {
            "ImgName": "Picture 1",
            "ImgURL": "https://images.pexels.com/photos/3573382/pexels-photo-3573382.jpeg",
            "ImgDetails": "Picture 1 updated"
        }
        response = self.client.put(reverse("pic_app:imageEdit", args=[1]), json.dumps(data), content_type="application/json")
        
        # Checking if the image got updated
        data = ImageSerializer(Image.objects.get(id=1)).data
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["ImgName"], "Picture 1")
        self.assertEqual(data["ImgURL"], "https://images.pexels.com/photos/3573382/pexels-photo-3573382.jpeg")
        self.assertEqual(data["ImgDetails"], "Picture 1 updated")