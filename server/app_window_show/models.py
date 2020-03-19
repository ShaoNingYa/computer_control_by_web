from django.db import models

# Create your models here.
class click_message(models.Model):
    position = models.CharField(max_length=30)
    isClicked = models.BooleanField()
    create_time = models.DateTimeField(auto_now_add=True)
