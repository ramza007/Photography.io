from django.db import models

# -----------Location Model-----------


class Location(models.Model):
    Location = models.CharField(max_length=30)

    def __str__(self):
        return self.Location

# -----------Timeshot Model-----------


class Timeshot(models.Model):
    Timeshot = models.CharField(max_length=30)

    def __str__(self):
        return self.Timeshot

# -----------Details Model-----------


class Details(models.Model):
    Details = models.CharField(max_length=200)

    def __str__(self):
        return self.Details

# -----------Image Model-----------


class Image(models.Model):
    image = models.ImageField(upload_to='photos/', null=True)
    image_name = models.CharField(max_length=30)
    image_caption = models.TextField(max_length=100, null=True, blank=True)

    def save_image(self):
        '''Method to save an image in the database'''
        self.save()

    def delete_image(self):
        ''' Method to delete an image from the database'''
        self.delete()

    def __str__(self):
        return self.image_name

    @classmethod
    def get_images(cls):
        '''
        Method that gets all image posts from the database
        Returns:
            images : list of image post objects from the database
        '''
        images = Image.objects.all()
        return images

        return Image.objects.all()