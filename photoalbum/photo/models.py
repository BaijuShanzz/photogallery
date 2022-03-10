from django.db import models


# Create your models here.
# category tables
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

# product table
class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='images', null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.description

    # @property
    # def imageURL(self):
    #     try:
    #         img = self.image.url
    #     except:
    #         img = ''
    #     return img
