from django.db import models

# Create your models here.
class s1(models.Model):
    name=models.CharField(max_length=200)
    class Meta:
        db_table="con"