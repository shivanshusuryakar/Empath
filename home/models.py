from django.db import models


class Imagemodel(models.Model):
    faceimg=models.ImageField(upload_to="testing/images")
