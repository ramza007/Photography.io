from django.db import models

# -----------Location Model-----------


class Location(models.Model):
    Location = models.CharField(max_length=30)

    def __str__(self):
        return self.Location

    def save_editor(self):
        self.save()

    @classmethod
    def location_taken(cls):
        shot = Location.objects.all()
        return shot

# -----------Timeshot Model-----------


class Timeshot(models.Model):
    Timeshot = models.CharField(max_length=30)

    def __str__(self):
        return self.Timeshot

    def save_editor(self):
        self.save()

    @classmethod
    def times_time(cls):
        time = Timeshot.objects.all()
        return time
# -----------Details Model-----------


class Details(models.Model):
    Details = models.TextField(max_length=200)

    def __str__(self):
        return self.Details

    def save_editor(self):
        self.save()

# -----------Image Model-----------


class Portraits(models.Model):
    image = models.ImageField(upload_to='photos/', null=True)
    image_name = models.CharField(max_length=30)
    image_caption = models.TextField(max_length=300, null=True, blank=True)
    location = models.CharField(max_length=30,
                                null=True,
                                blank=True)
    timeshot = models.CharField(max_length=20,
                                null=True,
                                blank=True)

    # class Meta:
    #     ordering = ['-date_uploaded']

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


# -----------Landscape Model-----------

class Landscape(models.Model):
    image = models.ImageField(upload_to='photos/landscapes', null=True)
    site = models.CharField(max_length=30)
    image_description = models.TextField(max_length=300, null=True, blank=True)
    location = models.CharField(max_length=30,null=True, blank=True)
    timeshot = models.CharField(max_length=20, null=True,blank=True)

    def save_image(self):
        '''Method to save an image in the database'''
        self.save()

    def delete_image(self):
        ''' Method to delete an image from the database'''
        self.delete()

    def __str__(self):
        return self.site

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


# -----------End of Landscape Model-----------


# -----------Arcitecture Model-----------


class Architecture(models.Model):
    image = models.ImageField(upload_to='photos/architecture', null=True)
    name = models.CharField(max_length=30)
    image_description = models.TextField(max_length=300, null=True, blank=True)
    location = models.CharField(max_length=30, null=True, blank=True)
    timeshot = models.CharField(max_length=20, null=True, blank=True)

    def save_image(self):
        '''Method to save an image in the database'''
        self.save()

    def delete_image(self):
        ''' Method to delete an image from the database'''
        self.delete()

    def __str__(self):
        return self.name

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


# -----------End of Architecture Model-----------


# -----------Email Model-----------

class NewsletterRecepients(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.name