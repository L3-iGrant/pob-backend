from django.db import models

# Create your models here.

class Requirement(models.Model):
    id = models.BigIntegerField(primary_key=True,unique = True)
    category = models.CharField(max_length=256)
    requirement_header = models.CharField(max_length=256)
    requirement_description = models.CharField(max_length=256)
    requirement_category = models.CharField(max_length=256)
    def __str__(self):
        return self.category

class Tender(models.Model):
    class STATUS(models.TextChoices):
        DRAFT = "DRAFT", "Draft"
        ISSUER = "PUBLISHED", "Published"
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=16, choices=STATUS.choices, default=STATUS.DRAFT)
    requirement_1 = models.ForeignKey(Requirement, on_delete=models.CASCADE, related_name= "requirement1")
    requirement_2 = models.ForeignKey(Requirement, on_delete=models.CASCADE, related_name= "requirement2")
    def __str__(self):
        return self.name